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
import os

from gdblib.gdb import GDB
from gdblib.exceptions import NotConnectedError

class GDBTestCase(unittest.TestCase):
    def setUp(self):
        self.gdb = GDB()
        self.connectedGdb = GDB()
        self.connectedGdb.connectApp('gdblib/testapplication/app','',None)

    def tearDown(self):
        self.connectedGdb.disconnect()

    def testConneApp(self):
        self.assertTrue(self.connectedGdb.state.isConnected())

    def testConnectApp_IncorrectPath(self):
        self.assertRaises(IOError,self.gdb.connectApp, 'incorrectpath','',None);

    def testRun_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.run)

    def testChangeDirectory_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.changeDirectory, '')

    def testGetSourceCodeFiles_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.getSourceCodeFiles)

    def testAddBreakpoint_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.addBreakpoint,'','')

    def testInfoBreakpoints_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.infoBreakpoints)

    def testDeleteBreakpoint_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.deleteBreakpoint,0)

    def testAddWatchpoint_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.addWatchpoint)

    def testDeleteWatchpoint_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.deleteWatchpoint)

    def testInfoThreads_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.infoThreads)

    def testAddDirectory_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.addDirectory,'')

    def testStep_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.step)

    def testBacktrace_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.backtrace)

    def testFinish_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.finish)

    def testUntil_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.until)

    def testClear_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.clear)

    def testContinue_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.continueExecution)

    def testWhatIs_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.whatIs, 'x')

    def testSetVar_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.setVar, 0, 0)

    def testJump_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.jump)

    def testCall_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.call)

    def testReturn_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.returnExecution)

    def testGetSourceCodeFiles(self):
        path =  os.getcwd() + os.sep + 'gdblib/testapplication/'
        #path = 'test/org/qdebug/gdb/testapplication/'
        file1 = 'main.c'
        file2 = 'module1/functions.c'

        fullname1 = path + file1
        fullname2 = path + file2
        files = self.connectedGdb.getSourceCodeFiles()
        self.assertEquals(2, len(files))
        dict1 = files[0]
        dict2 = files[1]
        self.assertEquals(file1, dict1['file'])
        self.assertEquals(fullname1, dict1['fullname'])
        self.assertEquals(file2, dict2['file'])
        self.assertEquals(fullname2, dict2['fullname'])

    #def testRun(self):
        #self.gdb.run()
        #pri

    #def testStep(self):    
        #""
    
    #def testNext(self):
        #""

    def testAddBreakpoint(self):
        self.assertEquals(0, self.connectedGdb.getState().getNumberOfBreakpoints())
        path =  os.getcwd() + os.sep + 'gdblib/testapplication/main.c'
        self.connectedGdb.addBreakpoint(path,6)
        self.assertEquals(1, self.connectedGdb.getState().getNumberOfBreakpoints())
        breakpoint = self.connectedGdb.getState().getBreakpoint(0)
        self.assertEquals(1, breakpoint.getNumber())
        self.assertEquals('breakpoint', breakpoint.getType())
        self.assertEquals('main', breakpoint.getFunction())
        self.assertEquals('main.c', breakpoint.getSourceFile())
        self.assertEquals(6, breakpoint.getLineNumber())

    
    def testDeleteBreakpoint(self):
        path =  os.getcwd() + os.sep + 'gdblib/testapplication/main.c'
        self.connectedGdb.addBreakpoint(path,6)
        self.assertEquals(1, self.connectedGdb.getState().getNumberOfBreakpoints())
        brk = self.connectedGdb.getState().getBreakpoint(0)
        self.connectedGdb.deleteBreakpoint(brk.getNumber())
        self.assertEquals(0, self.connectedGdb.getState().getNumberOfBreakpoints())
    
    #def testAddWatchPoint(self):
        #pass
    
    def testInfoBreakpoints(self):
        self.assertEquals(0, self.connectedGdb.getState().getNumberOfBreakpoints())
        path =  os.getcwd() + os.sep + 'gdblib/testapplication/main.c'
        self.connectedGdb.addBreakpoint(path,6)
        self.assertEquals(1, self.connectedGdb.getState().getNumberOfBreakpoints())
        self.connectedGdb.infoBreakpoints()
        breakpoint = self.connectedGdb.getState().getBreakpoint(0)
        self.assertEquals(1, breakpoint.getNumber())
        self.assertEquals('breakpoint', breakpoint.getType())
        self.assertEquals('main', breakpoint.getFunction())
        self.assertEquals('main.c', breakpoint.getSourceFile())
        self.assertEquals(6, breakpoint.getLineNumber())

    #def testDeleteWatchpoint(self):
        #path =  os.getcwd() + os.sep + 'test/org/qdebug/gdb/testapplication/main.c'
        #self.gdb.addWatchpoint(path,6)
        #self.assertEquals(1, self.gdb.getState().getNumberOfBreakpoints())
        #brk = self.gdb.getState().getBreakpoint(0)
        #self.gdb.deleteBreakpoint(brk.getNumber())
        #self.assertEquals(0, self.gdb.getState().getNumberOfBreakpoints())

    #def testAddReadWatchpoint(self):
        #self.fail('Not implemnted yet')

    #def testDeleteReadWatchpoint(self):
        #self.fail('Not implemnted yet')

    #def testDeleteAll(self):
        #self.gdb.addBreakpoint();
        #self.gdb.addBreakpoint();
        #self.gdb.addBreakpoint();

        #self.assertEquals(3, self.gdb.getState().getNumberOfBreakpoints())
        #self.gdb.deleteAll();
        #self.assertEquals(0, self.gdb.getState().getNumberOfBreakpoints())

    #def testInfoWatchpoints(self):
        #self.assertEquals(0, self.gdb.getState().getNumberOfWatchpoints())
        #path =  os.getcwd() + os.sep + 'test/org/qdebug/gdb/testapplication/main.c'
        #self.gdb.addWatchpoint(path,6)
        #self.assertEquals(1, self.gdb.getState().getNumberOfWatchpoints())
        #self.gdb.infoWatchpoints()
        #watchpoint = self.gdb.getState().getWatchpoint(0)
        #self.assertEquals(1, watchpoint.getNumber())
        #self.assertEquals('breakpoint', watchpoint.getType())
        #self.assertEquals('main', watchpoint.getFunction())
        #self.assertEquals('main.c', watchpoint.getSourceFile())
        #self.assertEquals(6, watchpoint.getLineNumber())

    #def testEnable_DisableBreakpoint(self):
        #self.gdb.addBreakpoint();
        #brk = self.gdb.getState().getBreakpoint(0)
        #self.assertEquals(True, brk.isEnabled())
        #self.gdb.disableBreakpoint(brk.getNumber())
        #brk = self.gdb.getState().getBreakpoint(0)
        #self.assertEquals(False, brk.isEnabled())
        #self.gdb.enableBreakpoint(brk.getNumber())
        #brk = self.gdb.getState().getBreakpoint(0)
        #self.assertEquals(True, brk.isEnabled())

    #def testFinish(self):
        #self.fail('Not implemnted yet')
    
    #def testUntil(self):
        #self.fail('Not implemnted yet')

    #def testBacktrace(self):
        #self.fail('Not implemnted yet')
    
    #def testContinue(self):
        #self.fail('Not implemnted yet')
    
    #def testPrint(self):
        #self.fail('Not implemnted yet')
    
    #def testPrintX(self):
        #self.fail('Not implemnted yet')

    #def testWhatIs(self):
        #self.fail('Not implemnted yet')

    #def testJump(self):
        #self.fail('Not implemnted yet')
    
    #def testCall(self):
        #self.fail('Not implemnted yet')
    
    #def testReturn(self):
        #self.fail('Not implemnted yet')

    #def testInfoThreads(self):
        #self.fail('Not implemnted yet')
