# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 13:09:34 2021

@author: 10906309
"""

from Parser import C, Parser
from CodeWriter import CodeWriter
import sys, os, glob

def main():
    files = glob.glob(sys.argv[1] + '/*.vm')
    filePath = sys.argv[1] + '/' + sys.argv[1]
    try:
        os.remove('{}.asm'.format(filePath))
    except:
        pass
    fout = CodeWriter(sys.argv[1])
    fout.writeInit()
    for file in files:
        parser = Parser(file)
        while parser.hasMoreCommands():
            parser.advance()
            commandType = parser.commandType()
            line = parser.lineStr()
            fout.writeArithmetic(commandType, line)
            fout.writePush(commandType, line)
            fout.writePop(commandType, line)
            fout.writeLabel(commandType, line)
            fout.writeIf(commandType, line)
            fout.writeGoTo(commandType, line)
            fout.writeFunction(commandType, line)
            fout.writeReturn(commandType, line)
            fout.writeCall(commandType, line, file)
        fout.close
    
if __name__ == "__main__":
    main()     