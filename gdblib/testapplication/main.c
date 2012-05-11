/*
 * Gdblib - A gdb python library. 
 * Copyright (C) 2012  Fernando Castillo
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
#include "module1/header.h"

int main(int argc, char *argv[])
{
    struct point mypoint = {6, 7};


    print_point(&mypoint);
    modify_point(&mypoint);
    print_point(&mypoint);

    return 0;
}
