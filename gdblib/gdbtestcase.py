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
import time
import platform

from gdblib.gdb import GDB
from gdblib.gdbremotetestserver import GDBRemoteTestServer
from gdblib.exceptions import *
from subprocess import call

class GDBTestCase(unittest.TestCase):
    def fileExists(self,filename):
        try :
            handle = open(filename, "r")
            handle.close()
            return True
        except IOError as e:
            return False

    def setUp(self):
        self.gdb = GDB()
        self.connectedGdb = GDB()
        self.gdbRemote = GDB()
        self.remoteServer = GDBRemoteTestServer()
        self.ttyfile = os.getcwd() + '/gdblib/testapplication/tty.console'
        if(self.fileExists(self.ttyfile) == True):
            os.remove(self.ttyfile)
        try:
            if platform.system() == 'Windows':
                self.connectedGdb.connectApp('gdblib' + os.sep + 'testapplication' + os.sep + 'app.exe')
            else:
                self.connectedGdb.connectApp('gdblib' + os.sep + 'testapplication' + os.sep + 'app')
        except AlreadyConnectedError:
            self.tearDown()

        self.listener = Listener()

    def tearDown(self):
        self.connectedGdb.disconnect()
        if(self.fileExists(self.ttyfile) == True):
            os.remove(self.ttyfile)

        if not platform.system() == 'Windows':
            if self.gdbRemote.isConnected() == True:
                self.gdbRemote.disconnect()

    def testConneApp(self):
        self.assertTrue(self.connectedGdb.state.isConnected())

    def testConneApp_Twice(self):
        self.assertRaises(AlreadyConnectedError, self.connectedGdb.connectApp, '')

    def testConnectApp_IncorrectPath(self):
        self.assertRaises(IOError,self.gdb.connectApp, 'incorrectpath');

    def testRun_NotConnectedException(self):
        self.assertRaises(NotConnectedError, self.gdb.run, '')

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
        self.assertRaises(NotConnectedError, self.gdb.clear, '', 0)

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
        path =  os.getcwd() + os.sep + 'gdblib' + os.sep + 'testapplication' + os.sep
        file1 = 'main.c'
        file2 = 'module1' + os.sep + 'functions.c'


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
        self.connectedGdb.run('')

    def testRun_Twice(self):
        self.connectedGdb.run('')
        self.connectedGdb.run('')

    def testStep(self):
        self.connectedGdb.addNewFileLocationListener(self.listener)
        path =  os.getcwd() + os.sep + 'gdblib' + os.sep + 'testapplication' + os.sep + 'main.c'
        self.connectedGdb.addBreakpoint(path,26)
        self.connectedGdb.run('')
        self.connectedGdb.step()
        self.assertEquals(2, self.listener.newFileLocationCounter())
        path =  os.getcwd() + os.sep + 'gdblib' + os.sep + 'testapplication' + os.sep + 'module1' + os.sep + 'functions.c'
        self.assertEquals(path, self.listener.newFile())
        self.assertEquals(23, self.listener.newLine())

    def testNext(self):
        self.connectedGdb.addNewFileLocationListener(self.listener)
        path =  os.getcwd() + os.sep + 'gdblib' + os.sep + 'testapplication' + os.sep + 'main.c'
        self.connectedGdb.addBreakpoint(path,26)
        self.connectedGdb.run('')
        self.connectedGdb.next()
        self.assertEquals(2, self.listener.newFileLocationCounter())
        self.assertEquals(path, self.listener.newFile())
        self.assertEquals(27, self.listener.newLine())

    def testPrint(self):
        self.connectedGdb.addNewFileLocationListener(self.listener)
        path =  os.getcwd() + os.sep + 'gdblib' + os.sep + 'testapplication' + os.sep + 'main.c'
        self.connectedGdb.addBreakpoint(path,26)
        self.connectedGdb.run('')
        self.assertEquals('$1 = 6', self.connectedGdb.p('mypoint.x'))

    def testPrint_Incorrect(self):
        self.connectedGdb.addNewFileLocationListener(self.listener)
        path =  os.getcwd() + os.sep + 'gdblib' + os.sep + 'testapplication'  + os.sep + 'main.c'
        self.connectedGdb.addBreakpoint(path,26)
        self.connectedGdb.run('')
        self.assertEquals('No symbol \\\"e\\\" in current context.\\n', \
                self.connectedGdb.p('e'))

    def testAddNewFileLocationListener(self):
        self.connectedGdb.addNewFileLocationListener(self.listener)
        path =  os.getcwd() + os.sep + 'gdblib' + os.sep + 'testapplication' + os.sep + 'main.c'
        self.connectedGdb.addBreakpoint(path,22)
        self.connectedGdb.run('')
        self.assertEquals(path, self.listener.newFile())
        self.assertEquals(22, self.listener.newLine())

    def testRemoveNewFileLocationListener(self):
        self.connectedGdb.addNewFileLocationListener(self.listener)
        self.assertEquals(1, len(self.connectedGdb.newFileLocationListeners()))
        self.connectedGdb.removeNewFileLocationListener(self.listener)
        self.assertEquals(0, len(self.connectedGdb.newFileLocationListeners()))

    def testsetTty(self):
        if not platform.system() == 'Windows':
            handle = open(self.ttyfile, "w")
            handle.close()
            self.connectedGdb.setTty(self.ttyfile)
            self.connectedGdb.run('')
            time.sleep(5)
            handle = open(self.ttyfile, "r")
            expected = 'X:6\tY:7\nX:8\tY:9\n'
            self.assertTrue(expected in handle.read())
            handle.close()
        else:
            print "\n" + self.testsetTty.__name__ + " is not implemented yet"

    def testAddBreakpoint(self):
        self.assertEquals(0, len(self.connectedGdb.getBreakpoints()))
        path1 =  os.getcwd() + os.sep + 'gdblib' + os.sep + 'testapplication' + os.sep + 'main.c'

        self.connectedGdb.addBreakpoint(path1,22)
        self.assertEquals(1, len(self.connectedGdb.getBreakpoints()))

        path2 =  os.getcwd() + os.sep + 'gdblib' + os.sep + 'testapplication' + os.sep + 'module1' + os.sep + 'functions.c'
        self.connectedGdb.addBreakpoint(path2,22)

        self.assertEquals(2, len(self.connectedGdb.getBreakpoints()))

        breakpoints = self.connectedGdb.getBreakpoints()
        self.assertEquals(1, breakpoints[0].getNumber())
        self.assertEquals('breakpoint', breakpoints[0].getType())
        self.assertEquals('main', breakpoints[0].getFunction())
        self.assertEquals(path1, breakpoints[0].getSourceFile(), 'Path is incorrect')
        self.assertEquals(22, breakpoints[0].getLineNumber())

        self.assertEquals(2, breakpoints[1].getNumber())
        self.assertEquals('breakpoint', breakpoints[1].getType())
        self.assertEquals('modify_point', breakpoints[1].getFunction())
        self.assertEquals(path2, breakpoints[1].getSourceFile())
        self.assertEquals(22, breakpoints[1].getLineNumber())

    def testAddBreakpoint_NoSourceFileError(self):
        self.assertRaises(NoSourceFileError, self.connectedGdb.addBreakpoint, 'incorrectfile', 6)

    def testAddBreakpoint_NoLineError(self):
        path =  os.getcwd() + os.sep + 'gdblib' + os.sep + 'testapplication' + os.sep + 'main.c'
        self.assertRaises(NoLineError, self.connectedGdb.addBreakpoint, path, 99)

    def testDeleteBreakpoint(self):
        path =  os.getcwd() + os.sep + 'gdblib' + os.sep + 'testapplication' + os.sep + 'main.c'
        self.connectedGdb.addBreakpoint(path,6)
        self.assertEquals(1, len(self.connectedGdb.getBreakpoints()))
        breakpoints = self.connectedGdb.getBreakpoints()
        self.connectedGdb.deleteBreakpoint(breakpoints[0].getNumber())
        self.assertEquals(0, len(self.connectedGdb.getBreakpoints()))
   
    def testClear(self):
        path =  os.getcwd() + os.sep + 'gdblib' + os.sep + 'testapplication' + os.sep + 'main.c'
        self.connectedGdb.addBreakpoint(path,6)
        self.assertEquals(1, len(self.connectedGdb.getBreakpoints()))
        self.connectedGdb.clear(path, 6)
        self.assertEquals(0, len(self.connectedGdb.getBreakpoints()))
   
    def testDeleteAllBreakpoints(self):
        path =  os.getcwd() + os.sep + 'gdblib' + os.sep + 'testapplication' + os.sep + 'main.c'
        self.connectedGdb.addBreakpoint(path,6)
        self.connectedGdb.addBreakpoint(path,7)
        self.assertEquals(2, len(self.connectedGdb.getBreakpoints()))
        breakpoints = self.connectedGdb.getBreakpoints()
        self.connectedGdb.deleteAllBreakpoints()
        self.assertEquals(0, len(self.connectedGdb.getBreakpoints()))
    
    def testContinueExecution(self):
        self.assertEquals(0, len(self.connectedGdb.getBreakpoints()))
        path =  os.getcwd() + os.sep + 'gdblib' + os.sep + 'testapplication' + os.sep + 'main.c'
        self.connectedGdb.addBreakpoint(path,22)
        self.connectedGdb.run('')
        self.connectedGdb.continueExecution()

    def testRemoteTarget(self):
        if not platform.system() == 'Windows':
            self.remoteServer.start()
            time.sleep(1)
            self.gdbRemote.connectRemote(':1234')
            self.assertTrue(self.gdbRemote.isConnected())
            self.gdbRemote.continueExecution()
            self.remoteServer.stop()
        else:
            print "\n" + self.testRemoteTarget.__name__ + " is not implemented yet"

    def testRemoteTarget_Timeout(self):
        if not platform.system() == 'Windows':
            time.sleep(1)
            self.assertRaises(TimeoutError, self.gdbRemote.connectRemote, ':1234')
        else:
            print "\n" + self.testRemoteTarget_Timeout.__name__ + " is not implemented yet"


    def testSymbolFile(self):
        if not platform.system() == 'Windows':
            self.remoteServer.start()
            time.sleep(1)
            self.gdbRemote.connectRemote(':1234')
            symbol = self.gdbRemote.symbolFile('gdblib/testapplication/app')
            path =  'gdblib/testapplication/app'
            self.assertEquals(path, symbol)
            self.remoteServer.stop()
        else:
            print "\n" + self.testSymbolFile.__name__ + " is not implemented yet"

    def testHang(self):
        hangGdb = GDB()
        if platform.system() == 'Windows':
            hangGdb.connectApp('gdblib' + os.sep + 'testapplication' + os.sep + 'app.exe')
        else:
            hangGdb.connectApp('gdblib' + os.sep + 'testapplication' + os.sep + 'app')

    def testLoad(self):
        if not platform.system() == 'Windows':
            self.remoteServer.start()
            time.sleep(1)
            self.gdbRemote.connectRemote(':1234')
            symbol = self.gdbRemote.load('gdblib/testapplication/app')
            self.remoteServer.stop()
        else:
            print "\n" + self.testLoad.__name__ + " is not implemented yet"


class Listener():
    output = ''
    eventCounter = 0
    exitCounter = 0

    def newFileLocation(self, newFileStr, newLineStr):
        self.newFileStr = newFileStr
        self.newLineStr = newLineStr
        self.eventCounter += 1

    def newContent(self, output):
        self.output += output

    def newFile(self):
        return self.newFileStr

    def newLine(self):
        return self.newLineStr

    def newFileLocationCounter(self):
        return self.eventCounter

    def standardOutputReceived(self):
        return self.output

    def exitCount(self):
        return self.exitCounter
