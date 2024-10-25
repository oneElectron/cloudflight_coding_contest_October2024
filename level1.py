#!/usr/bin/env python3

from input_manager.manager import Manager
from pathlib import Path

def process_input(inp: str) -> str:
    """
    Processes the input and returns the output.

    Parameters
    ----------
    inp : str
        The entire input to be processed.

    Returns
    -------
    str
        The output.
    """
    lines = inp.strip().splitlines()
    num = int(lines[0].strip())

    input = []
    for line in lines[1:]:
        s = line.strip().split(" ")
        print(line, s)
        input.append([int(s[0]), int(s[1])])

    output = ""
    for i in input:
        output += str(int(i[0] * i[1] // 3))
        output += "\n"

    return output

m = Manager()
m.load_folder(path=Path("level1"))
m.apply_to_all(func=process_input)
