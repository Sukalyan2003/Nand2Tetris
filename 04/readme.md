# This chapter deals with Writing some stuff in the Hack Machine language that we will finally implement in the next chapter. 

Some notes:

1. The currently selected Register of the RAM is called M.
2. The data register of CPU is named D. Stores a 16bit value 
3. Address register named A. Can work both as Data and Address register.

**Syntax for the Hack Machine code**

1. @xxx sets A=xxx. But it has some side effects too.
	1. M=xxx
	2. Selected instruction in the ROM = xxx
	So, depends on the command that follows it, A can act as either Data or Address register.
	And even in the Address part, A can either access the Data memory or the instruction memory.
2. if we want the program flow to jump to a specific location in the Instruction memory, then we set @xxx and then 
	write 0;JMP for unconditional branching
	to replicate something like if D==0 goto xxx, you write D;JEQ

3. Variables:
	These are written as @variable where the name can be anything. 
	The Hack specficiation includes 16 inbuilt symbols going from R0 to R15. These are called virtual registers
	The symbols SCREEEN and KBD are special keywords for the screen and keyboard respectively. They have a fixed value in the memory.

4. Label symbols
	LOOP
	STOP
	END
	always write them within () like (STOP) or (LOOP) 
5. The instruction memory is 0 indexed
	When a program is loaded, the nth line of the program is loaded into the address n in the instruction memory

6. Always end a program with an infinite loop or it will move ahead and start executing anything it finds next in the memory.

## Some experiments
Let's start with some pseudocode for the examples of the book, then try to translate it into assembly language.

( This mostly contains the final version of the code, probably the same as the book as I am reading it whenever i get stuck)


Q1) Calculate the sum of first N Positive integers where R0 = N. Then store the Sum in R1.

Pseudocode:
	initialize i = 1, sum = 0
	Run a loop that checks if D > R0 then goto STOP
	loop:
		sum = sum + i
		i  = i + 1
	goto loop
	STOP: 
		R1 = sum
	Then end the program.

Now let's try to write the assembly

The code is in sum.asm. Im using separate files as then i could import them into the Nand2Tetris IDE and run them 	

Q2) : Implement the array accessing system in the Hack assembly

The example in the book uses the notations to set all array indices to -1, but I want to try something different. Add the current index into the array. and if that works, i'll try to add the sum of all n numbers so far. 

This basically starts at R0 and accesses R1 number of indices from that start. 
Pseudocode: 
	i = 0
	LOOP
	if(i == R1) then goto end
	*(R0 + i) = i
	i = i+1
	goto LOOP
	END




## Second assigment

The first multiplication one was easy but the IO one needs some planning first. 

So, i'll do this in three steps.

Step1: Read input from keyboard and set it to memory to learn about keyboard input. DONE

Step2: Create an arbitrary pattern in screen (just blacked it tf out.) DONE

Step3: Connecting the dots and finishing the assignment.

Now to start working on step 3, 
We name the file Fill.asm as specified.

Pseudocode: 
	Start outer loop
		if KBD input == 0 then colour is white(0)
		if KBD input != colour is black(1 or -1)
		Start filling loop
			Fill the 8192 memory words with colour value
			Then goto repeat
	Repeat
		go to beginning of outer loop

And using this the code is complete. 



