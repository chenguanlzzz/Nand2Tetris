
// function SimpleFunction.test 2 
(SimpleFunction.test)
@0 
D=A 
@SP 
A=M 
M=D 
@SP 
M=M+1 
@0 
D=A 
@SP 
A=M 
M=D 
@SP 
M=M+1 

// push local 0 
@LCL 
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

// push local 1 
@LCL 
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

// add 
@SP 
AM=M-1 
D=M 
A=A-1 
M=M+D 

// not 
@SP 
A=M-1 
M=!M 

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

// add 
@SP 
AM=M-1 
D=M 
A=A-1 
M=M+D 

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
A=M 
A=A-D 
D=M 
@SimpleFunction$ret.0 
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
@SimpleFunction$ret.0 
A=M 
0;JMP 
