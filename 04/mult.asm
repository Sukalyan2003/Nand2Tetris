@R2
M=0
@i
M=0
(LOOP)
	@i
	D=M
	@R0
	D=M-D
	@END
	D;JEQ
	// So far checks if i==R1
	// Next up, actually repeatedly adding
	@R1
	D=M
	@R2
	M=D+M
	//Now to increment i
	@i
	M=M+1
	@LOOP
	0;JMP
(END)
	@END
	0;JMP
