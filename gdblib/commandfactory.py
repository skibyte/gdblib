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
from gdblib.cmd import *;

class CommandFactory():
    def createAddDirectoryCommand(self, directory):
        return AddDirectoryCommand(directory)

    def createChangeDirectoryCommand(self, directory):
        return ChangeDirectoryCommand(directory)

    def createInfoSourceCommand(self):
        return ListSourceFilesCommand()

    def createNextCommand(self):
        return NextCommand()

    def createStepCommand(self):
        return StepCommand()

    def createPrintCommand(self, expression):
        return PrintCommand(expression)

    def createAddBreakpointCommand(self, filename, line):
        return AddBreakpointCommand(filename, line)

    def createDeleteBreakpointCommand(self, number):
        return DeleteBreakpointCommand(number)

    def createAddWatchPointCommand(self):
        return AddWatchpointCommand()

    def createDeleteWatchPointCommand(self):
        return DeleteWatchpointCommand()

    def createRunCommand(self,arguments):
        return RunCommand(arguments)

    def createBacktraceCommand(self):
        return BacktraceCommand()

    def createReturnCommand(self):
        return ReturnCommand()

    def createInfoBreakpointCommand(self):
        return InfoBreakpointCommand()
