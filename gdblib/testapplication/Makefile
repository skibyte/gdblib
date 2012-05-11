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
CFLAGS=-g

app: functions.o main.o
	gcc $(CFLAGS) $^ -o $@

functions.o: module1/functions.c module1/functions.h 
	gcc $(CFLAGS) -c $<

main.o: main.c 
	gcc $(CFLAGS) -c $<

.PHONY: clean
clean:
	rm functions.o main.o app

