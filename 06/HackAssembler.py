import sys
import os
from Parser import Parser
from Code import Code


def main():
    if len(sys.argv) != 2:
        print("Usage: python HackAssembler.py Prog.asm")
        sys.exit(1)
    input_path = sys.argv[1]
    base, _ = os.path.splitext(input_path)
    output_path = base + ".hack"

    # First pass: build symbol table from label (L) instructions
    parser = Parser(input_path)
    symbol_table = {}
    rom_address = 0
    while parser.hasMoreLines():
        parser.advance()
        parser.instructionType()
        if parser.instType == 'L_INSTRUCTION':
            label = parser.symbol()
            if label not in symbol_table:
                symbol_table[label] = rom_address
        else:
            rom_address += 1

    # Second pass: translate instructions
    parser = Parser(input_path)
    code = Code()
    with open(output_path, 'w', newline='\n') as fout:
        while parser.hasMoreLines():
            parser.advance()
            parser.instructionType()
            if parser.instType == 'A_INSTRUCTION':
                symbol = parser.symbol()
                if symbol.isdigit():
                    address = int(symbol)
                else:
                    if symbol not in symbol_table:
                        raise ValueError(f"Undefined symbol: {symbol}")
                    address = symbol_table[symbol]
                fout.write(format(address, '016b') + '\n')
            elif parser.instType == 'C_INSTRUCTION':
                comp_bits = code.comp(parser.comp())
                dest_bits = code.dest(parser.dest())
                jump_bits = code.jump(parser.jump())
                fout.write('111' + comp_bits + dest_bits + jump_bits + '\n')


if __name__ == '__main__':
    main()