	// Set R0 value to your starting address THEN set R1 etc
	//RAM[0] Should not be your starting point!!!!!
	@i
	M=0
(LOOP)
	@i
	D=M
	@R1
	D=M-D
	@END
	D;JEQ
	@R0
	D=M
	@i
	A=D+M
	M=-1
	@i
	M=M+1
	@LOOP
	0;JMP
(END)
	@END
	0;JMP
