# 
# GdbLib - A Gdb python library.
# Copyright (C) 2016  Fernando Castillo
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

import os
from gdblib.gdb import GDB

def main():
    test_application = 'gdblib' + os.sep + 'testapplication' + os.sep + 'app'
    test_application_arguments = ''
    gdb = GDB()
    listener = Listener()
    gdb.connectApp(test_application)
    gdb.addBreakpoint('main.c', 20)
    breakpoints = gdb.getBreakpoints()
    gdb.addNewFileLocationListener(listener)
    gdb.run(test_application_arguments)
    gdb.step()
    gdb.next()
    gdb.deleteBreakpoint(1)
    gdb.disconnect()

class Listener():
    def newFileLocation(self, newFileStr, newLine):
        print newFileStr + ':' + str(newLine)

if __name__== '__main__':
    main()
