class Ship:
	def __init__(self, x, y, isHorizontal):
		self.x = x # Leftmost x-coordinate
		self.y = y # Topmost y-coordinate

		# True if the ship is horizontally oriented
		self.isHorizontal = isHorizontal 

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
		pass

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
				if gs.ship != None and canSeeShips: 
					row += 's'
				if gs.isGuessed: 
					row += 'X'
				if gs.ship == None and not gs.isGuessed:
					row += '_'
				row += ' '
			print row
