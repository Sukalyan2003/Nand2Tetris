# Hack Assembler - Nand2Tetris Project 06

A two-pass assembler for the Hack assembly language, converting `.asm` files to `.hack` binary files. This implementation is part of the Nand2Tetris course and translates Hack assembly instructions into 16-bit binary machine code.

## Overview

This assembler processes Hack assembly language files and generates binary machine code. It handles three types of instructions:
- **A-instructions**: Address instructions (`@value`)
- **C-instructions**: Computation instructions (`dest=comp;jump`) 
- **L-instructions**: Label declarations (`(LABEL)`)

The assembler uses Python for easier syntax and readability, diverging from the C++ tutorials to avoid blind copying.

## Specification

https://drive.google.com/file/d/1S5MD3scFSlocH829_v1IJHIHKaVcEZc9/view

refer to the above charts for guidance. Not my chart, got it off youtube from [this video](https://www.youtube.com/watch?v=TZ10SOChdPo&list=PLT4mIxZjQO1rTavJ5zelv_gr0rR7lkAwm&index=8&pp=iAQB)

This clearly summarizes the entire specification as mentioned in the book. I suppose realizing this was a big part of this assignment, but even if i tried to, i'm just too lazy to make such a comprehensive chart. 

I did go through the chapter and verify that it's accurate. 

## Implementation

The assembler is implemented using a modular approach with separate Python files, each handling specific responsibilities:

### HackAssembler.py - Main Assembler Module

The main entry point that orchestrates the two-pass assembly process:

**Features:**
- **Command-line interface**: Takes `.asm` file as argument
- **Two-pass algorithm**: 
  - First pass: Builds symbol table from label instructions
  - Second pass: Translates all instructions to binary
- **Symbol resolution**: Handles both numeric addresses and symbolic references
- **Output generation**: Creates `.hack` files with 16-bit binary instructions
- **Error handling**: Validates undefined symbols and instruction formats

**Usage:** `python HackAssembler.py Prog.asm`

### Parser.py - Instruction Parser

Handles reading and parsing of assembly source files:

**Key Methods:**
- `hasMoreLines()`: Checks for remaining lines to process
- `advance()`: Moves to next valid instruction (skips comments and empty lines)
- `instructionType()`: Identifies instruction type (A, C, or L)
- `symbol()`: Extracts symbols from A and L instructions
- `dest()`, `comp()`, `jump()`: Parses components of C-instructions

**Features:**
- **Comment filtering**: Automatically skips `//` comments and empty lines
- **Instruction validation**: Ensures proper syntax for all instruction types
- **Symbol recognition**: Handles predefined symbols (LOOP, STOP, END)
- **Component extraction**: Breaks down C-instructions into dest, comp, and jump parts

### Code.py - Binary Translation Module

Translates assembly mnemonics to binary machine code:

**Translation Tables:**
- **DEST_TABLE**: Maps destination mnemonics to 3-bit codes (M, D, A, MD, AM, AD, AMD)
- **COMP_TABLE**: Maps computation mnemonics to 7-bit codes (includes both A and M variants)
- **JUMP_TABLE**: Maps jump conditions to 3-bit codes (JGT, JEQ, JGE, JLT, JNE, JLE, JMP)

**Key Methods:**
- `dest(mnemonic)`: Returns 3-bit binary code for destination field
- `comp(mnemonic)`: Returns 7-bit binary code for computation field  
- `jump(mnemonic)`: Returns 3-bit binary code for jump condition

**Features:**
- **Complete mnemonic coverage**: Supports all Hack assembly mnemonics
- **A/M register handling**: Separate codes for A-register and M-memory operations
- **Error validation**: Raises exceptions for invalid mnemonics


## Assembly Process

### Two-Pass Algorithm

1. **First Pass (Symbol Table Construction)**:
   - Scans through all instructions
   - Records label positions (L-instructions) in symbol table
   - Maintains ROM address counter for proper label addressing

2. **Second Pass (Code Generation)**:
   - Translates A-instructions to 16-bit binary addresses
   - Converts C-instructions to 16-bit binary (111 + comp + dest + jump)
   - Resolves symbols using the symbol table from first pass

### Binary Instruction Format

- **A-instruction**: `0vvvvvvvvvvvvvvv` (15-bit address/value)
- **C-instruction**: `111accccccdddjjj` (3-bit prefix + 7-bit comp + 3-bit dest + 3-bit jump)

## File Structure

```
06/
├── HackAssembler.py    # Main assembler entry point
├── Parser.py           # Assembly file parser
├── Code.py            # Binary code translator
├── Add.asm            # Sample assembly files
├── MaxL.asm
├── PongL.asm
├── RectL.asm
├── *.hack             # Generated binary output files
└── readme.md          # This documentation
```

## Usage Examples

```bash
# Assemble a single file
python HackAssembler.py Add.asm

# This generates Add.hack with binary machine code
```

## Future Improvements

### Enhanced Error Handling
- **Line number reporting**: Show exact location of syntax errors
- **Detailed error messages**: Provide specific guidance for common mistakes
- **Symbol validation**: Check for undefined or duplicate symbols
- **Instruction validation**: Verify proper mnemonic usage

### File Management
- **Batch processing**: Handle multiple `.asm` files at once
- **Directory operations**: Process entire folders of assembly files
- **Output customization**: Allow custom output file names and locations
- **Backup creation**: Optional backup of existing `.hack` files

### Development Features
- **Debug mode**: Verbose output showing symbol table and translation steps
- **Assembly listing**: Generate annotated output showing original and binary code
- **Performance optimization**: Faster parsing for large assembly files

