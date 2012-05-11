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
from gdblib.cmd import *
from gdblib.utilityvisitor import UtilityVisitor

class DefaultCommandTestCase(unittest.TestCase):
    def testAccept(self):
        self.fail('Not implemented yet')

    def testSetCompleted(self):
        self.fail('Not implemented yet')

    def testIsComplete(self):
        self.fail('Not implemented yet')

class AddDirectoryCommandTestCase(unittest.TestCase):
    cmd = None
    visitor = None

    def setUp(self):
        self.cmd = AddDirectoryCommand('/mydirectory/dir')
        self.visitor = UtilityVisitor()

    def testGetValue(self):
        self.assertEquals('-environment-directory /mydirectory/dir\n', self.cmd.getValue())

    def testAccept(self):
        self.cmd.accept(self.visitor)
        self.assertEquals(True, self.visitor.isAddDirectoryCommandVisited())

class ChangeDirectoryCommandTestCase(unittest.TestCase):
    cmd = None
    visitor = None

    def setUp(self):
        self.cmd = ChangeDirectoryCommand('/mydirectory/dir')
        self.visitor = UtilityVisitor()

    def testGetValue(self):
        self.assertEquals('-environment-cd /mydirectory/dir\n', self.cmd.getValue())

    def testAccept(self):
        self.cmd.accept(self.visitor)
        self.assertEquals(True, self.visitor.isChangeDirectoryCommandVisited())

class ListSourceFilesCommandTestCase(unittest.TestCase):
    cmd = None
    visitor = None

    def setUp(self):
        self.cmd = ListSourceFilesCommand()
        self.visitor = UtilityVisitor()

    def testGetValue(self):
        self.assertEquals('interpreter-exec \"-file-list-exec-source-files\"\n', self.cmd.getValue())

    def testAccept(self):
        self.cmd.accept(self.visitor)
        self.assertEquals(True, self.visitor.isListSourceFilesCommandVisited())

class AdvanceCommandTestCase(unittest.TestCase):
    cmd = None
    visitor = None

    def setUp(self):
        self.cmd = AdvanceCommand('function')
        self.visitor = UtilityVisitor()

    def testGetValue(self):
        self.assertEquals('advance function\n', self.cmd.getValue())

    def testAccept(self):
        self.cmd.accept(self.visitor)
        self.assertEquals(True, self.visitor.isAdvanceCommandVisited())

class NextCommandTestCase(unittest.TestCase):
    cmd = None
    visitor = None

    def setUp(self):
        self.cmd = NextCommand()
        self.visitor = UtilityVisitor()

    def testGetValue(self):
        self.assertEquals('next\n', self.cmd.getValue())

    def testAccept(self):
        self.cmd.accept(self.visitor)
        self.assertEquals(True, self.visitor.isNextCommandVisited())

class StepCommandTestCase(unittest.TestCase):
    cmd = None
    visitor = None

    def setUp(self):
        self.cmd = StepCommand()
        self.visitor = UtilityVisitor()

    def testGetValue(self):
        self.assertEquals('step\n', self.cmd.getValue())

    def testAccept(self):
        self.cmd.accept(self.visitor)
        self.assertEquals(True, self.visitor.isStepCommandVisited())

class RunCommandTestCase(unittest.TestCase):
    cmd = None
    visitor = None

    def setUp(self):
        self.cmd = RunCommand('arg')
        self.visitor = UtilityVisitor()

    def testGetValue(self):
        self.assertEquals('run arg > output.console\n', self.cmd.getValue())

    def testAccept(self):
        self.cmd.accept(self.visitor)
        self.assertEquals(True, self.visitor.isRunCommandVisited())

class BacktraceCommandTestCase(unittest.TestCase):
    cmd = None
    visitor = None

    def setUp(self):
        self.cmd = BacktraceCommand()
        self.visitor = UtilityVisitor()

    def testGetValue(self):
        self.assertEquals('backtrace\n', self.cmd.getValue())

    def testAccept(self):
        self.cmd.accept(self.visitor)
        self.assertEquals(True, self.visitor.isBacktraceCommandVisited())

class PrintCommandTestCase(unittest.TestCase):
    cmd = None
    visitor = None

    def setUp(self):
        self.cmd = PrintCommand('var')
        self.visitor = UtilityVisitor()

    def testGetValue(self):
        self.assertEquals('print var\n', self.cmd.getValue())

    def testAccept(self):
        self.cmd.accept(self.visitor)
        self.assertEquals(True, self.visitor.isPrintCommandVisited())

