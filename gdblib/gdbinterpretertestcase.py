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
import unittest;
from gdblib.gdbinterpreter import GDBInterpreter;

class GDBInterpreterTestCase(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)
        self.interpreter = GDBInterpreter()

    def _testBreak(self, breakpoint, number, breakpoint_type, address, 
            function, line, source_file):
        self.assertEquals(breakpoint.getNumber(), number)
        self.assertEquals(breakpoint.getType(), breakpoint_type)
        self.assertEquals(breakpoint.getAddress(), address)
        self.assertEquals(breakpoint.getFunction(), function)
        self.assertEquals(breakpoint.getLineNumber(), line)
        self.assertEquals(breakpoint.getSourceFile(), source_file)

    def testParse_AddBreakpoint(self):
        #"break main"
        handle = open('gdblib/test_files/add-breakpoint.dat','r')
        content = handle.readlines()
        handle.close()
        breakpoint = self.interpreter.parseAddBreakpointCommand(content)

        self._testBreak(breakpoint, 1,'', '0x498ea1', '', 169, 'src/main.c') 

    def testParse_Info_Functions(self):
        #"info functions"
        self.assertEquals(6,6)

    def testParse_Info_Break(self):
        #"info breakpoints"
        handle = open("gdblib/test_files/info_break.dat","r")
        filecontent = handle.readlines()
        handle.close()        
        breaks = self.interpreter.parseInfoBreak(filecontent)
        
        self.assertEqual(2, len(breaks))
        self._testBreak(breaks[0], 1, "breakpoint", "0x98ea1", "main", 169, "src/main.c")
        self._testBreak(breaks[1], 2, "breakpoint", "0x98e77", "main", 192, "src/main.c")

    #def testParse_Until(self):
        #"until"

    #def testParse_Info_Watchpoints(self):
        #"info watchpoints"
       
    def testParse_ListSourceFiles(self):
        handle = open("gdblib/test_files/list_source_files.dat", "r")
        filecontent = handle.readlines()
        handle.close()
        files = self.interpreter.parseListSourceFiles(filecontent)

        self.assertEquals(2, len(files))
        self.assertEquals('main.c',files[0]['file'])
        self.assertEquals('/home/lobo/programming/projects/python/gdb_frontend/test/org/qdebug/gdb/testapplication/main.c',files[0]['fullname'])

        self.assertEquals('module1/functions.c',files[1]['file'])
        self.assertEquals('/home/lobo/programming/projects/python/gdb_frontend/test/org/qdebug/gdb/testapplication/module1/functions.c',files[1]['fullname'])

    #def testParse_Info_Local(self):
        #"info local"
    
    def testParse_Step_Next(self):
        handle = open("gdblib/test_files/next.dat", "r")
        content = handle.readlines()
        handle.close()

        location = self.interpreter.parseStepCommand(content)

        self.assertEquals('print_point', location['func'])
        self.assertEquals('module1/functions.c', location['file'])
        self.assertEquals('/home/lobo/programming/projects/python/gdb_frontend/test/org/qdebug/gdb/testapplication/module1/functions.c', location['fullname'])
        self.assertEquals(13, location['line'])
        
    #def testParse_Backtrace(self):
        #"backtrace"


    #def testParse_Clear(self):
        #"clear"


    #def testContinue(self):
        #"continue"

    #def testWhatIs(self):
        #"whatis x"

    #def testSetVar(self):
        #"setvar " 

    #def testJump(self):
        #"jump"

    #def testReturn(self):
        #"return 2"

    #def testPrint(self):
        #"print x"
if __name__ == '__main__':
    unittest.main()
