'''
Ship
- Fields:
	- x: int
	- y: int
	- isHorizontal: bool
	- isSunk: bool
- Methods

Grid
- Fields:
	- grid_array: 2D array of GridSquares
	- ships: list of Ships (?)
- Methods:
	- add_ship(ship, x, y)
	- make_guess(x, y)
	- check_sunk(ship)

GridSquare
- Fields:
	- x: int
	- y: int
	- ship: Ship object
	- isGuessed: bool

'''