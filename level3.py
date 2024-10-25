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
    # lines = inp.strip().splitlines()
    lines = inp.strip().splitlines()
    num = int(lines[0].strip())

    input = []
    for line in lines[1:]:
        s = line.strip().split(" ")
        print(line, s)
        input.append([int(s[0]), int(s[1]), int(s[2])])

    output = []
    id = 1
    for room in input:
        room_output = []
        rest_x = room[0] % 3
        rest_y = room[1] // 3

        for j in range (room[1]):
            line = []
            for k in range (room[0]//3):
                line.append(str(id))
                line.append(str(id))
                line.append(str(id))
                id += 1
            room_output.append(line)

        for j in range(rest_x):
            for i in range(room[1] // 3):
                room_output[i * 3].append(str(id))
                room_output[i * 3 + 1].append(str(id))
                room_output[i * 3 + 2].append(str(id))
                id += 1

        for line in range(len(room_output)):
            while len(room_output[line]) < room[0]:
                room_output[line].append("0")

        id = 1
        output.append(room_output)


    o = ""
    for line in output:
        for lineline in line:
            for linelineline in lineline:
                o += str(linelineline) + " "

            o += "\n"
        o += "\n"

    return o

m = Manager()
m.load_folder(path=Path("level3"))
m.apply_to_all(func=process_input)
