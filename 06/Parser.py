class Parser:
    def __init__(self, filepath):
        with open(filepath) as f:
            self.lines = f.read().splitlines() # store the file contents as a list of lines
        
        self.pointer = 0
        self.currInstruction = ''
        self.instType = ''
        self.symbols = ('LOOP','STOP','END')

    def hasMoreLines(self) -> bool:
        return self.pointer < len(self.lines)

    def advance(self):
        while self.hasMoreLines() and (self.lines[self.pointer].strip() == "" or self.lines[self.pointer].strip().startswith("//")):
                self.pointer += 1
        if(self.hasMoreLines()):          
            self.currInstruction = self.lines[self.pointer].strip()
            self.pointer += 1
        else:
            raise StopIteration("No more lines")
    
    def instructionType(self):
        if self.currInstruction.startswith('@') and (
            self.currInstruction[1:].isdigit() or 
            self.currInstruction[1:] in self.symbols
        ):
            self.instType = 'A_INSTRUCTION'
            
        elif '=' in self.currInstruction or ';' in self.currInstruction:
            self.instType = 'C_INSTRUCTION'
        
        elif self.currInstruction.startswith('(') and self.currInstruction.endswith(')') and self.currInstruction[1:-1] in self.symbols:
            self.instType = 'L_INSTRUCTION'
        else:
            raise StopIteration(f"Invalid instruction: {self.currInstruction}")

    def symbol(self) -> str:
        if self.instType == 'L_INSTRUCTION':
            return self.currInstruction[1:-1]
        elif self.instType == 'A_INSTRUCTION':
            return str(self.currInstruction[1:])
        else:
            raise StopIteration('Not an A or L instruction')
    
    def dest(self) -> str:
        if self.instType != 'C_INSTRUCTION':
            raise StopIteration("Not a C instruction")
        # dest is the part before '='; if no '=', dest is empty
        if '=' in self.currInstruction:
            return self.currInstruction.split('=')[0]
        return ''

    def comp(self) -> str:
        if self.instType != 'C_INSTRUCTION':
            raise StopIteration("Not a C instruction")
        inst = self.currInstruction
        # strip off dest=
        if '=' in inst:
            inst = inst.split('=')[1]
        # strip off ;jump
        if ';' in inst:
            inst = inst.split(';')[0]
        return inst

    def jump(self) -> str:
        if self.instType != 'C_INSTRUCTION':
            raise StopIteration("Not a C instruction")
        # jump is the part after ';'; if no ';', jump is empty
        if ';' in self.currInstruction:
            return self.currInstruction.split(';')[1]
        return ''



