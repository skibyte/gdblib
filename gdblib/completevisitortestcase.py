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

from gdblib.completevisitor import *
from gdblib.cmd import *

class CompleteVisitorTestCase(unittest.TestCase):
    def setUp(self):
        self.visitor = CompleteVisitor()

    def testVisitDefaultCommand_Quit(self):
        quit = QuitCommand()
        self.visitor.setoutput('&"quit\\n"')
        self.visitor.visitDefaultCommand(quit)
        self.assertEquals(True, quit.isComplete(), 'Quit command not completed')
