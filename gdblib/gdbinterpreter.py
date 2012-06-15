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
from gdblib.breakpoint import Breakpoint
from gdblib.exceptions import NoLineError
from gdblib.exceptions import NoSourceFileError
import re;

class GDBInterpreter():
    def parseInfoBreak(self, gdboutputlines):
        breakpoints = []
        for line in gdboutputlines:
            matches = re.match(r'~"(\d+)\s+(\w+)\s+\w+\s+\w+\s+(\w+)\s+in\s+(\w+)\s+at\s+(\w+/*\w+\.\w+):(\d+)\\n', line)
            if(matches):
                number = int(matches.group(1))
                breakpointType = matches.group(2)
                address = matches.group(3)
                function = matches.group(4)
                source = matches.group(5)
                line = int(matches.group(6))
                breakpoints.append(Breakpoint(number,breakpointType,address,function,source, line))
        return breakpoints;

    def parseListSourceFiles(self, gdboutputlines):
        files = []
        for line in gdboutputlines:
            sub = line.split('},')
            for inner in sub:
                matches = re.match(r'.*file=\"(.+)\",fullname=\"(.+)\".*',inner)
                if(matches):
                    filename = matches.group(1)
                    fullname = matches.group(2) 
                    dictionary = {"file":filename, "fullname":fullname};
                    #TODO: Check for other extensions
                    if (filename.endswith(".c") or filename.endswith(".cpp")):
                        files.append(dictionary)

        return files;                

    def parseAddBreakpointCommand(self, gdboutputlines):
        breakpoint = None
        for line in gdboutputlines:
            matches = re.match(r'~\"Breakpoint (\d+) at (\w+): file (.+\.\w+), line (\d+)\.\\n',line)
            if(matches):
                number = int(matches.group(1))
                address = matches.group(2)
                source = matches.group(3)
                line = int(matches.group(4))
                breakpoint = Breakpoint(number,'',address,'',source, line)
                return breakpoint

            matches = re.match('.*No\sline\s\d+\sin\sfile\s.*',line)
            if(matches):
                raise NoLineError("Breakpoint could not be added")

            matches = re.match('.*No\ssource\sfile\snamed\s.*',line)
            if(matches):
                raise NoSourceFileError("Breakpoint could not be added")

        return breakpoint                

    def parseStepCommand(self,gdboutputlines):
        dictionary = {}
        for line in gdboutputlines:
            matches = re.match(r'.*func=\"(.*)\",args.*file=\"(.*)\".*fullname=\"(.*)\".*line=\"(\d+)\".*',line)
            if(matches):
                dictionary['func'] = matches.group(1)
                dictionary['file'] = matches.group(2)
                dictionary['fullname'] = matches.group(3)
                dictionary['line'] = int(matches.group(4))
        return dictionary    

    def parsePrintCommand(self, gdboutputlines):
        for line in gdboutputlines:
            matches = re.match(r'~\"(\$\d+\s=.*)\"',line)
            if(matches):
                return matches.group(1)

    def parse(self,cmd, output):
        self.output = output
        cmd.accept(self)

    def visitListSourceFilesCmd(self,cmd):
        cmd.setSourceFiles(self.parseListSourceFiles(self.output))

    def visitAddBreakpointCommand(self,cmd):
        breakpoint = self.parseAddBreakpointCommand(self.output)
        cmd.setBreakpointAdded(breakpoint)
    
    def visitDeleteBreakpointCommand(self, cmd):
        pass

    def visitAdvanceCommand(self,cmd):
        dictionary = self.parseStepCommand(self.output)
        cmd.setLocation(dictionary)

    def visitDefaultCommand(self,cmd):        
        pass

    def visitAddDirectoryCommand(self,cmd):
        pass

    def visitChangeDirectoryCommand(self,cmd):
        pass

    def visitInfoBreakpointCommand(self,cmd):
        breakpoints = self.parseInfoBreak(self.output)
        cmd.setBreakpoints(breakpoints)

    def visitPrintCommand(self, cmd):
        cmd.setResult(self.parsePrintCommand(self.output))
