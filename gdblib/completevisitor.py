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
class CompleteVisitor():
    def setoutput(self, output):
        self.output = output
        
    def visitOpenCommand(self,cmd):
        cmd.setCompleted(self.findstr('(gdb)',1))

    def visitDefaultCommand(self,cmd):
        for line in self.output:
            if line.find('done') or line.find('error'):
                cmd.setCompleted(True)
                return

    def visitAdvanceCommand(self,cmd):
        cmd.setCompleted(self.findstr('(gdb)',2))
        if not cmd.isComplete():
            cmd.setCompleted(self.findstr('^error',1))

    def visitAddDirectoryCommand(self,cmd):
        cmd.setCompleted(self.findstr('^done',1))

    def visitChangeDirectoryCommand(self,cmd):
        cmd.setCompleted(self.findstr('^done',1))

    def visitAddBreakpointCommand(self,cmd):
        cmd.setCompleted(self.findstr('^done',1))

    def visitInfoBreakpointCommand(self,cmd):
        cmd.setCompleted(self.findstr('^done',1))

    def visitDeleteBreakpointCommand(self, cmd):
        cmd.setCompleted(self.findstr('^done',1))
        
    def findstr(self,string, number):
        found = 0
        for line in self.output:
            if line.find(string) != -1:
                found += 1
                if found == number:
                    return True
        
        return False
                
    def visitListSourceFilesCmd(self,cmd):
        cmd.setCompleted(self.findstr('^done',2))
