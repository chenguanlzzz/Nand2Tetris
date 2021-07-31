@256 
D=A 
@SP 
M=D 

// call Sys.init 0 
@Sys$ret.0 
D=A 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@LCL 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@ARG 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@THIS 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@THAT 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@0 
D=A 
@5 
D=D+A 
@SP 
D=M-D 
@ARG 
M=D 
@SP 
D=M 
@LCL 
M=D 
@Sys.init 
0;JMP 
(Sys$ret.0) 

// function Class1.set 0 
(Class1.set)

// push argument 0 
@ARG 
D=M 
@0 
D=D+A 
A=D 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 

// pop static 0 
@SP 
AM=M-1 
D=M 
@StaticsTest0 
M=D 

// push argument 1 
@ARG 
D=M 
@1 
D=D+A 
A=D 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 

// pop static 1 
@SP 
AM=M-1 
D=M 
@StaticsTest1 
M=D 

// push constant 0 
@0 
D=A 
@SP 
A=M 
M=D 
@SP 
M=M+1 

// return 
@LCL 
D=M 
@endFrame 
M=D 
@5 
D=A 
@endFrame 
D=M-D 
A=D 
D=M 
@retAddr 
M=D 
@SP 
AM=M-1 
D=M 
@ARG 
A=M 
M=D 
D=A+1 
@SP 
M=D 
@endFrame 
A=M-1 
D=M 
@THAT 
M=D 
@2 
D=A 
@endFrame 
A=M-D 
D=M 
@THIS 
M=D 
@3 
D=A 
@endFrame 
A=M-D 
D=M 
@ARG 
M=D 
@4 
D=A 
@endFrame 
A=M-D 
D=M 
@LCL 
M=D 
@retAddr 
A=M 
0;JMP 

// function Class1.get 0 
(Class1.get)

// push static 0 
@StaticsTest0 
D=M 
@SP 
AM=M+1 
A=A-1 
M=D 

// push static 1 
@StaticsTest1 
D=M 
@SP 
AM=M+1 
A=A-1 
M=D 

// sub 
@SP 
AM=M-1 
D=M 
A=A-1 
M=M-D 

// return 
@LCL 
D=M 
@endFrame 
M=D 
@5 
D=A 
@endFrame 
D=M-D 
A=D 
D=M 
@retAddr 
M=D 
@SP 
AM=M-1 
D=M 
@ARG 
A=M 
M=D 
D=A+1 
@SP 
M=D 
@endFrame 
A=M-1 
D=M 
@THAT 
M=D 
@2 
D=A 
@endFrame 
A=M-D 
D=M 
@THIS 
M=D 
@3 
D=A 
@endFrame 
A=M-D 
D=M 
@ARG 
M=D 
@4 
D=A 
@endFrame 
A=M-D 
D=M 
@LCL 
M=D 
@retAddr 
A=M 
0;JMP 

// function Sys.init 0 
(Sys.init)

// push constant 6 
@6 
D=A 
@SP 
A=M 
M=D 
@SP 
M=M+1 

// push constant 8 
@8 
D=A 
@SP 
A=M 
M=D 
@SP 
M=M+1 

// call Class1.set 2 
@Sys$ret.1 
D=A 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@LCL 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@ARG 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@THIS 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@THAT 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@2 
D=A 
@5 
D=D+A 
@SP 
D=M-D 
@ARG 
M=D 
@SP 
D=M 
@LCL 
M=D 
@Class1.set 
0;JMP 
(Sys$ret.1) 

// pop temp 0 
@5 
D=A 
@0 
D=D+A 
@addr 
M=D 
@SP 
AM=M-1 
D=M 
@addr 
A=M 
M=D 

// push constant 23 
@23 
D=A 
@SP 
A=M 
M=D 
@SP 
M=M+1 

// push constant 15 
@15 
D=A 
@SP 
A=M 
M=D 
@SP 
M=M+1 

// call Class2.set 2 
@Sys$ret.2 
D=A 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@LCL 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@ARG 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@THIS 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@THAT 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@2 
D=A 
@5 
D=D+A 
@SP 
D=M-D 
@ARG 
M=D 
@SP 
D=M 
@LCL 
M=D 
@Class2.set 
0;JMP 
(Sys$ret.2) 

// pop temp 0 
@5 
D=A 
@0 
D=D+A 
@addr 
M=D 
@SP 
AM=M-1 
D=M 
@addr 
A=M 
M=D 

// call Class1.get 0 
@Sys$ret.3 
D=A 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@LCL 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@ARG 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@THIS 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@THAT 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@0 
D=A 
@5 
D=D+A 
@SP 
D=M-D 
@ARG 
M=D 
@SP 
D=M 
@LCL 
M=D 
@Class1.get 
0;JMP 
(Sys$ret.3) 

// call Class2.get 0 
@Sys$ret.4 
D=A 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@LCL 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@ARG 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@THIS 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@THAT 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@0 
D=A 
@5 
D=D+A 
@SP 
D=M-D 
@ARG 
M=D 
@SP 
D=M 
@LCL 
M=D 
@Class2.get 
0;JMP 
(Sys$ret.4) 

// label WHILE 
(WHILE)

// goto WHILE 
@WHILE 
0;JMP 

// function Class2.set 0 
(Class2.set)

// push argument 0 
@ARG 
D=M 
@0 
D=D+A 
A=D 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 

// pop static 0 
@SP 
AM=M-1 
D=M 
@StaticsTest0 
M=D 

// push argument 1 
@ARG 
D=M 
@1 
D=D+A 
A=D 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 

// pop static 1 
@SP 
AM=M-1 
D=M 
@StaticsTest1 
M=D 

// push constant 0 
@0 
D=A 
@SP 
A=M 
M=D 
@SP 
M=M+1 

// return 
@LCL 
D=M 
@endFrame 
M=D 
@5 
D=A 
@endFrame 
D=M-D 
A=D 
D=M 
@retAddr 
M=D 
@SP 
AM=M-1 
D=M 
@ARG 
A=M 
M=D 
D=A+1 
@SP 
M=D 
@endFrame 
A=M-1 
D=M 
@THAT 
M=D 
@2 
D=A 
@endFrame 
A=M-D 
D=M 
@THIS 
M=D 
@3 
D=A 
@endFrame 
A=M-D 
D=M 
@ARG 
M=D 
@4 
D=A 
@endFrame 
A=M-D 
D=M 
@LCL 
M=D 
@retAddr 
A=M 
0;JMP 

// function Class2.get 0 
(Class2.get)

// push static 0 
@StaticsTest0 
D=M 
@SP 
AM=M+1 
A=A-1 
M=D 

// push static 1 
@StaticsTest1 
D=M 
@SP 
AM=M+1 
A=A-1 
M=D 

// sub 
@SP 
AM=M-1 
D=M 
A=A-1 
M=M-D 

// return 
@LCL 
D=M 
@endFrame 
M=D 
@5 
D=A 
@endFrame 
D=M-D 
A=D 
D=M 
@retAddr 
M=D 
@SP 
AM=M-1 
D=M 
@ARG 
A=M 
M=D 
D=A+1 
@SP 
M=D 
@endFrame 
A=M-1 
D=M 
@THAT 
M=D 
@2 
D=A 
@endFrame 
A=M-D 
D=M 
@THIS 
M=D 
@3 
D=A 
@endFrame 
A=M-D 
D=M 
@ARG 
M=D 
@4 
D=A 
@endFrame 
A=M-D 
D=M 
@LCL 
M=D 
@retAddr 
A=M 
0;JMP 
