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
from distutils.core import setup, Command
import os
import sys
import subprocess
from gdblib import alltests
from gdblib import readme

class ReadmeTestCommand (Command):
    description = "readme test task"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.call(["make", "-C","gdblib/testapplication"])
        sys.exit(readme.main())

class TestCommand (Command):
    description = "test task"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.call(["make", "-C","gdblib/testapplication"])
        sys.exit(alltests.main())

class CoverageCommand (Command):
    description = "coverage task"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from coverage import coverage
        cov = coverage()
        cov.start()
        subprocess.call(["make", "-C","gdblib/testapplication"])
        alltests.main()
        cov.stop()
        cov.html_report(directory='build/covhtml')

setup(
    name="gdblib",
    description="A gdb module interface",
    version="0.4.8",
    author="Fernando Castillo",
    author_email="skibyte@gmail.com",
    url = "https://github.com/skibyte/gdblib",
    packages=["gdblib"],
    keywords=["gdb", "python"],
    cmdclass = {
        'test' : TestCommand,
        'coverage' : CoverageCommand,
        'readme' : ReadmeTestCommand
    }
)

