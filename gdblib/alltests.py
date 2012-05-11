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

sys.path.append('src')

from gdblib.gdbinterpretertestcase import GDBInterpreterTestCase;
from gdblib.gdbtestcase import GDBTestCase;
from gdblib.utiltestcase import UtilTestCase
from gdblib.breakpointtestcase import BreakpointTestCase;
from gdblib.cmdtestcase import *
from gdblib.commandfactorytestcase import *


def main():
    loader = unittest.TestLoader()

    suite = unittest.TestSuite()
    #suite.addTests(loader.loadTestsFromTestCase(GDBInterpreterTestCase))
    suite.addTests(loader.loadTestsFromTestCase(GDBTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(UtilTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(BreakpointTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(DefaultCommandTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(AddDirectoryCommandTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(ChangeDirectoryCommandTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(ListSourceFilesCommandTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(AdvanceCommandTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(NextCommandTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(StepCommandTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(RunCommandTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(BacktraceCommandTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(PrintCommandTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(PrintXCommandTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(SetVarCommandTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(ReturnCommandTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(ContinueCommandTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(FinishCommandTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(WhatIsCommandTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(AddBreakpointCommandTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(DeleteBreakpointCommandTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(AddWatchPointCommandTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(DeleteWatchpointCommandTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(InfoBreakpointCommandTestCase))
    #suite.addTests(loader.loadTestsFromTestCase(CommandFactoryTestCase))
    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(suite)

if __name__ == '__main__':
    sys.exit(main())
