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
		# TODO: change this to use a better state representation

	# Returns a single-character representation of the square
	# Key:
	# 	O = missed
	# 	X = hit
	# 	_ = not guessed
	# 	* = contains ship (only visible if can_see_ships is True)
	def gs_string(self, can_see_ships):
		if self.isGuessed and self.ship is not None:
			return 'X'
		elif self.ship is not None and can_see_ships:
			return '*'
		elif self.isGuessed:
			return 'O'
		else:
			return '_'

# Represents the board
class Grid:
	# If addRandomShips is True, randomly places 5 ships on the board
	def __init__(self, add_random_ships = False):
		self.w = 10 # Default width of 10
		self.h = 10 # Default height of 10

		# Initialize an empty wxh grid array and empty ships array
		self.grid_array = [[GridSquare(x, y) for x in range(self.w)] for y in range(self.h)]
		self.ships = []

		# Randomly place the ships
		if add_random_ships:
			ships_to_add = [
				Ship('Aircraft Carrier', 5, False),
				Ship('Battleship', 4, True),
				Ship('Submarine', 3, False),
				Ship('Cruiser', 3, True),
				Ship('Destroyer', 2, False)
			]
			while len(ships_to_add) > 0:
				rand_x = random.randint(0, 9)
				rand_y = random.randint(0, 9)
				s = ships_to_add[0]
				if self.add_ship(s, rand_x, rand_y):
					ships_to_add.remove(s)

	# Checks if the board is 'ready', e.g. all 5 ships have been added
	def check_if_ready(self):
		return len(self.ships) == 5

	# Adds the given ship to the grid at the given coordinates
	# Returns True if successful, False if invalid placement
	def add_ship(self, ship, x, y):
		# First check to see if this is in bounds of the grid
		if (x < 0 or (ship.isHorizontal and (x + ship.length) >= self.w)
			or y < 0 or (not ship.isHorizontal and (y + ship.length) >= self.h)):
			return False

		# TODO: add a check here to make sure we can add a ship
		# of this length (i.e. can't have more than 2 length-3 ships)

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
		self.ships.append(ship)
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
	def print_grid(self, can_see_ships):
		for y in range(self.h):
			row = ''
			for x in range(self.w):
				row += self.grid_array[x][y].gs_string(can_see_ships) + ' '
			print row

