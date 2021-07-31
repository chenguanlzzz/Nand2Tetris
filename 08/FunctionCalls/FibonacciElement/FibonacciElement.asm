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

// function Main.fibonacci 0 
(Main.fibonacci)

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

// push constant 2 
@2 
D=A 
@SP 
A=M 
M=D 
@SP 
M=M+1 

// lt 
@SP 
AM=M-1 
D=M 
A=A-1 
D=M-D 
@LT0 
D;JLT 
@SP 
A=M-1 
M=0 
@END0 
0;JMP 
(LT0) 
@SP 
A=M-1 
M=-1 
(END0) 

// if-goto IF_TRUE 
@SP 
AM=M-1 
D=M 
@IF_TRUE 
D;JGT 

// goto IF_FALSE 
@IF_FALSE 
0;JMP 

// label IF_TRUE 
(IF_TRUE)

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

// label IF_FALSE 
(IF_FALSE)

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

// push constant 2 
@2 
D=A 
@SP 
A=M 
M=D 
@SP 
M=M+1 

// sub 
@SP 
AM=M-1 
D=M 
A=A-1 
M=M-D 

// call Main.fibonacci 1 
@Main$ret.1 
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
@1 
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
@Main.fibonacci 
0;JMP 
(Main$ret.1) 

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

// push constant 1 
@1 
D=A 
@SP 
A=M 
M=D 
@SP 
M=M+1 

// sub 
@SP 
AM=M-1 
D=M 
A=A-1 
M=M-D 

// call Main.fibonacci 1 
@Main$ret.2 
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
@1 
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
@Main.fibonacci 
0;JMP 
(Main$ret.2) 

// add 
@SP 
AM=M-1 
D=M 
A=A-1 
M=M+D 

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

// push constant 4 
@4 
D=A 
@SP 
A=M 
M=D 
@SP 
M=M+1 

// call Main.fibonacci 1 
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
@1 
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
@Main.fibonacci 
0;JMP 
(Sys$ret.3) 

// label WHILE 
(WHILE)

// goto WHILE 
@WHILE 
0;JMP 
