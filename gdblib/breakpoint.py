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
class Breakpoint():
    def __init__(self, number, breakpointtype, 
            address, function, sourcefile, linenumber):
        self.number = number
        self.breakpointtype = breakpointtype
        self.address = address
        self.function = function
        self.linenumber = linenumber
        self.sourcefile = sourcefile

    def getNumber(self):
        return self.number

    def getType(self):
        return self.breakpointtype

    def getAddress(self):
        return self.address

    def getFunction(self):
        return self.function

    def getLineNumber(self):
        return self.linenumber

    def getSourceFile(self):
        return self.sourcefile

    def setSourceFile(self, sourcefile):
        self.sourcefile = sourcefile

    def __str__(self):
        return str(self.number)

