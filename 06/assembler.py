# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 15:25:07 2021

@author: 10906309
"""

from Parse import Parse
from SymbolTable import SymbolTable
import Code, sys
import os
SymbolTable = SymbolTable()

def pass1():
    file = sys.argv[1]
    parser = Parse(file)
    i = 0
    while parser.hasMoreCommands():
        parser.advance()
        commandType = parser.commandType()
        if (commandType == "L_COMMAND"):
            SymbolTable.addEntryROM(parser.symbol(), i)
            i -= 1
        i+=1

def pass2():
    file = sys.argv[1]
    parser = Parse(file)
    try:
        os.remove('{}ans.hack'.format(file[:-4]))
    except:
        pass
    with open('{}ans.hack'.format(file[:-4]), 'xt') as fileBin:
        while parser.hasMoreCommands():
            parser.advance()
            commandType = parser.commandType()
            if (commandType == "A_COMMAND"):
                symbol = parser.symbol()
                try:
                    int(symbol)
                except:
                    if (not SymbolTable.contains(symbol)):
                        SymbolTable.addEntry(symbol)
                    symbol = str(SymbolTable.getAddr(symbol))
                fileBin.write(Code.getA(symbol)+'\n')
            elif (commandType == "C_COMMAND"):
                dest = parser.dest()
                comp = parser.comp()
                jump = parser.jump()
                fileBin.write(Code.getC(dest, comp, jump)+'\n')
             
                
def main():
    pass1()
    pass2()
    

if __name__ == "__main__":
    main()     