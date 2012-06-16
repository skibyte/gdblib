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
from threading import Thread
import time

class FileWatcher(Thread):
    def __init__(self, fileToWatch):
        Thread.__init__(self)
        self.fileToWatch = fileToWatch
        self.keepReading = True
        self.listeners = []

    def addContentListener(self, listener):
        self.listeners.append(listener)

    def run(self):
        pass
        opened = False
        f = None

        while self.keepReading == True:
            try :
                if opened == False:
                    f = open(self.fileToWatch,'r')
                    opened = True

                if opened == True:
                    line = f.readline();
                    if line != '':
                        self.notifyListeners(line)
            except IOError as e:
                pass

            time.sleep(0.5)    
        try :
            if f != None:
                f.close()
        except IOError as e:
            pass


    def notifyListeners(self, line):
        for listener in self.listeners:
            listener.newContent(line)

    def stopWatching(self):
        self.keepReading = False
