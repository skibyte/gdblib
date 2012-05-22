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
from gdblib.exceptions import NoLineError
from gdblib.exceptions import NoSourceFileError

class GDBTestCase(unittest.TestCase):
    def setUp(self):
        self.gdb = GDB()
        self.connectedGdb = GDB()
        self.connectedGdb.connectApp('gdblib/testapplication/app','')
        self.listener = Listener()

    def tearDown(self):
        self.connectedGdb.disconnect()

    def testConneApp(self):
        self.assertTrue(self.connectedGdb.state.isConnected())

    def testConnectApp_IncorrectPath(self):
        self.assertRaises(IOError,self.gdb.connectApp, 'incorrectpath','');

    def testRun_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.run)

    def testChangeDirectory_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.changeDirectory, '')

    def testGetSourceCodeFiles_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.getSourceCodeFiles)

    def testAddBreakpoint_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.addBreakpoint,'','')

    def testGetBreakpoints_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.getBreakpoints)

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

    def testRun(self):
        self.connectedGdb.run()

    #def testStep(self):    
        #""
    
    #def testNext(self):
        #""

    def testAddNewFileLocationListener(self):
        self.connectedGdb.addNewFileLocationListener(self.listener)
        path =  os.getcwd() + os.sep + 'gdblib/testapplication/main.c'
        self.connectedGdb.addBreakpoint(path,22)
        self.connectedGdb.run()
        self.assertEquals(path, self.listener.newFile())
        self.assertEquals(22, self.listener.newLine())

    def testAddStandardOutputListener(self):
        pass
        #self.connectedGdb.addStandardOutputListener(self.listener)
        #self.connectedGdb.run()
        #self.assertEquals('X:6\tY:7\nX:8\tY:9', self.listener.standardOutputReceived())

    def testAddErrorListener(self):
        pass

    def testStandardInput(self):
        pass

    def testAddBreakpoint(self):
        self.assertEquals(0, len(self.connectedGdb.getBreakpoints()))
        path =  os.getcwd() + os.sep + 'gdblib/testapplication/main.c'
        self.connectedGdb.addBreakpoint(path,22)
        self.assertEquals(1, len(self.connectedGdb.getBreakpoints()))
        breakpoints = self.connectedGdb.getBreakpoints()
        self.assertEquals(1, breakpoints[0].getNumber())
        self.assertEquals('breakpoint', breakpoints[0].getType())
        self.assertEquals('main', breakpoints[0].getFunction())
        self.assertEquals('main.c', breakpoints[0].getSourceFile())
        self.assertEquals(22, breakpoints[0].getLineNumber())

    def testAddBreakpoint_NoSourceFileError(self):
        self.assertRaises(NoSourceFileError, self.connectedGdb.addBreakpoint, 'incorrectfile', 6)

    def testAddBreakpoint_NoLineError(self):
        path =  os.getcwd() + os.sep + 'gdblib/testapplication/main.c'
        self.assertRaises(NoLineError, self.connectedGdb.addBreakpoint, path, 99)

    def testDeleteBreakpoint(self):
        path =  os.getcwd() + os.sep + 'gdblib/testapplication/main.c'
        self.connectedGdb.addBreakpoint(path,6)
        self.assertEquals(1, len(self.connectedGdb.getBreakpoints()))
        breakpoints = self.connectedGdb.getBreakpoints()
        self.connectedGdb.deleteBreakpoint(breakpoints[0].getNumber())
        self.assertEquals(0, len(self.connectedGdb.getBreakpoints()))
    
    #def testAddWatchPoint(self):
        #pass
    
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

class Listener():
    def newFileLocation(self, newFileStr, newLineStr):
        self.newFileStr = newFileStr
        self.newLineStr = newLineStr

    def standardOutput(self, output):
        self.output = output

    def newFile(self):
        return self.newFileStr

    def newLine(self):
        return self.newLineStr
    
    def standardOutputReceived(self):
        return self.output
