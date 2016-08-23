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

Enabling logs for Gdb lib
-------------------------
        # Log levels are defined in the standard logging module
        import logging

        gdblib.log.Logger.enable(True)
        gdblib.log.Logger.level(logging.DEBUG)
        gdblib.log.Logger.logToFile('gdblib.log')
        gdblib.log.Logger.logToConsole(True)

**Available log levels:**

        logging.DEBUG
        logging.INFO
        logging.WARNING
        logging.ERROR
        logging.CRITICAL

Todo
----
* Add attach process support
* Add core support
* Implement more gdb commands
* Any good suggestion you have

License
-------
Gdb lib is licenced under a LGPL v3 license. Please see COPYING file for details.

Report a bug
------------
If you find a bug in gdblib please let me know in the following page: https://github.com/skibyte/gdblib/issues
