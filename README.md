# Sudoku

A python sudoku solveur

## How to use

```bash
# Clone this repository
git clone https://github.com/GouruRK/Sudoku.git

# Go into the repository
cd Sudoku

# Launch the programm
python3 sudoku.py <grid>
```

The `grid` argument can be a path to a file containing a grid, or direclty the grid

### Examples

Grid in argument :
```bash
python3 sudoku.py '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'

python3 sudoku.py '004020006700000500020700000050000032003094600080010000305900000090000043000073200'
```

Grid in file :

```bash
python3 sudoku.py grids/grid1.txt
```

___

Based on https://norvig.com/sudoku.html