import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSEMBLER_DIR = ROOT / "06"
sys.path.insert(0, str(ASSEMBLER_DIR))

from Code import Code  # noqa: E402
from Parser import Parser  # noqa: E402


def test_code_translates_c_instruction_fields():
    code = Code()

    assert code.comp("D+M") == "1000010"
    assert code.dest("AMD") == "111"
    assert code.jump("JGE") == "011"


def test_parser_skips_blank_lines_and_comments(tmp_path):
    source = tmp_path / "Loop.asm"
    source.write_text("// comment\n\n(LOOP)\n@2\nD=A\n", encoding="utf-8")
    parser = Parser(source)

    parsed = []
    while parser.hasMoreLines():
        parser.advance()
        parser.instructionType()
        parsed.append((parser.instType, parser.currInstruction))

    assert parsed == [
        ("L_INSTRUCTION", "(LOOP)"),
        ("A_INSTRUCTION", "@2"),
        ("C_INSTRUCTION", "D=A"),
    ]


def test_assembler_writes_expected_machine_code(tmp_path):
    source = tmp_path / "AddAndStop.asm"
    source.write_text(
        "@2\nD=A\n@3\nD=D+A\n@END\n0;JMP\n(END)\n@END\n0;JMP\n",
        encoding="utf-8",
    )

    subprocess.run(
        [sys.executable, str(ASSEMBLER_DIR / "HackAssembler.py"), str(source)],
        check=True,
        capture_output=True,
        text=True,
    )

    assert source.with_suffix(".hack").read_text(encoding="utf-8").splitlines() == [
        "0000000000000010",
        "1110110000010000",
        "0000000000000011",
        "1110000010010000",
        "0000000000000110",
        "1110101010000111",
        "0000000000000110",
        "1110101010000111",
    ]
