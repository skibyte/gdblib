# 
# GdbLib - A Gdb python library.
# Copyright (C) 2012  Fernando Castillo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from gdblib.commandfactory import CommandFactory;
from gdblib.gdbserver import GDBServer;
from gdblib.gdbstate import GDBState;
from gdblib.log import Logger
from gdblib.exceptions import *

import subprocess;
import time;
from os import path;
# FIXME: Add support for core dumps
# FIXME: Add support for attaching into a process

class GDB():
    def __init__(self):
        self.core = False
        self.log = Logger("Gdb")
        self.factory = CommandFactory()
        self.state = GDBState()
        self.fileLocationListeners = []

    def connectApp(self, apppath):
        if self.isConnected() == True:
            raise AlreadyConnectedError()

        self.apppath = apppath
        arguments = ['gdb','-i','mi','-q',self.apppath]
        self.connect(arguments)
    
    def connectCore(self,apppath,corepath):
        if self.isConnected() == True:
            raise AlreadyConnectedError()
        self.apppath = apppath
        arguments = ['gdb','-i','mi','-q', self.apppath, corepath]
        self.connect(arguments)

    def connect(self,arguments):
        if self.isConnected() == True:
            raise AlreadyConnectedError()
        handle = open(self.apppath);
        handle.close();
        self.process = subprocess.Popen(arguments,
                shell=False,stdin=subprocess.PIPE,
                stdout = subprocess.PIPE)
        self.gdbserver = GDBServer(self.process)
        self.gdbserver.start()
        self.state.setConnected(True)
        self.changeDirectory(path.dirname(arguments[4])) 

    def addNewFileLocationListener(self, listener):
        self.fileLocationListeners.append(listener)

    def newFileLocationListeners(self):
        return self.fileLocationListeners

    def removeNewFileLocationListener(self, listener):
        self.fileLocationListeners.remove(listener)

    def setTty(self, tty):
        self.checkConnection();
        cmd = self.factory.createTtyCommand(tty)
        self.gdbserver.send(cmd)

    def addExitListener(self, listener):
        self.exitListeners.append(listener)

    def changeDirectory(self,directory):
        self.checkConnection();
        cmd = self.factory.createChangeDirectoryCommand(directory)
        self.gdbserver.send(cmd)

    def setCore(self,value):
        self.checkConnection();
        self.core = value

    def getSourceCodeFiles(self):
        self.checkConnection();
        cmd = self.factory.createInfoSourceCommand()
        self.gdbserver.send(cmd)
        return cmd.getSourceFiles()

    def addBreakpoint(self, filename, line):
        self.checkConnection();
        cmd = self.factory.createAddBreakpointCommand(filename,line)
        self.gdbserver.send(cmd)    

    def getBreakpoints(self):
        self.checkConnection();
        cmd  = self.factory.createInfoBreakpointCommand()
        self.gdbserver.send(cmd)
        breakpoints = cmd.getBreakpoints()

        files = self.getSourceCodeFiles()

        for b in breakpoints:
            for f in files:
                if b.getSourceFile() == f['file']:
                    b.setSourceFile(f['fullname'])
        
        return breakpoints

    def deleteBreakpoint(self, number):    
        self.checkConnection()
        cmd = self.factory.createDeleteBreakpointCommand(number)
        self.gdbserver.send(cmd)

    def deleteAllBreakpoints(self):
        self.checkConnection()
        cmd = self.factory.createDeleteAllBreakpointsCommand()
        self.gdbserver.send(cmd)

    def addWatchpoint(self):
        self.checkConnection();
    
    def deleteWatchpoint(self):
        self.checkConnection();
    
    def infoThreads(self):
        self.checkConnection();
    
    def addDirectory(self,directory):
        self.checkConnection();
        cmd = self.factory.createAddDirectoryCommand(directory)
        self.gdbserver.send(cmd)

    def checkConnection(self):
        if not self.isConnected():
            raise NotConnectedError("GDB must be connected before using this method");

    def run(self, arguments):
        self.checkConnection()
        cmd = self.factory.createRunCommand(arguments)
        self.gdbserver.send(cmd)
        location = cmd.getLocation()
        if location.has_key('fullname'):
            self.log.debug("Reporting new location: " + location['fullname'] +":"+str(location['line']))
            self.updateNewFileLocationListeners(location['fullname'], location['line'])
    
    def step(self):
        self.checkConnection();
        cmd = self.factory.createStepCommand()
        self.gdbserver.send(cmd)
        location = cmd.getLocation()
        if location.has_key('fullname'):
            self.log.debug("Reporting new location: " + location['fullname'] +":"+str(location['line']))
            self.updateNewFileLocationListeners(location['fullname'], location['line'])
    
    def next(self):
        self.checkConnection();
        cmd = self.factory.createNextCommand()
        self.gdbserver.send(cmd)
        location = cmd.getLocation()
        if location.has_key('fullname'):
            self.log.debug("Reporting new location: " + location['fullname'] +":"+str(location['line']))
            self.updateNewFileLocationListeners(location['fullname'], location['line'])

    def p(self, expression):
        self.checkConnection()
        cmd = self.factory.createPrintCommand(expression)
        self.gdbserver.send(cmd)
        value = cmd.getResult()
        return value

    def backtrace(self):
        self.checkConnection();
        cmd = self.factory.createBacktraceCommand()
        self.gdbserver.send(cmd)
        self.observer.printBacktrace(cmd.getBacktrace())

    def updateNewFileLocationListeners(self, newFile, newLine):
        for listener in self.fileLocationListeners:
            listener.newFileLocation(newFile, newLine)

    def finish(self):
        self.checkConnection();

    def until(self):
        self.checkConnection();

    def clear(self, filename, lineNumber):
        self.checkConnection();
        cmd = self.factory.createClearCommand(filename, lineNumber)
        self.gdbserver.send(cmd)

       
    def continueExecution(self):
        self.checkConnection();
        cmd = self.factory.createContinueCommand()
        self.gdbserver.send(cmd)


    def whatIs(self,variable):
        self.checkConnection();

    def setVar(self, variable, value):
        self.checkConnection();

    def jump(self):
        self.checkConnection();
    
    def call(self):
        self.checkConnection();

    def returnExecution(self):
        self.checkConnection();

    def getState(self):
        return self.state

    def disconnect(self):
        self.checkConnection();
        self.gdbserver.stopserver()
        self.state.setConnected(False)
        #self.monitor.destroy()

    def isConnected(self):
        return self.state.isConnected()

