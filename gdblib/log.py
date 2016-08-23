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

import logging
import threading

class Logger:
    enabled = False
    logLevel = logging.INFO
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    name = ''
    isFileHandlerCreated = False
    isConsoleHandlerCreated = False

    def __init__(self,name):
        self.name = name
        self.logger = logging.getLogger('gdblib')
        self.logger.setLevel(self.logLevel)


    @classmethod
    def enable(cls, enabled):
        cls.enabled = enabled

    @classmethod
    def isEnabled(cls):
        return cls.enabled

    @classmethod
    def logToFile(cls, filename):
        if len(filename) > 0 and cls.isFileHandlerCreated == False:
            cls.fileHandler = logging.FileHandler(filename)
            cls.fileHandler.setFormatter(cls.formatter)
            cls.logger = logging.getLogger('gdblib')
            cls.logger.addHandler(cls.fileHandler)
            cls.isFileHandlerCreated = True

        elif len(filename) == 0 and cls.isFileHandlerCreated == True:
            cls.logger = logging.getLogger('gdblib')
            cls.logger.removeHandler(cls.fileHandler)
            cls.isFileHandlerCreated = False

    @classmethod
    def logToConsole(cls, console):
        if console == True and cls.isConsoleHandlerCreated == False:
            cls.consoleHandler = logging.StreamHandler()
            cls.consoleHandler.setFormatter(cls.formatter)
            cls.logger = logging.getLogger('gdblib')
            cls.logger.addHandler(cls.consoleHandler)
            cls.isConsoleHandlerCreated = True

        elif console == False and cls.isConsoleHandlerCreated == True:
            cls.logger = logging.getLogger('gdblib')
            cls.logger.removeHandler(cls.consoleHandler)
            cls.isConsoleHandlerCreated = False

    @classmethod
    def level(cls, l):
        cls.logLevel = l

    def debug(self, data):
        if self.enabled == True:
            self.logger.debug(self.name + ' - ' + data)

    def info(self, data):
        if self.enabled == True:
            self.logger.info(self.name + ' - ' + data)

    def warn(self,data):
        if self.enabled == True:
            self.logger.warn(self.name + ' - ' + data)

    def error(self,data):
        if self.enabled == True:
            self.logger.error(self.name + ' - ' + data)

    def critical(self,data):
        if self.enabled == True:
            self.logger.critical(self.name + ' - ' + data)
