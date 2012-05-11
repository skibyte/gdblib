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
class GDBState():
    def __init__(self):
        self.connected = False
        self.breakpoints = []
        self.listeners = []
        self.watchpoints = []

    def addListener(self,listener):
        self.listeners.append(listener)

    def getNumberOfBreakpoints(self):

        return len(self.breakpoints)

    def getBreakpoint(self, index):
        return self.breakpoints[index]

    def getBreakpoints(self):
        return self.breakpoints;

    def setBreakpoints(self,breakpoints):
        self.breakpoints = breakpoints

    def addBreakpoint(self, breakpoint):
        self.breakpoints.append(breakpoint)
        for listener in self.listeners:
            listener.updateBreakpoints()
     
    def deleteBreakpoint(self, breakpoint):
        self.breakpoints.remove(breakpoint)

    def addWatchpoint(self,watchpoint):
        self.watchpoints.append(watchpoint)

    def setCurrentLocation(self,currentfile,currentline):
        self.currentfile = currentfile
        self.currentline = currentline
   
    def isConnected(self):
        return self.connected
   
    def setConnected(self, connected):
        self.connected = connected
