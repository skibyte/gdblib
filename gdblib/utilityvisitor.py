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
class UtilityVisitor():
    addDirectoryCommandVisited = False
    changeDirectoryCommandVisited = False;
    listSourceFilesCommandVisited = False;
    advanceCommandVisited = False;
    nextCommandVisited = False;
    stepCommandVisited = False;
    runCommandVisited = False;
    backtraceCommandVisited = False;
    printCommandVisited = False;
    printXCommandVisited = False;
    setVarCommandVisited = False;
    returnCommandVisited = False;
    continueCommandVisited = False;
    finishCommandVisited = False;
    whatIsCommandVisited = False;
    addBreakpointCommandVisited = False;
    deleteBreakpointCommandVisited = False;
    infoBreakpointCommandVisited = False;
    addWatchpointCommandVisited = False;
    deleteWatchpointCommandVisited = False;

    def visitAddDirectoryCommand(self, cmd):
        self.addDirectoryCommandVisited = True

    def isAddDirectoryCommandVisited(self):        
        return self.addDirectoryCommandVisited

    def visitChangeDirectoryCommand(self, cmd):
        self.changeDirectoryCommandVisited = True

    def isChangeDirectoryCommandVisited(self):        
        return self.changeDirectoryCommandVisited

    def visitListSourceFilesCommand(self, cmd):
        self.listSourceFilesCommandVisited = True

    def isListSourceFilesCommandVisited(self):        
        return self.listSourceFilesCommandVisited

    def visitAdvanceCommand(self, cmd):
        self.advanceCommandVisited = True

    def isAdvanceCommandVisited(self):        
        return self.advanceCommandVisited

    def visitNextCommand(self, cmd):
        self.nextCommandVisited = True

    def isNextCommandVisited(self):        
        return self.nextCommandVisited

    def visitStepCommand(self, cmd):
        self.stepCommandVisited = True

    def isStepCommandVisited(self):        
        return self.stepCommandVisited

    def visitRunCommand(self, cmd):
        self.runCommandVisited = True

    def isRunCommandVisited(self):        
        return self.runCommandVisited

    def visitBacktraceCommand(self, cmd):
        self.backtraceCommandVisited = True

    def isBacktraceCommandVisited(self):        
        return self.backtraceCommandVisited

    def visitPrintCommand(self, cmd):
        self.printCommandVisited = True

    def isPrintCommandVisited(self):        
        return self.printCommandVisited

    def visitPrintXCommand(self, cmd):
        self.printXCommandVisited = True

    def isPrintXCommandVisited(self):        
        return self.printXCommandVisited

    def visitSetVarCommand(self, cmd):
        self.setVarCommandVisited = True

    def isSetVarCommandVisited(self):        
        return self.setVarCommandVisited

    def visitReturnCommand(self, cmd):
        self.returnCommandVisited = True

    def isReturnCommandVisited(self):        
        return self.returnCommandVisited

    def visitContinueCommand(self, cmd):
        self.continueCommandVisited = True

    def isContinueCommandVisited(self):        
        return self.continueCommandVisited

    def visitFinishCommand(self, cmd):
        self.finishCommandVisited = True

    def isFinishCommandVisited(self):        
        return self.finishCommandVisited

    def visitWhatIsCommand(self, cmd):
        self.whatIsCommandVisited = True

    def isWhatIsCommandVisited(self):        
        return self.whatIsCommandVisited

    def visitAddBreakpointCommand(self, cmd):
        self.addBreakpointCommandVisited = True

    def isAddBreakpointCommandVisited(self):        
        return self.addBreakpointCommandVisited

    def visitDeleteBreakpointCommand(self, cmd):
        self.deleteBreakpointCommandVisited = True

    def isDeleteBreakpointCommandVisited(self):        
        return self.deleteBreakpointCommandVisited

    def visitInfoBreakpointCommand(self, cmd):
        self.infoBreakpointCommandVisited = True

    def isInfoBreakpointCommandVisited(self):        
        return self.infoBreakpointCommandVisited

    def visitAddWatchpointCommand(self, cmd):
        self.addWatchCommandVisited = True

    def isAddWatchpointCommandVisited(self):        
        return self.addWatchpointCommandVisited

    def visitDeleteWatchpointCommand(self, cmd):
        self.deleteWatchCommandVisited = True

    def isDeleteWatchpointCommandVisited(self):        
        return self.deleteWatchpointCommandVisited
