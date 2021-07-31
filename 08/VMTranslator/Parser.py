# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 18:22:00 2021

@author: 10906309
"""

# C_ARITHMETIC = 0
# C_PUSH = 1
# C_POP = 2
# C_LABEL = 3
# C_GOTO = 4
# C_IF = 5
# C_FUNCTION = 6
# C_RETURN = 7
# C_CALL = 8
C = {0: ["add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"], 1: ["push"], 2: ["pop"],
        3: ["label"], 4:["if-goto"], 5:["goto"], 6:["function"], 7:["return"], 8:["call"]}
# Parser module
class Parser():
    def __init__(self, file):
        fin = open(file, 'r')
        self.lines = fin.readlines()
        fin.close()
        self.curLine = 0
        self.lenLines = len(self.lines)
        self.line = ""
        self.Type = -1
        
    def hasMoreCommands(self):
        if self.curLine < self.lenLines:
            return True
        return False
    
    def advance(self):
        while self.hasMoreCommands():
            line = self.lines[self.curLine]
            commentIndex = line.find('//')
            
            # check the line is newline or the comment line?
            if line == '\n' or commentIndex == 0:
                self.curLine += 1
                continue
                
           
            if commentIndex > 0:
                line = line[:commentIndex-1]      # Delete the comment part & newLine character
            line = line.strip()        # Remove space、tabs、newLine
            self.line = line
            self.curLine += 1
            self.Type = self.commandType()
            break
            
    def commandType(self):
        line = self.line.split()
        if line[0] in C[0]:
            return 0
        elif line[0] in C[1]:
            return 1
        elif line[0] in C[2]:
            return 2
        elif line[0] in C[3]:
            return 3
        elif line[0] in C[4]:
            return 4
        elif line[0] in C[5]:
            return 5
        elif line[0] in C[6]:
            return 6
        elif line[0] in C[7]:
            return 7
        elif line[0] in C[8]:
            return 8
        
        
    def arg1(self):
        line = self.line
        if self.Type == 0:
            return
        return line[1]
    
    def arg2(self):
        line = self.line
        if self.Type == 1 or self.Type == 2 or self.Type == 6 or self.Type == 8:
            return line[2]
        return
        
    def lineStr(self):
        return self.line.split()