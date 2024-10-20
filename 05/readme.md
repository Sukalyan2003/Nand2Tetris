# Basic stuff
In this chapter, we make the CPU of the machine on which the assembler and everything of part two will be made.

 I've realized that I don't write much notes in obsidian for this anyways, so i'll just write everything in this folder readmes itself. 

 The chapter starts with an explanation of the stored program concept.

 Especially the Von neumann architecture, which specifies that the program and data are stored in the same memory and are treated the same way.

 This means that the same hardware can act completely differently depending on the software and most of it's functionaility is not hardcoded. 

 Physically, the memory is a linear sequence of addressable,fixed-size registers, each having a unique address and a value. Logically,this address space serves two purposes: storing data and storing instructions. Both the “instruction words” and the “data words” are
implemented exactly the same way—as sequences of bits.

In some variants of the von Neumann architecture, the data memory and the instruction memory are allocated and managed dynamically, as needed, within the same physical address space. In other variants, the data memory and the instruction memory are kept in two
physically separate memory units, each having its own distinct address space.

When the CPU works faster than the rate at which data can be fetched from the memory, the CPU will have to wait for the data to be fetched. This is called the Von Neumann bottleneck.
This is called Starvation. 

To fix this we have on CPU memory called the cache. And beyond that we have the registers. Which is a very small  amount of memory that is directly on the CPU.

To avoid learning about the specific engineering of each IO device, everything is abstracted into a memory mapped IO. This means that
every IO device is mapped to a specific memory address, which is constantly synchronized to check for changes. 

# The Hack specification

1. 16bit architecture with two memory spaces: data memory and instruction memory. And two specific IO devices, the screen and the keyboard.
2. The CPU consists of the ALU from project 2 and three registers A, D and PC.
3. 