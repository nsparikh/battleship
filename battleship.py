import random

# Represents a ship object on the board
class Ship:
	def __init__(self, name, length, isHorizontal):
		self.name = name
		self.length = length

		# True if the ship is horizontally oriented
		self.isHorizontal = isHorizontal 

		# Coordinates are only set when the ship is placed successfully
		self.x = None # Leftmost x-coordinate
		self.y = None # Topmost y-coordinate

		# True if the ship has been sunk
		self.isSunk = False 

# Represents one square of the board
class GridSquare:
	def __init__(self, x, y):
		self.x = x
		self.y = y

		# Holds a reference to the Ship object occupying this square, if any
		self.ship = None 

		# True if the opponent has guessed this square
		self.isGuessed = False 

# Represents the board
class Grid:
	# If addRandomShips is True, randomly places 5 ships on the board
	def __init__(self, addRandomShips = False):
		self.w = 10 # Default width of 10
		self.h = 10 # Default height of 10

		# Initialize an empty wxh grid array and empty ships array
		self.grid_array = [[GridSquare(x, y) for x in range(self.w)] for y in range(self.h)]
		self.ships = []

		# Randomly place the ships
		if addRandomShips:
			self.add_ship(Ship('Aircraft Carrier', 5, False), 0, 0)
			self.add_ship(Ship('Battleship', 4, False), 1, 0)
			self.add_ship(Ship('Submarine', 3, False), 2, 0)
			self.add_ship(Ship('Cruiser', 3, False), 3, 0)
			self.add_ship(Ship('Destroyer', 2, False), 4, 0)
			# TODO: actually make this random

	# Adds the given ship to the grid at the given coordinates
	# Returns True if successful, False if invalid placement
	def add_ship(self, ship, x, y):
		# TODO: add restrictions on how many ships of each size can be placed

		# First check to see if this is in bounds of the grid
		if (x < 0 or (ship.isHorizontal and (x + ship.length) >= self.w)
			or y < 0 or (not ship.isHorizontal and (y + ship.length) >= self.h)):
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
			self.ships.append(ship)
			if ship.isHorizontal:
				x += 1
			else:
				y += 1
		return True

	# Makes a guess at the given coordinates and updates the board
	# Returns the response message
	def make_guess(self, x, y):
		# First check if the guess in in bounds
		if x < 0 or x >= self.w or y < 0 or y >= self.h:
			return 'Out of bounds.'

		gs = self.grid_array[x][y]

		# Next check if the square has already been guessed
		if gs.isGuessed:
			return 'Already guessed.'

		# Make the guess
		gs.isGuessed = True
		if gs.ship is None:
			return 'Miss!'
		else:
			if self.check_sunk(gs.ship):
				# Check to see if all ships have been sunk
				for ship in self.ships:
					if not self.check_sunk(ship):
						return 'Hit and sink! You sunk the ' + gs.ship.name
				return 'Hit and sink! You sunk all the ships -- you win!'
			else:
				return 'Hit!'

	# Checks if the given ship is fully sunk (i.e. all of its coordinates
	# have been hit)
	# This method does NOT modify the grid or the ship object
	def check_sunk(self, ship):
		curX = ship.x
		curY = ship.y
		if curX is None or curY is None:
			return False

		for i in range(ship.length):
			if not self.grid_array[curX][curY].isGuessed:
				return False
			if ship.isHorizontal:
				curX += 1
			else:
				curY += 1

		return True

	# Prints out the grid in a human readable format
	# Represents empty squares with '_', hit squares with 'X', 
	# missed squares with 'O', and ships with 's' if they can be seen
	def print_grid(self, canSeeShips):
		for y in range(self.h):
			row = ''
			for x in range(self.w):
				gs = self.grid_array[x][y]
				gs_string = ''
				if gs.ship != None and canSeeShips: 
					gs_string += 's'
				if gs.ship != None and gs.isGuessed:
					gs_string += 'X'
				elif gs.isGuessed: 
					gs_string += 'O'
				if len(gs_string) == 0:
					gs_string += '_'
				row += gs_string + ' '
			print row

