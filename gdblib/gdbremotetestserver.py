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
from threading import Thread;
import signal
import subprocess;
import time
class GDBRemoteTestServer(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.started = False

    def run(self):
        arguments = ['gdbserver', ':1234', 'gdblib/testapplication/app']
        self.process = subprocess.Popen(arguments,
                shell=False,stdin=subprocess.PIPE,
                stdout = subprocess.PIPE)
        self.started = True

    def stop(self):
        if self.started == True:
            self.process.send_signal(signal.SIGKILL)
            time.sleep(1)

