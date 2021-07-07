# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 18:26:15 2021

@author: 10906309
"""
destToBin = {"": "000", "M":"001", "D":"010", "MD":"011", 
             "A":"100", "AM":"101", "AD":"110", "AMD":"111"}

compToBin = {'0':'0101010',  '1':'0111111',  '-1':'0111010', 'D':'0001100', 
             'A':'0110000',  '!D':'0001101', '!A':'0110001', '-D':'0001111', 
             '-A':'0110011', 'D+1':'0011111','A+1':'0110111','D-1':'0001110', 
             'A-1':'0110010','D+A':'0000010','D-A':'0010011','A-D':'0000111', 
             'D&A':'0000000', 'D|A':'0010101', 'M':'1110000', '!M':'1110001',
             '-M':'1110011', 'M+1':'1110111', 'M-1':'1110010','D+M':'1000010',
             'D-M':'1010011','M-D':'1000111', 'D&M':'1000000', 'D|M':'1010101'}

jumpToBin = {'':'000', 'JGT':'001', 'JEQ':'010', 'JGE':'011', 
             'JLT':'100', 'JNE':'101', 'JLE':'110', 'JMP':'111'}

def dest(destAsm):
    return destToBin[destAsm]

def comp(compAsm):
    return compToBin[compAsm]

def jump(jumpAsm):
    return jumpToBin[jumpAsm]

def getC(destAsm, compAsm, jumpAsm):
    return '111'+comp(compAsm)+dest(destAsm)+jump(jumpAsm)

def getA(addr):
    return bin(int(addr))[2:].zfill(16)