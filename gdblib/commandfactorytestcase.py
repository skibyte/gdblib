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

from gdblib.commandfactory import CommandFactory
from gdblib.cmd import *

class CommandFactoryTestCase(unittest.TestCase):
    factory = None

    def setUp(self):
        self.factory = CommandFactory()

    def testCreateAddDirectoryCommand(self):
        cmd = self.factory.createAddDirectoryCommand('directory')
        self.assertTrue(isinstance(cmd, AddDirectoryCommand()))

    #def testCreateChangeDirectoryCommand(self):
        #cmd = self.factory.createAddDirectoryCommand('directory')
        #self.assertTrue(isinstance(cmd, AddDirectoryCommand))

    #def testCreateInfoSourceCommand(self):
        #cmd = self.factory.createAddDirectoryCommand('directory')
        #self.assertTrue(isinstance(cmd, AddDirectoryCommand))

    #def testCreateNextCommand(self):
        #cmd = self.factory.createAddDirectoryCommand('directory')
        #self.assertTrue(isinstance(cmd, AddDirectoryCommand))

    #def testCreateStepCommand(self):
        #cmd = self.factory.createAddDirectoryCommand('directory')
        #self.assertTrue(isinstance(cmd, AddDirectoryCommand))

    #def testCreateAddBreakpointCommand(self, filename, line):
        #cmd = self.factory.createAddDirectoryCommand('directory')
        #self.assertTrue(isinstance(cmd, AddDirectoryCommand))

    #def testCreateDeleteBreakpointCommand(self, number):
        #cmd = self.factory.createAddDirectoryCommand('directory')
        #self.assertTrue(isinstance(cmd, AddDirectoryCommand))

    #def testCreateAddWatchPointCommand(self):
        #cmd = self.factory.createAddDirectoryCommand('directory')
        #self.assertTrue(isinstance(cmd, AddDirectoryCommand))

    #def testCreateDeleteWatchPointCommand(self):
        #cmd = self.factory.createAddDirectoryCommand('directory')
        #self.assertTrue(isinstance(cmd, AddDirectoryCommand))

    #def testCreateRunCommand(self,arguments):
        #cmd = self.factory.createAddDirectoryCommand('directory')
        #self.assertTrue(isinstance(cmd, AddDirectoryCommand))

    #def testCreateBacktraceCommand(self):
        #cmd = self.factory.createAddDirectoryCommand('directory')
        #self.assertTrue(isinstance(cmd, AddDirectoryCommand))

    #def testCreateReturnCommand(self):
        #cmd = self.factory.createAddDirectoryCommand('directory')
        #self.assertTrue(isinstance(cmd, AddDirectoryCommand))

    #def testCreateInfoBreakpointCommand(self):
        #cmd = self.factory.createInfoBreakpointCommand('directory')
        #self.assertTrue(isinstance(cmd, InfoBreakpointCommand))
