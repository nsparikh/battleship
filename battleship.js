var invalidGuess = 'Invalid guess';
var alreadyGuessed = 'Already guessed';
var hitShip = 'You hit a ship: ';
var hitAndSunk = 'You hit and sunk a ship: ';
var miss = 'You missed :(';

// Initializes a ship with the given length and orientation
function Ship(name, length, isHorizontal) {
	this.name = name;
	this.length = length;
	this.isHorizontal = isHorizontal; 
	this.isSunk = false; // True when the opponent sinks this ship

	// The leftmost and topmost coordinates of this ship
	// These values are only set when the ship is successfully placed on the grid
	this.x = null; // Leftmost x-coordinate of this ship
	this.y = null; // Topmost y-coordinate of this ship
}

// Initializes an empty grid square at the given location
function GridSquare(x, y) {
	this.x = x;
	this.y = y;
	this.ship = null; // True if there is a ship in this square
	this.isGuessed = false; // True if the opponent has 'guessed' this square
}

// Initializes an empty grid of GridSquare objects
// Position (0, 0) is the top left corner of the grid
function Grid() {
	this.w = 10; // Grid width
	this.h = 10; // Grid height

	this.gridArray = [[]];
	for (var x = 0; x < this.w; x++) {
		this.gridArray[x] = [];
		for (var y = 0; y < this.h; y++) {
			var gs = new GridSquare(x, y);
			this.gridArray[x][y] = gs;
		}
	}
}

// Prints out a representation of the grid to the console in a readable format
Grid.prototype.printGrid = function() {
	for (var j = 0; j < this.h; j++) {
		var rowString = j + ': ';
		for (var i = 0; i < this.w; i++) {
			var gsString = ''
			if (this.gridArray[i][j].ship != null) gsString += 's';
			if (this.gridArray[i][j].isGuessed) gsString += 'X';

			if (gsString.length == 0) gsString = '_';
			rowString += gsString + ' ';
		}
		console.log(rowString);
	}
	console.log('\n');
}

// Adds a boat at the specified location with the given orientation
// Returns false if the ship is trying to be placed in an invalid location
// Returns true if the ship was successfully placed
Grid.prototype.addShip = function(ship, x, y) {
	// Make sure that this is 'legal' placement (not off the edges
	// and not conflicting with other ships)
	if (x < 0 || (ship.isHorizontal && (x+ship.length) >= this.w) || 
		y < 0 || (!ship.isHorizontal && (y+ship.length) >= this.h)) {
		return false;
	}

	var curX = x;
	var curY = y;
	for (var i = 0; i < ship.length; i++) {
		if (this.gridArray[curX][curY].ship != null) return false;
		if (ship.isHorizontal) curX += 1;
		else curY += 1;
	}
	
	// Update the appropriate elements in the grid array
	for (var i = 0; i < ship.length; i++) {
		// Set the ship coordinates if necessary
		if (ship.x == null) ship.x = x;
		if (ship.y == null) ship.y = y;

		// Mark the coordinates in the grid array as containing this ship
		this.gridArray[x][y].ship = ship;
		if (ship.isHorizontal) x += 1;
		else y += 1;
	}
	return true;
}

// Helper method to check if the given ship is sunk 
// (i.e. if all of the ship's coordinates have been guessed)
// This method does NOT make any modifications to the grid or ship
// and assumes that the ship has been placed at a valid location
Grid.prototype.checkIfSunk = function(ship) {
	if (ship.x == null || ship.y == null) return false;

	var curX = ship.x;
	var curY = ship.y;
	for (var i = 0; i < ship.length; i++) {
		if (!this.gridArray[curX][curY].isGuessed) return false;
		if (ship.isHorizontal) curX += 1;
		else curY += 1;
	}
	return true;
}

// Makes a guess at the specified location in the grid
// Returns a message to the player
Grid.prototype.makeGuess = function(x, y) {
	// Make sure this is a legal guess
	if (x < 0 || x >= this.w || y < 0 || y >= this.h) return invalidGuess;
	if (this.gridArray[x][y].isGuessed) return alreadyGuessed;

	// First mark this square as guessed
	this.gridArray[x][y].isGuessed = true;

	// Check to see if a ship has been hit
	if (this.gridArray[x][y].ship != null) {
		var ship = this.gridArray[x][y].ship;
		// Check to see if a ship has been sunk
		if (this.checkIfSunk(ship)) return hitAndSunk + ship.name;
		else return hitShip + ship.name;
	} else {
		return miss;
	}
}

var grid = new Grid();
var ship5 = new Ship('5-length', 5, true);
grid.addShip(ship5, 2, 3);
grid.printGrid();
console.log(grid.makeGuess(0, 0));
grid.printGrid();
console.log(grid.makeGuess(2, 3));
grid.printGrid();

