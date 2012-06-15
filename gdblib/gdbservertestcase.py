#
# GdbLib - A Gdb python library.
# Copyright (C) 2012 Fernando Castillo
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
import subprocess;

from gdblib.gdbserver import GDBServer

class GDBServerTestCase(unittest.TestCase):
    def setUp(self):
        self.apppath = 'gdblib/testapplication/app'
        self.arguments = ['gdb','-i','mi','-q',self.apppath, '']
        self.process = subprocess.Popen(self.arguments,
                shell=False,stdin=subprocess.PIPE,
                stdout = subprocess.PIPE)
        self.server = GDBServer(self.process)

    def tearDown(self):
        self.server.stopserver()

    def testStart(self):
        self.server.start()
