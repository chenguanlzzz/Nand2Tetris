# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 20:39:12 2021

@author: 10906309
"""

class SymbolTable():
    def __init__(self):
        self.symbols = {'SP':0, 'LCL':1, 'ARG':2, 'THIS':3, 'THAT':4,
               'R0':0, 'R1':1, 'R2':2, 'R3':3, 'R4':4, 'R5':5, 'R6':6, 'R7':7,
               'R8':8, 'R9':9, 'R10':10, 'R11':11, 'R12':12, 'R13':13, 'R14':14, 'R15':15,
               'SCREEN':0x4000, 'KBD':0x6000}
        self.lastAddr = 15
     
    def contains(self, symbol):
        return symbol in self.symbols
      
    def addEntry(self, symbol):
        if (not self.contains(symbol)):
            self.lastAddr += 1
            self.symbols[symbol] = self.lastAddr
            
    def addEntryROM(self, symbol, addr):
        self.symbols[symbol] = addr
            
    def getAddr(self, symbol):
        return self.symbols[symbol]
        