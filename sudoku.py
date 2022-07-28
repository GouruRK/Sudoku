"""
Inspirated by http://norvig.com/sudoku.html
"""

from coordinates import *


class Sudoku:
    def __init__(self, grid):
        self.grid = grid.copy()

    def __str__(self):
        ch = ""
        for x in range(9):
            if x != 0 and x % 3 == 0:
                ch += "- - - + - - - + - - -\n"
            for y in range(9):
                if y != 0 and y % 3 == 0:
                    ch += "| "
                if self.grid[grid_reference[x][y]] == "0":
                    ch += ". "
                else:
                    ch += f"{self.grid[grid_reference[x][y]]} "
            if x != 8:
                ch += "\n"
        return ch

    def get_line(self, cell, remove=False):
        return self.coords_to_value(get_line(cell, remove))

    def get_column(self, cell, remove=False):
        return self.coords_to_value(get_column(cell, remove))

    def get_square(self, cell, remove=False):
        return self.coords_to_value(get_square(cell, remove))

    def get_peers(self, cell, remove=False):
        return self.coords_to_value(get_peers(cell, remove))

    def coords_to_value(self, coords):
        return {self.grid[coord] for coord in coords}

    def is_complete(self):
        for i in range(9):
            cell = letters[i] + digits[i]
            values = self.get_peers(cell)
            if len(values) != 9 or "0" in values:
                return False
        return True

    def solve(self):
        solveur = Solveur(self.grid)
        for cell in coords:
            if self.grid[cell] != "0":
                solveur.assign(cell, self.grid[cell])
        if not solveur.is_solved():
            solveur.backtrack()
        self.grid = solveur.solved.copy()

    def is_solved(self):
        ref = {digit for digit in digits}
        for cell in coords:
            functions = {get_column, get_line, get_square, get_peers}
            for f in functions:
                if self.coords_to_value(f(cell)) != ref:
                    return False, cell, self.coords_to_value(f(cell))
        return True


class Solveur:
    """
    Solveur inspirated by https://github.com/Julien00859
    """
    def __init__(self, grid):
        self.grid = grid.copy()
        self.solved = {cell: "123456789" for cell in coords}

    def is_solved(self):
        for cell in self.solved:
            if len(self.solved[cell]) != 1:
                return False
        return True

    def coord_to_value(self, coords):
        return {self.grid[coord] for coord in coords}

    def assign(self, cell, value):
        other_possibilities = self.solved[cell].replace(value, "")
        for v in other_possibilities:
            self.eliminate(cell, v)

    def eliminate(self, cell, value):
        if value not in self.solved[cell]:
            raise ValueError
        if len(self.solved[cell]) != 1:
            self.solved[cell] = self.solved[cell].replace(value, "")
            peers = get_peers(cell, remove=True)
            if len(self.solved[cell]) == 1:
                for peer in peers:
                    if self.solved[cell] in self.solved[peer]:
                        self.eliminate(peer, self.solved[cell])
            peer = [peer for peer in peers if value in self.solved[peer]]
            if len(peer) == 0:
                raise ValueError
            if len(peer) == 1:
                self.assign(peer[0], value)
        else:
            raise ValueError

    def backtrack(self):
        uncomplete_cells = [cell for cell in coords if len(self.solved[cell]) != 1]
        cells_by_lenght = sorted(
            uncomplete_cells, key=lambda cell: len(self.solved[cell])
        )
        cell = cells_by_lenght[0]
        keep = self.solved.copy()
        for digit in self.solved[cell]:
            try:
                self.assign(cell, digit)
                if self.is_solved():
                    return True
                return self.backtrack()
            except ValueError:
                self.solved = keep
        raise ValueError


def parse_args():
    import argparse

    parser = argparse.ArgumentParser(description="Sudoku")
    parser.add_argument("map")
    return vars(parser.parse_args())


def tab_to_dict(tab):
    grid = {}
    line_number = 0
    for line in tab:
        column_number = 0
        for cell in line:
            cell_name = grid_reference[line_number][column_number]
            grid[f"{cell_name}"] = cell
            column_number += 1
        line_number += 1
    return grid


def parser(map):
    tab = []
    if map[-4:] == ".txt":
        with open(map) as file:
            for line in file:
                line = line.rstrip()
                if len(line) == 9:
                    tab.append(["0" if line[i] == "." else  line[i] for i in range(9)])
                else:
                    tab.append(["0" if cell == "." else cell for cell in line.split()])
    elif len(map) == 81:
        temp = []
        for i in range(81):
            if i % 9 == 0:
                if temp != []:
                    tab.append(temp)
                    temp = []
            temp.append(map[i])
        tab.append(temp)
    return tab_to_dict(tab)


def main():
    from time import time

    args = parse_args()
    grid = parser(args["map"])
    game = Sudoku(grid)
    print(game)
    print("-" * 21)
    d = time()
    game.solve()
    f = time()
    print(game)
    print(game.is_solved(), f - d)


if __name__ == "__main__":
    main()
