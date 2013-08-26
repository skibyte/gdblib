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
from gdblib.gdbinterpreter import GDBInterpreter;
from gdblib.exceptions import CommandNotCompletedException
from gdblib.cmd import QuitCommand
from threading import Thread;
import threading;
import subprocess;
import time;
import platform
import os
from gdblib.completevisitor import CompleteVisitor;
from gdblib.log import Logger

class GDBServer(Thread):
    def __init__(self,process):
        Thread.__init__(self)
        self.working = True
        self.cmdcondition = threading.Condition()
        self.cmdSingle = threading.Condition()
        self.process = process
        self.interpreter = GDBInterpreter()
        self.output = ''
        self.currentcmd = None
        self.log = Logger("GDBServer")
        self.completevisitor = CompleteVisitor()

    def run(self):
        lineCondition = threading.Condition()
        while(self.working):
            line = self.process.stdout.readline()
            if platform.system() == 'Windows':
                line = line.replace(os.sep + os.sep + '', os.sep)
                line = line.replace('/', os.sep)
            self.log.info(line)
            self.output += line
            if self.currentcmd != None and not self.currentcmd.isComplete():
                self.completevisitor.setoutput(self.output)
                self.currentcmd.accept(self.completevisitor)

            if self.currentcmd != None and self.currentcmd.isComplete():
                self.cmdcondition.acquire()
                self.cmdcondition.notify()
                self.cmdcondition.release()
    
    def send(self,cmd):
        self.cmdSingle.acquire()
        self.output = ''
        self.currentcmd = cmd
        self.log.info("Write -> " + str(cmd.getValue()))
        self.cmdcondition.acquire()
        self.process.stdin.write(cmd.getValue())
        self.cmdcondition.wait(15)

        try:
            if self.currentcmd.isComplete() == True:
                self.interpreter.parse(self.currentcmd,self.output.split('\n')) 
        finally:
            self.cmdcondition.release()
            self.cmdSingle.release()


    # FIXME: Start gdb without confirmation questions
    def stopserver(self):
        self.output = ''
        self.process.stdin.write("quit\n")
        self.working = False
        
        
