// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// n: all RAMs that scrren have
// i: number to count in the LOOPFILL or LOOPCLC
@KBD
D=A
@SCREEN
D=D-A
@n
M=D

// LOOPINF:
//		set i = 0
// 		if (KBD is pressed): goto LOOPFILL
//		else: goto LOOPCLC
//		goto LOOPINF

// LOOPFILL:
//		if (i >= n): goto LOOPINF
//		RAM[SCREEN+i] = -1
//		i++
//		goto LOOPFILL

// LOOPCLC:
//		if (i >= n): goto LOOPINF
//		RAM[SCREEN+i] = 0
// 		i++
// 		goto LOOPCLC

(LOOPINF)
	@i
	M=0         //set i = 0
	@KBD
	D=M
	@LOOPFILL
	D;JNE		// if KBD is pressed -> goto fill screen
	@LOOPCLC
	D;JEQ		// if KBD is not pressed -> goto clear screen
	@LOOPINF
	0;JMP
	
(LOOPFILL)
	@i
	D=M
	@n
	D=D-M
	@LOOPINF	
	D;JGE   	// if i >= n: break this loop, go back to infinite loop
	@SCREEN
	D=A
	@i
	D=D+M
	A=D
	M=-1		// RAM[SCREEN+i] = -1
	@i
	M=M+1		// i++
	@LOOPFILL
	0;JMP
	
(LOOPCLC)
	@i
	D=M
	@n
	D=D-M
	@LOOPINF	
	D;JGE   	// if i >= n: break this loop, go back to infinite loop
	@SCREEN
	D=A
	@i
	D=D+M
	A=D
	M=0			// RAM[SCREEN+i] = -1
	@i
	M=M+1		// i++
	@LOOPCLC
	0;JMP