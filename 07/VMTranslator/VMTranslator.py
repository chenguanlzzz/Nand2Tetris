# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 13:09:34 2021

@author: 10906309
"""

from Parser import Parser
from CodeWriter import CodeWriter
import sys, os

def main():
    file = sys.argv[1]
    try:
        os.remove('{}.asm'.format(file[:-3]))
    except:
        pass
    parser = Parser(file)
    fout = CodeWriter(file)
    while parser.hasMoreCommands():
        parser.advance()
        commandType = parser.commandType()
        line = parser.lineStr()
        fout.writeArithmetic(commandType, line)
        fout.writePush(commandType, line)
        fout.writePop(commandType, line)
    fout.close
    
if __name__ == "__main__":
    main()     