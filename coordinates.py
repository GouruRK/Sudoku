digits = "123456789"
letters = "ABCDEFGHI"


def cross(A, B):
    return {a + b for a in A for b in B}


coords = cross(letters, digits)
lines_per_cell = {coord: cross(coord[0], digits) for coord in coords}
columns_per_cell = {coord: cross(letters, coord[1]) for coord in coords}
squares_per_cell = [
    cross(rs, cs) for rs in ("ABC", "DEF", "GHI") for cs in ("123", "456", "789")
]
squares_per_cell = {
    coord: [sq for sq in squares_per_cell if coord in sq][0] for coord in coords
}
grid_reference = [
    ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9"],
    ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"],
    ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"],
    ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9"],
    ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9"],
    ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"],
    ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9"],
    ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9"],
    ["I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9"],
]


def get_line(cell, remove=False):
    line = lines_per_cell[cell].copy()
    if remove:
        line.remove(cell)
    return line


def get_column(cell, remove=False):
    column = columns_per_cell[cell].copy()
    if remove:
        column.remove(cell)
    return column


def get_square(cell, remove=False):
    square = squares_per_cell[cell].copy()
    if remove:
        square.remove(cell)
    return square


def get_peers(cell, remove=False):
    line = get_line(cell, remove)
    column = get_column(cell, remove)
    square = get_square(cell, remove)
    return line | column | square
