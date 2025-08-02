class Code:
    # dest mnemonics map to d1d2d3
    DEST_TABLE = {
        "":    "000",
        "M":   "001",
        "D":   "010",
        "MD":  "011",
        "A":   "100",
        "AM":  "101",
        "AD":  "110",
        "AMD": "111",
    }

    # comp mnemonics map to a c1c2c3c4c5c6
    COMP_TABLE = {
        # a=0
        "0":   "0101010",
        "1":   "0111111",
        "-1":  "0111010",
        "D":   "0001100",
        "A":   "0110000",
        "!D":  "0001101",
        "!A":  "0110001",
        "-D":  "0001111",
        "-A":  "0110011",
        "D+1": "0011111",
        "A+1": "0110111",
        "D-1": "0001110",
        "A-1": "0110010",
        "D+A": "0000010",
        "D-A": "0010011",
        "A-D": "0000111",
        "D&A": "0000000",
        "D|A": "0010101",
        # a=1 (M instead of A)
        "M":   "1110000",
        "!M":  "1110001",
        "-M":  "1110011",
        "M+1": "1110111",
        "M-1": "1110010",
        "D+M": "1000010",
        "D-M": "1010011",
        "M-D": "1000111",
        "D&M": "1000000",
        "D|M": "1010101",
    }

    # jump mnemonics map to j1j2j3
    JUMP_TABLE = {
        "":    "000",
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE": "101",
        "JLE": "110",
        "JMP": "111",
    }

    def dest(self, mnemonic: str) -> str:
        """Returns the 3-bit binary code for the dest field."""
        try:
            return self.DEST_TABLE[mnemonic]
        except KeyError:
            raise ValueError(f"Invalid dest mnemonic: '{mnemonic}'")

    def comp(self, mnemonic: str) -> str:
        """Returns the 7-bit binary code for the comp field."""
        try:
            return self.COMP_TABLE[mnemonic]
        except KeyError:
            raise ValueError(f"Invalid comp mnemonic: '{mnemonic}'")

    def jump(self, mnemonic: str) -> str:
        """Returns the 3-bit binary code for the jump field."""
        try:
            return self.JUMP_TABLE[mnemonic]
        except KeyError:
            raise ValueError(f"Invalid jump mnemonic: '{mnemonic}'")