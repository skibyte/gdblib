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
import gdblib.gdb;
from gdblib.gdbinterpreter import GDBInterpreter;
from threading import Thread;
import threading;
import subprocess;
import time;
from gdblib.completevisitor import CompleteVisitor;
from gdblib.log import Logger

class GDBServer(Thread):
    def __init__(self,app,process):
        Thread.__init__(self)
        self.app = app
        self.working = True
        self.cmdcondition = threading.Condition()
        self.process = process
        self.interpreter = GDBInterpreter()
        self.output = ''
        self.currentcmd = None
        self.log = Logger("GDBServer")
        self.completevisitor = CompleteVisitor()

    def __del__(self):
        if self.working:
            self.stopserver()

    def run(self):
        while(self.working):
            line = self.process.stdout.readline()
            self.log.debug(line)
            self.output += line
            if(self.currentcmd != None):
                self.completevisitor.setoutput(self.output.split('\n'))
                self.currentcmd.accept(self.completevisitor)

            if self.currentcmd == None or self.currentcmd.isComplete():
                self.cmdcondition.acquire()
                self.cmdcondition.notify()
                self.cmdcondition.release()
    
    def send(self,cmd):
        self.cmdcondition.acquire()
        self.output = ''
        self.currentcmd = cmd
        self.log.debug("Write -> " + str(cmd.getValue()))
        self.process.stdin.write(cmd.getValue())
        
        self.cmdcondition.wait()
        try:
            self.interpreter.parse(cmd,self.output.split('\n')) 
        finally:
            self.cmdcondition.release()



    # FIXME: Start gdb without confirmation questions
    def stopserver(self):
        self.working = False
        self.process.stdin.write("quit\n")
        
        
