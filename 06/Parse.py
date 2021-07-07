# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 18:22:00 2021

@author: 10906309
"""

# Parser module
class Parse():
    def __init__(self, file):
        fin = open(file, 'r')
        self.lines = fin.readlines()
        fin.close()
        self.curLine = 0
        self.lenLines = len(self.lines)
        self.line = ""
        self.Type=""
        
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
                line = line[:commentIndex-2]      # Delete the comment part & newLine character
            line = line.strip()        # Remove space、tabs、newLine
            self.line = line
            self.curLine += 1
            self.Type = self.commandType()
            break
            
    def commandType(self):
        line = self.line
        if line[0] == '@':
            return "A_COMMAND"
        elif line[0] == '(':
            return "L_COMMAND"
        else:
            return "C_COMMAND"
        
    def symbol(self):
        line = self.line
        if self.Type == "A_COMMAND":
            return line[1:]
        elif self.Type == "L_COMMAND":
            return line[1:-1]
        else:
            return ""
        
    def dest(self):
        line = self.line
        equalIndex = line.find('=')
        if self.Type == "C_COMMAND" and equalIndex > 0:
            return line[:equalIndex]
        else:
            return ""
        
    def comp(self):
        line = self.line
        equalIndex = line.find('=') + 1
        semicolonIndex = line.find(';')
        if self.Type == "C_COMMAND":
            if semicolonIndex < 0:
                return line[equalIndex:]
            return line[equalIndex:semicolonIndex]
        else:
            return ""
        
    def jump(self):
        line = self.line
        semicolonIndex = line.find(';') + 1
        if semicolonIndex > 0:
            return line[semicolonIndex:]
        else:
            return ""