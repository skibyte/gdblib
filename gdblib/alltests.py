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


import gdblib

from gdbservertestcase import GDBServerTestCase
from gdbtestcase import GDBTestCase
from gdbinterpretertestcase import GDBInterpreterTestCase
from utiltestcase import UtilTestCase
from breakpointtestcase import BreakpointTestCase
from completevisitortestcase import *
import logging

def main(log):
    loader = unittest.TestLoader()

    if log == '1':
        gdblib.log.Logger.enable(True)
        gdblib.log.Logger.level(logging.DEBUG)
        gdblib.log.Logger.logToFile('gdblib.log')

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
