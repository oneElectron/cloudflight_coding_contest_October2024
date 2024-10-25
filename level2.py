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
        input.append([int(s[0]), int(s[1]), int(s[2])])
    output = ""
    id = 1
    for i in input:
        for j in range(i[1]):
            for k in range(i[0]//3):
                output += (str(id) + " ") * 3
                id += 1
            output = output[:-1]
            output += "\n"
        output += "\n"
        id = 1

    o = ""
    for line in output.splitlines():
        for lineline in line:
            o += lineline.strip()
            o += "\n"

    return output


m = Manager()
m.load_folder(path=Path("level2"))
m.apply_to_all(func=process_input)
