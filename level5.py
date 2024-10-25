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

        if len_x % 2 == 0 and len_y % 2 == 0:
            self.rechne_mit_grade_seiten(0, 0, len_x, len_y)
        elif ((len_x % 2 == 0 or len_y % 2 == 0) and len_x % 2 != len_y % 2):
            pass


    def rechne_mit_grade_seiten(self, skip_x: int, skip_y: int, len_x: int, len_y: int):

        if len_x - skip_x >= 4:
            for i in range(skip_x, len_x - skip_x - 3, 2):
                self.cells[i][0 + skip_y] = True
                self.cells[i][1 + skip_y] = True

        if len_y - skip_y >= 4:
            for i in range(skip_y, len_y - skip_y - 3, 2):
                self.cells[-1 - skip_x][i] = True
                self.cells[-2 - skip_x][i] = True

        if len_x - skip_x >= 6:
            for i in range(len_x - skip_x - 1, 2 + skip_x, -2):
                self.cells[i][-1 - skip_y] = True
                self.cells[i][-2 - skip_y] = True

        if len_y - skip_y >= 6:
            for i in range(len_y - skip_y - 1, 2 + skip_y, -2):
                self.cells[0 + skip_x][i] = True
                self.cells[1 + skip_x][i] = True

        if len_x - skip_y * 2 > 6 and len_y - skip_y * 2 > 6:
            self.rechne_mit_grade_seiten(skip_x + 3, skip_y + 3, len_x, len_y)

    """
    def rechne_mit_ungeraden_seiten(self, len_x: int, len_y: int):
        if len_x % 2 != 0:                              #check if x -> ungerade                  sonst gerade
                                                        # self.cells[y][x]
                                                        # True = X
            for i in range(len_y):
                
                
        
    """

    def __cell_to_str__(self, s: bool) -> str:
        if not s:
            return "."
        else:
            return "X"

    def toString(self) -> str:
        output = ""

        for i in range(len(self.cells[0])):
            for j in range(len(self.cells)):
                output += self.__cell_to_str__(self.cells[j][i])
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
m.load_folder(path=Path("level5"))
m.apply_to_all(func=process_input)
