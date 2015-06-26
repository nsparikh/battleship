class Ship:
	def __init__(self, length, isHorizontal):
		self.length = length

		# True if the ship is horizontally oriented
		self.isHorizontal = isHorizontal 

		# Coordinates are only set when the ship is placed successfully
		self.x = x # Leftmost x-coordinate
		self.y = y # Topmost y-coordinate

		# True if the ship has been sunk
		self.isSunk = False 

class GridSquare:
	def __init__(self, x, y):
		self.x = x
		self.y = y

		# Holds a reference to the Ship object occupying this square, if any
		self.ship = None 

		# True if the opponent has guessed this square
		self.isGuessed = False 

class Grid:
	def __init__(self):
		self.w = 10 # Default width of 10
		self.h = 10 # Default height of 10

		# Initialize an empty wxh grid array and empty ships array
		self.grid_array = [[GridSquare(x, y) for x in range(self.w)] for y in range(self.h)]
		self.ships = []

	# Adds the given ship to the grid at the given coordinates
	# Returns True if successful, False if invalid placement
	def add_ship(self, ship, x, y):
		# First check to see if this is in bounds of the grid
		if (x < 0 or (ship.isHorizontal and (x + ship.length) >= self.w)
			or y < 0 or (!ship.isHorizontal and (y + ship.length) >= self.h):
			return False

		# Next check to see if this will overlap with any other ships
		curX = x
		curY = y
		for i in range(ship.length):
			if self.grid_array[curX][curY].ship is not None: 
				return False
			if ship.isHorizontal: 
				curX += 1
			else: 
				curY += 1

		# Add the ship to the grid
		ship.x = x
		ship.y = y
		for i in range(ship.length):
			self.grid_array[x][y].ship = ship
			if ship.isHorizontal:
				x += 1
			else:
				y += 1

	# Makes a guess at the given coordinates
	# Returns True if it hits a ship, False if the guess is a miss
	def make_guess(self, x, y):
		pass

	# Checks if the given ship is fully sunk (i.e. all of its coordinates
	# have been hit)
	# This method does NOT modify the grid or the ship object
	def check_sunk(self, ship):
		pass

	# Prints out the grid in a human readable format
	# Represents empty squares with '_', hit squares with 'X', and ships with 's'
	def print_grid(self, canSeeShips):
		for y in range(self.h):
			row = ''
			for x in range(self.w):
				gs = self.grid_array[x][y]
				gs_string = ''
				if gs.ship != None and canSeeShips: 
					gs_string += 's'
				if gs.isGuessed: 
					gs_string += 'X'
				if len(gs_string) == 0:
					gs_string += '_'
				row += gs_string + ' '
			print row
