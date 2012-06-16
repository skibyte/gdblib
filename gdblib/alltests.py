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
import sys


from gdblib.gdbservertestcase import GDBServerTestCase
from gdblib.gdbtestcase import GDBTestCase
from gdblib.gdbinterpretertestcase import GDBInterpreterTestCase
from gdblib.utiltestcase import UtilTestCase
from gdblib.breakpointtestcase import BreakpointTestCase
from gdblib.completevisitortestcase import *

def main():
    loader = unittest.TestLoader()

    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(GDBServerTestCase))
    suite.addTests(loader.loadTestsFromTestCase(CompleteVisitorTestCase))
    suite.addTests(loader.loadTestsFromTestCase(GDBInterpreterTestCase))
    suite.addTests(loader.loadTestsFromTestCase(GDBTestCase))
    suite.addTests(loader.loadTestsFromTestCase(UtilTestCase))
    suite.addTests(loader.loadTestsFromTestCase(BreakpointTestCase))
    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(suite)
    return len(result.errors) + len(result.failures)

if __name__ == '__main__':
    sys.exit(main())