class PrintXCommandTestCase(unittest.TestCase):
    cmd = None
    visitor = None

    def setUp(self):
        self.cmd. PrintXCommand('/mydirectory/dir')
        self.visitor = UtilityVisitor()

    def testGetValue(self):
        self.fail('Not implemented yet')

    def testAccept(self):
        self.cmd.accept(self.visitor)
        self.assertEquals(True, self.visitor.isPrintXCommandVisited())

class SetVarCommandTestCase(unittest.TestCase):
    cmd = None
    visitor = None

    def setUp(self):
        self.cmd. SetVarCommand('/mydirectory/dir')
        self.visitor = UtilityVisitor()

    def testGetValue(self):
        self.fail('Not implemented yet')

    def testAccept(self):
        self.cmd.accept(self.visitor)
        self.assertEquals(True, self.visitor.isSetVarCommandVisited())

class ReturnCommandTestCase(unittest.TestCase):
    cmd = None
    visitor = None

    def setUp(self):
        self.cmd. ReturnCommand('/mydirectory/dir')
        self.visitor = UtilityVisitor()

    def testGetValue(self):
        self.fail('Not implemented yet')

    def testAccept(self):
        self.cmd.accept(self.visitor)
        self.assertEquals(True, self.visitor.isReturnCommandVisited())

class ContinueCommandTestCase(unittest.TestCase):
    cmd = None
    visitor = None

    def setUp(self):
        self.cmd. ContinueCommand('/mydirectory/dir')
        self.visitor = UtilityVisitor()

    def testGetValue(self):
        self.fail('Not implemented yet')

    def testAccept(self):
        self.cmd.accept(self.visitor)
        self.assertEquals(True, self.visitor.isContinueCommandVisited())

class FinishCommandTestCase(unittest.TestCase):
    cmd = None
    visitor = None

    def setUp(self):
        self.cmd. FinishCommand('/mydirectory/dir')
        self.visitor = UtilityVisitor()

    def testGetValue(self):
        self.fail('Not implemented yet')

    def testAccept(self):
        self.cmd.accept(self.visitor)
        self.assertEquals(True, self.visitor.isFinishCommandVisited())

class WhatIsCommandTestCase(unittest.TestCase):
    cmd = None
    visitor = None

    def setUp(self):
        self.cmd. WhatIsCommand('/mydirectory/dir')
        self.visitor = UtilityVisitor()

    def testGetValue(self):
        self.fail('Not implemented yet')

    def testAccept(self):
        self.cmd.accept(self.visitor)
        self.assertEquals(True, self.visitor.isWhatIsCommandVisited())

class AddBreakpointCommandTestCase(unittest.TestCase):
    cmd = None
    visitor = None

    def setUp(self):
        self.cmd. AddBreakpointCommand('/mydirectory/dir')
        self.visitor = UtilityVisitor()

    def testGetValue(self):
        self.fail('Not implemented yet')

    def testAccept(self):
        self.cmd.accept(self.visitor)
        self.assertEquals(True, self.visitor.isAddBreakpointCommandVisited())

class DeleteBreakpointCommandTestCase(unittest.TestCase):
    cmd = None
    visitor = None

    def setUp(self):
        self.cmd. DeleteBreakpoint('/mydirectory/dir')
        self.visitor = UtilityVisitor()

    def testGetValue(self):
        self.fail('Not implemented yet')

    def testAccept(self):
        self.cmd.accept(self.visitor)
        self.assertEquals(True, self.visitor.isDeleteBreakpointCommandVisited())

class AddWatchPointCommandTestCase(unittest.TestCase):
    cmd = None
    visitor = None

    def setUp(self):
        self.visitor = UtilityVisitor()
        self.cmd. AddWatchpointCommand('/mydirectory/dir')

    def testGetValue(self):
        self.fail('Not implemented yet')

    def testAccept(self):
        self.cmd.accept(self.visitor)
        self.assertEquals(True, self.visitor.isAddWatchPointCommandVisited())

class DeleteWatchpointCommandTestCase(unittest.TestCase):
    cmd = None
    visitor = None

    def setUp(self):
        self.cmd. DeleteWatchpointCommand('/mydirectory/dir')
        self.visitor = UtilityVisitor()

    def testGetValue(self):
        self.fail('Not implemented yet')

    def testAccept(self):
        self.cmd.accept(self.visitor)
        self.assertEquals(True, self.visitor.isDeleteWatchpointCommandVisited())

class InfoBreakpointCommandTestCase(unittest.TestCase):
    cmd = None
    visitor = None

    def setUp(self):
        self.cmd. InfoBreakpointCommand('/mydirectory/dir')
        self.visitor = UtilityVisitor()

    def testGetValue(self):
        self.fail('Not implemented yet')

    def testAccept(self):
        self.cmd.accept(self.visitor)
        self.assertEquals(True, self.visitor.isInfoBreakpointCommandVisited())

