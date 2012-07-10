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
from gdblib.log import Logger
class DefaultCommand():
    completed = False
    log = Logger("DefaultCommand")

    def accept(self,visitor):
        visitor.visitDefaultCommand(self)

    def setCompleted(self,value):
        self.completed = value
        if self.completed == True:
            self.log.info("Command completed: " + str(self.getValue()))

    def isComplete(self):
        return self.completed

    def getValue(self):
        return ''

class QuitCommand(DefaultCommand):
    def getValue(self):
        return 'quit\n'

class ClearCommand(DefaultCommand):
    def __init__(self, filename, line):
        self.filename = filename
        self.line = line

    def getValue(self):
        return "clear " + self.filename + ":" + str(self.line) + "\n"

class AddDirectoryCommand(DefaultCommand):
    def __init__(self, directory):
        self.directory = directory

    def getValue(self):
        return "-environment-directory " + self.directory +"\n"

    def accept(self,visitor):
        visitor.visitAddDirectoryCommand(self)


class ChangeDirectoryCommand(DefaultCommand):
    def __init__(self,directory):
        self.directory = directory

    def getValue(self):
        return "-environment-cd " + self.directory + "\n"

    def accept(self,visitor):
        visitor.visitChangeDirectoryCommand(self)

class ListSourceFilesCommand(DefaultCommand):
    def getValue(self):
        return "interpreter-exec mi \"-file-list-exec-source-files\"\n"    
    def getSourceFiles(self):    
        return self.sourcefiles

    def setSourceFiles(self,files):
        self.sourcefiles = files

    def accept(self,visitor):
        visitor.visitListSourceFilesCmd(self)


class AdvanceCommand(DefaultCommand):
    def accept(self,visitor):
        visitor.visitAdvanceCommand(self)

    def setLocation(self,location):
        self.location = location

    def getLocation(self):
        return self.location

class NextCommand(AdvanceCommand):
    def getValue(self):
        return "next\n"

class StepCommand(AdvanceCommand):
    def getValue(self):
        return "step\n"

class RunCommand(AdvanceCommand):
    def __init__(self, arguments):
        self.arguments = arguments

    def getValue(self):
        return "run " + self.arguments + "\n"

class BacktraceCommand(DefaultCommand):
    backtrace = None

    def getValue(self):
        return "backtrace\n"

    def getBacktrace(self):
        return self.backtrace

class PrintCommand(DefaultCommand):
    result = ''
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        visitor.visitPrintCommand(self)

    def setResult(self, result):
        self.result = result

    def getResult(self):
        return self.result

    def getValue(self):
        return "print " + self.expression + "\n"

class SetVarCommand(DefaultCommand):
    def __init__(self, variable, value):
        self.variable = variable 
        self.value = value

    def getValue(self):
        return "set var " + self.variable + "=" + self.value

class ReturnCommand(DefaultCommand):
    def getValue(self):
        return "return\n"

class ContinueCommand(DefaultCommand):
    def getValue(self):
        return "continue\n"

class FinishCommand(DefaultCommand):
    def getValue(self):
        return "finish\n"

class WhatIsCommand(DefaultCommand):
    def __init__(self,variable):
        self.variable = variable

    def getValue(self):
        return "whatis " + self.variable

class AddBreakpointCommand(DefaultCommand):
    def __init__(self,filename, line):
        self.filename = filename
        self.line = line
        self.breakpointAdded = None
    
    def getValue(self):
        command =  "break " + self.filename +":"+ str(self.line)+"\n"
        return command

    def setBreakpointAdded(self, breakpoint):
        self.breakpoint = breakpoint
    
    def getBreakpointAdded(self):
        return self.breakpoint

    def accept(self,visitor):
        visitor.visitAddBreakpointCommand(self)

class DeleteBreakpointCommand(DefaultCommand):
    def __init__(self, n):
        self.number = n

    def getValue(self):
        return 'delete ' + str(self.number) + '\n'

    def accept(self,visitor):
        visitor.visitDeleteBreakpointCommand(self)

class DeleteAllBreakpointsCommand(DefaultCommand):
    def getValue(self):
            return 'delete breakpoints\n'


class TtyCommand(DefaultCommand):
    def __init__(self, tty):
        self.tty = tty

    def getValue(self):
        return 'tty ' + self.tty + ' \n'

class AddWatchpointCommand(DefaultCommand):
    def __init__(self):
        pass

class DeleteWatchpointCommand(DefaultCommand):
    def __init__(self):
        pass

class InfoBreakpointCommand(DefaultCommand):
    def __init__(self):
        self.breakpoints = None

    # FIXME: Remove this comment.
    # This tests create a single definition of a thread command 
    # The most important aspect here is howto eliminate most of the leak
    # resources 
    def getValue(self):
        command = "info breakpoint\n"
        return command

    def setBreakpoints(self,breakpoints):
        self.breakpoints = breakpoints

    def getBreakpoints(self):
        return self.breakpoints

    def accept(self, visitor):
        visitor.visitInfoBreakpointCommand(self)

class TargetCommand(DefaultCommand):
    def __init__(self, host):
        self.host = host
        self.timeout = False

    def setTimeoutError(self, error):
        self.timeout = error

    def getTimeoutError(self):
        return self.timeout

    def getValue(self):
        return "target remote " + self.host + "\n"

    def accept(self, visitor):
        visitor.visitTargetRemoteCommand(self)

class SymbolFileCommand(DefaultCommand):
    def __init__(self, symbol):
        self.symbol = symbol

    def setSymbolFile(self, symbol):
        self.symbol = symbol

    def getSymbolFile(self):
        return self.symbol

    def getValue(self):
        return "symbol-file " + self.symbol + "\n"

    def accept(self, visitor):
        visitor.visitSymbolFileCommand(self)

class LoadCommand(DefaultCommand):
    def __init__(self, symbol):
        self.symbol = symbol

    def getValue(self):
        return "load " + self.symbol + "\n"
