import json
from enum import Enum


class Opcode(str, Enum):
    ADD = "ADD"
    SUB = "SUB"
    MUL = "MUL"
    DIV = "DIV"
    MOV = "MOV"
    LOAD = "LOAD"
    STORE = "STORE"
    JUMP = "JUMP"
    JUMP_IF = "JUMP_IF"
    JUMP_IF_NOT = "JUMP_IF_NOT"
    CALL = "CALL"
    RET = "RET"
    CMP = "CMP"
    HALT = "HALT"

    def __str__(self) -> str:
        return str(self.value)


def write_code(filename: str, code: dict) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        buf = []
        for instr in code:
            buf.append(json.dumps(instr))
        f.write("[", ",\n".join(buf), "]")


def read_code(filename: str) -> dict:
    with open(filename, "r", encoding="utf-8") as f:
        code = json.loads(f.read())

    for instr in code:
        instr["opcode"] = Opcode(instr["opcode"])

        if "term" in instr:
            assert len(instr["term"]) == 3

    return code
