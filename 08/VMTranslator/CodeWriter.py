# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 18:54:08 2021

@author: 10906309
"""
# C = {0: ["add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"], 1: ["push"], 2: ["pop"]}
class CodeWriter():
    def __init__(self, file):
        self.foutName = file + '/' +file + '.asm'
        self.fout = open(self.foutName, 'xt')
        self.eqNum = 0
        self.endNum = 0
        self.gtNum = 0
        self.ltNum = 0
        self.retNum = 0
        
    def close(self):
        self.fout.close()
        
    def lineComment(self, line):
        lines = ""
        for word in line:
            lines = lines + word + " "
        self.fout.write("\n// " + lines + "\n")
        
    def writeArithmetic(self, commandType, line):
        if commandType == 0:      
            self.lineComment(line)
            if line[0] == 'add':
                self.arithTemplate1()
                self.fout.write("M=M+D \n")
               
            elif line[0] == 'sub':
                self.arithTemplate1()
                self.fout.write("M=M-D \n")
                
            elif line[0] == 'neg':
                self.fout.write("@SP \n"
                                +"A=M-1 \n"
                                +"M=-M \n")
            
            elif line[0] == 'eq':
                self.arithTemplate1()
                self.fout.write("D=M-D \n"
                                +f'@EQ{self.eqNum} \n'
                                +"D;JEQ \n"
                                +"@SP \n"
                                +"A=M-1 \n"
                                +"M=0 \n"
                                +f"@END{self.endNum} \n"
                                +"0;JMP \n"
                                +f"(EQ{self.eqNum}) \n"
                                +"@SP \n"
                                +"A=M-1 \n"
                                +"M=-1 \n"
                                +f"(END{self.endNum}) \n")
                self.eqNum += 1
                self.endNum += 1
                     
            elif line[0] == "gt":
                self.arithTemplate1()
                self.fout.write("D=M-D \n"
                                +f'@GT{self.gtNum} \n'
                                +"D;JGT \n"
                                +"@SP \n"
                                +"A=M-1 \n"
                                +"M=0 \n"
                                +f"@END{self.endNum} \n"
                                +"0;JMP \n"
                                +f"(GT{self.gtNum}) \n"
                                +"@SP \n"
                                +"A=M-1 \n"
                                +"M=-1 \n"
                                +f"(END{self.endNum}) \n")
                self.gtNum += 1
                self.endNum += 1
            
            elif line[0] == 'lt':
                self.arithTemplate1()
                self.fout.write("D=M-D \n"
                                +f"@LT{self.ltNum} \n"
                                +"D;JLT \n"
                                +"@SP \n"
                                +"A=M-1 \n"
                                +"M=0 \n"
                                +f"@END{self.endNum} \n"
                                +"0;JMP \n"
                                +f"(LT{self.ltNum}) \n"
                                +"@SP \n"
                                +"A=M-1 \n"
                                +"M=-1 \n"
                                +f"(END{self.endNum}) \n")
                self.ltNum += 1
                self.endNum += 1
                
            elif line[0] == 'and':
                self.arithTemplate1()
                self.fout.write("D=D&M \n"
                                +"@SP \n"
                                +"A=M-1 \n"
                                +"M=D \n")
                
            elif line[0] == 'or':
                self.arithTemplate1()
                self.fout.write("D=D|M \n"
                                +"@SP \n"
                                +"A=M-1 \n"
                                +"M=D \n")
                
            elif line[0] == 'not':
                self.fout.write("@SP \n"
                                +"A=M-1 \n"
                                +"M=!M \n")
                
            
    def arithTemplate1(self):
        self.fout.write("@SP \n"
                        +"AM=M-1 \n"      ## SP--; *SP
                        +"D=M \n"        
                        +"A=A-1 \n")
        
    def writePush(self, commandType, line):
        if commandType == 1:     
            self.lineComment(line)
            if line[1] == 'constant':
                self.fout.write(f"@{line[2]} \n"
                                +"D=A \n")
                self.pushTemplate1()
                 
            elif line[1] == 'local':
                self.fout.write("@LCL \n")
                self.pushTemplate2(line)
                self.pushTemplate1()
                
            elif line[1] == 'argument':
                self.fout.write("@ARG \n")
                self.pushTemplate2(line)
                self.pushTemplate1()
                
            elif line[1] == 'this':
                self.fout.write("@THIS \n")
                self.pushTemplate2(line)
                self.pushTemplate1()
            
            elif line[1] == 'that':
                self.fout.write("@THAT \n")
                self.pushTemplate2(line)
                self.pushTemplate1()
                
            elif line[1] == 'temp':
                self.fout.write("@5 \n"
                                +"D=A \n"
                                +f"@{line[2]} \n"
                                +"D=D+A \n"
                                +"A=D \n"
                                +"D=M \n")
                self.pushTemplate1()
                
            elif line[1] == 'static':
                staticFile = self.foutName.split('/')[0] + str(line[2])
                self.fout.write('@' + staticFile +' \n')
                self.pushTemplate3()
                
            
            elif line[1] == 'pointer':
                if line[2] == '0':    ## push THIS
                    self.fout.write('@THIS \n')
                    self.pushTemplate3()
                elif line[2] == '1':  ## push THAT
                    self.fout.write('@THAT \n')
                    self.pushTemplate3()
        
        
    def writePop(self, commandType, line):
        if commandType == 2:     
            self.lineComment(line)
            if line[1] == 'local':
                self.fout.write("@LCL \n")
                self.popTemplate1(line)
                
            elif line[1] == 'argument':
                self.fout.write("@ARG \n")
                self.popTemplate1(line)
                
            elif line[1] == 'this':
                self.fout.write("@THIS \n")
                self.popTemplate1(line)
            
            elif line[1] == 'that':
                self.fout.write("@THAT \n")
                self.popTemplate1(line)
                
            elif line[1] == 'temp':
                self.fout.write("@5 \n"
                                +'D=A \n'
                                +f'@{line[2]} \n'
                                +'D=D+A \n'
                                +'@addr \n'
                                +'M=D \n' 
                                +'@SP \n'
                                +'AM=M-1 \n'
                                +'D=M \n'
                                +'@addr \n'
                                +'A=M \n'
                                +'M=D \n')
                
            elif line[1] == 'static':
                staticFile = self.foutName[:-3].split('/')[0] + str(line[2])
                self.fout.write('@SP \n'
                                +'AM=M-1 \n'
                                +'D=M \n'
                                +'@' + staticFile +' \n'
                                +'M=D \n')
                
            elif line[1] == 'pointer':
                if line[2] == '0':    ## pop THIS
                     self.fout.write('@SP \n'
                                     +'AM=M-1 \n'
                                     +'D=M \n'
                                     +'@THIS \n'
                                     +'M=D \n')
                elif line[2] == '1':  ## pop THAT
                    self.fout.write('@SP \n'
                                     +'AM=M-1 \n'
                                     +'D=M \n'
                                     +'@THAT \n'
                                     +'M=D \n')
        
    def pushTemplate1(self):
        self.fout.write("@SP \n"
                        +"A=M \n"
                        +"M=D \n"
                        +"@SP \n"
                        +"M=M+1 \n")
        
    def pushTemplate2(self, line):
        self.fout.write("D=M \n"
                        +f"@{line[2]} \n"
                        +"D=D+A \n"
                        +"A=D \n"
                        +"D=M \n")
        
    def pushTemplate3(self):
        self.fout.write('D=M \n'
                        +'@SP \n'
                        +'AM=M+1 \n'
                        +'A=A-1 \n'
                        +'M=D \n')
        
    def popTemplate1(self, line):
        self.fout.write('D=M \n'
                        +f'@{line[2]} \n'
                        +'D=D+A \n'
                        +'@addr \n'
                        +'M=D \n' 
                        +'@SP \n'
                        +'AM=M-1 \n'
                        +'D=M \n'
                        +'@addr \n'
                        +'A=M \n'
                        +'M=D \n')

    def writeLabel(self, commandType, line):
        if commandType == 3:
            self.lineComment(line)
            self.fout.write('(' + f'{line[1]}' + ')\n')

    def writeIf(self, commandType, line):
        if commandType == 4:
            self.lineComment(line)
            self.fout.write('@SP \n'
                            +'AM=M-1 \n'
                            +'D=M \n'
                            +f'@{line[1]} \n'
                            +'D;JGT \n')
    
    def writeGoTo(self, commandType, line):
        if commandType == 5:
            self.lineComment(line)
            self.fout.write(f'@{line[1]} \n'
                            +'0;JMP \n')
    
    def writeFunction(self, commandType, line):
        if commandType == 6:
            self.lineComment(line)
            self.fout.write('(' + f'{line[1]}' + ')\n')
            for i in range(int(line[2])):
                self.fout.write("@0 \n"
                                +"D=A \n")
                self.pushTemplate1()
    
    def writeReturn(self, commandType, line):
        if commandType == 7:
            self.lineComment(line)
            self.fout.write('@LCL \n'         # endframe is a temporary variable  endFrame=LCL
                            +'D=M \n'
                            +'@endFrame \n'
                            +'M=D \n'
                            +'@5 \n'           # gets the return address    retAddr = *(endFrame-5)
                            +'D=A \n'
                            +'@endFrame \n'
                            +'D=M-D \n'
                            +'A=D \n'        
                            +'D=M \n'
                            +'@retAddr \n'
                            +'M=D \n'
                            +'@SP \n'           # repositions the return value for the caller    *ARG=pop()
                            +'AM=M-1 \n'
                            +'D=M \n'
                            +'@ARG \n'
                            +'A=M \n'
                            +'M=D \n'
                            +'D=A+1 \n'         # repositions SP of the caller     SP=ARG+1
                            +'@SP \n'
                            +'M=D \n'
                            +'@endFrame \n'     # restores THAT of the caller      THAT=*(endFrame-1)
                            +'A=M-1 \n'
                            +'D=M \n'
                            +'@THAT \n'
                            +'M=D \n'
                            +'@2 \n'            # restores THIS of the caller      THIS=*(endFrame-2)
                            +'D=A \n'
                            +'@endFrame \n'
                            +'A=M-D \n'
                            +'D=M \n'
                            +'@THIS \n'
                            +'M=D \n'
                            +'@3 \n'            # restores ARG of the caller      ARG=*(endFrame-3)
                            +'D=A \n'
                            +'@endFrame \n'
                            +'A=M-D \n'
                            +'D=M \n'
                            +'@ARG \n'
                            +'M=D \n'
                            +'@4 \n'            # restores LCL of the caller      LCL=*(endFrame-4)
                            +'D=A \n'
                            +'@endFrame \n'
                            +'A=M-D \n'
                            +'D=M \n'
                            +'@LCL \n'
                            +'M=D \n'
                            +'@retAddr \n'    # goes to the caller’s return address    goto retAddr
                            +'A=M \n'
                            +'0;JMP \n')       

    def writeInit(self):
        self.fout.write('@256 \n'
                        +'D=A \n'
                        +'@SP \n'
                        +'M=D \n')
        self.writeCall(8, ['call', 'Sys.init', '0'], '/Sys.vm')

    def writeCall(self, commandType, line, file):
        if commandType == 8:
            self.lineComment(line)
            funcRet = file.split('/')[1][:-3] + f'$ret.{self.retNum}'
            self.fout.write(f'@{funcRet} \n'
                            +'D=A \n')
            self.pushTemplate1()
            self.fout.write('@LCL \n'
                            +'D=M \n')
            self.pushTemplate1()
            self.fout.write('@ARG \n'
                            +'D=M \n')
            self.pushTemplate1()
            self.fout.write('@THIS \n'
                            +'D=M \n')
            self.pushTemplate1()
            self.fout.write('@THAT \n'
                            +'D=M \n')
            self.pushTemplate1()
            self.fout.write(f'@{line[2]} \n'
                            +'D=A \n'
                            +'@5 \n'
                            +'D=D+A \n'
                            +'@SP \n'
                            +'D=M-D \n'
                            +'@ARG \n'
                            +'M=D \n'
                            +'@SP \n'
                            +'D=M \n'
                            +'@LCL \n'
                            +'M=D \n'
                            +f'@{line[1]} \n'
                            +'0;JMP \n'
                            +f'({funcRet}) \n')
            self.retNum += 1
                    
