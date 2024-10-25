#!/usr/bin/env python3

from input_manager.manager import Manager
from pathlib import Path

class RoomInfo:
    len_x: int
    len_y: int
    max_desks: int

    def __init__(self, len_x, len_y, max_desks):
        self.len_x = len_x
        self.len_y = len_y
        self.max_desks = max_desks


class Room:
    cells: list[list[bool]]

    def __init__(self, len_x, len_y):
        self.cells = [[False for _ in range(len_y)] for _ in range(len_x)]

        # Put stripes
        for i in range(0, len_x, 2):
            for j in range(0, len_y):
                self.cells[i][j] = True

        # break strips
        for i in range(2, len_y, 3):
            for j in range(0, len_x):
                self.cells[j][i] = False

        # Ende korrekt abschneiden
        for i in range(0, len_x):
            if len_y % 3 < 2:
                for j in range(len_y - (len_y % 3), len_y):
                    self.cells[i][j] = False

        # Verikalle einzetzten
        if self.cells[0][-1] == False and self.cells[0][-2] == False:
            for i in range (len_x):
               self.cells[i][-1] = True
            for i in range (2, len_x, 3):
                self.cells[i][-1] = False
            if len_x % 3 < 2:
                for i in range(len_x - (len_x % 3), len_x):
                    self.cells[i][-1] = False

    def __cell_to_str__(self, s: bool) -> str:
        if not s:
            return "."
        else:
            return "X"

    def toString(self) -> str:
        output = ""
        for i in self.cells:
            for j in i:
                output += self.__cell_to_str__(j)
            output += "\n"
        output += "\n"
        return output

    pass

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

    rooms = []
    # Read the input file and output a list of RoomInfos
    for line in lines[1:]:
        s = line.strip().split(" ")
        print(line, s)
        rooms.append(
            RoomInfo(int(s[1]), int(s[0]), int(s[2]))
        )

    output_rooms = ""
    for room in rooms:
        output_rooms += handle_room(room).toString() + "\n"

    return output_rooms

def handle_room(room_info: RoomInfo) -> Room:
    return Room(room_info.len_x, room_info.len_y)

m = Manager()
m.load_folder(path=Path("level4"))
m.apply_to_all(func=process_input)
