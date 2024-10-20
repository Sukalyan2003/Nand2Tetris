(LOOP)
	@KBD
	D=M
	@R0
	M=D
	@LOOP
	0;JMP
// Successfully takes keyboard input and shoves it into RAM[0]
