Gdb lib
=======
Gdb lib is a python library aimed to work as a simple interface for gdb.

Contact
-------
**Author:** Fernando Castillo skibyte@gmail.com

Installation
------------
See INSTALL file for details

Usage
-----
        from gdblib import GDB

        gdb = GDB() 
        gdb.connectApp('application', 'application arguments')
        gdb.addBreakpoint('main.c', 54)
        gdb.deleteBreakpoint('main.c', 54)
        breakpoints = gdb.getBreakpoins()
        gdb.addNewFileLocationListener(listener)
        gdb.addStandardOutputListener(listener)
        gdb.run()
        gdb.step()
        gdb.next()
        gdb.disconnect()

Todo
----
* Add remote debugging support
* Add attach process support
* Add core support
* Implement more gdb commands
* Any good suggestion you have

License
-------
Gdb lib is licenced under a LGPL v3 license. Please see COPYING file for details.

Report a bug
------------
If you find a bug in walldo please let me know in the following page: https://github.com/skibyte/gdblib/issues
