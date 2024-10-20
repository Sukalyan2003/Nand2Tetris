// Each row in the physical screen,starting at the screens top-left 
//corner, is represented in the RAM by thirty-two 
// consecutive 16-bit words
// Basically we start at @SCREEN and set the next 
// 8192 memory locations to 1
@SCREEN
D=A
@i
M=D
@count
M=0
(LOOP)
	@i
	A=M
	M=-1
	@i
	M=M+1
	@count
	M=M+1
	@8192
	D=A
	@count
	D=M-D
	@LOOP
	D;JNE
(END)
	@END
	0;JMP

// So from this what i learned is that, if you want to assign a value to D or something, 
// Instead of directly equating it, which will give you an error, 
// Just @1234 and then D=A to it. My original code tried to use the counter for everything
// and tried to take the SCREEN symbol in every loop iteration and that was giving errors. 