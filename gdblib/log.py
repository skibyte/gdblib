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
#                                                                                                                              
import logging

class Logger:
    enabled = False
    level = logging.DEBUG

    def __init__(self,name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(self.level)
        self.consoleHandler = logging.StreamHandler()
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.consoleHandler.setFormatter(self.formatter)
        self.logger.addHandler(self.consoleHandler)

    def logInConsole(self):
        self.logger.addHandler(self.consoleHandler)
    
    def debug(self, data):
        if self.enabled == True:
            self.logger.debug(data)

    def info(self, data):
        if self.enabled == True:
            self.logger.info(data)

    def warn(self,data):
        if self.enabled == True:
            self.logger.warn(data)
    
    def error(self,data):
        if self.enabled == True:
            self.logger.error(data)

    def critical(self,data):
        if self.enabled == True:
            self.logger.critical(data)
