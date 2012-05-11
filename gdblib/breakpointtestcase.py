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
import unittest

from gdblib.breakpoint import Breakpoint

class BreakpointTestCase(unittest.TestCase):
    def testStr(self):
        number = 10;
        brktype = 'type'
        address = '0x00'
        function = 'main'
        line = 199
        source = 'main.c'
        brk = Breakpoint(number,brktype,address, function, line, source)
        self.assertEquals(str(number), brk.__str__())

