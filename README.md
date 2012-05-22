Gdb lib
=======

Usage
-----

gdb = GDB()
gdb.connectApp()
gdb.addBreakpoint('main.c', 54)
gdb.deleteBreakpoint('main.c', 54)
breakpoints = gdb.getBreakpoins()
gdb.addNewFileLocationListener(listener)
gdb.addConsoleListener(listener)
gdb.run()
gdb.step()
gdb.next()
gdb.changeDirectory()
gdb.addDirectory()
gdb.disconnect()
gdb.getSourceCodeFiles()
gdb.continue()
gdb.isConnected()

TODO
----
Add remote debugging support
Add attach process support
Add core support
