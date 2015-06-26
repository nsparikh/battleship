
// Initializes a ship with the given length and orientation
function Ship(name, length, isHorizontal) {
	this.name = name;
	this.length = length;
	this.isHorizontal = isHorizontal; 
	this.sunk = false; // True when the opponent sinks this ship
}

// Initializes an empty grid square at the given location
function GridSquare(x, y) {
	this.x = x;
	this.y = y;
	this.containsShip = false; // True if there is a ship in this square
	this.isHit = false; // True if the opponent has 'guessed' this square
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

// Prints out a representation of the grid in a readable format
Grid.prototype.printGrid = function() {
	for (var j = 0; j < this.h; j++) {
		var rowString = '';
		for (var i = 0; i < this.w; i++) {
			var gsString = ''
			if (this.gridArray[i][j].containsShip) gsString += 's';
			if (this.gridArray[i][j].isHit) gsString += 'X';

			if (gsString.length == 0) gsString = '_';
			rowString += gsString + ' ';
		}
		console.log(rowString);
	}
	console.log('\n');
}

// Adds a boat at the specified location with the given orientation
Grid.prototype.addShip = function(ship, x, y) {
	// TODO: make sure that this is 'legal' placement (not off the edges
	// and not conflicting with other ships)
	
	// Update the appropriate elements in the grid array
	for (var i = 0; i < ship.length; i++) {
		this.gridArray[x][y].containsShip = true;
		if (ship.isHorizontal) x += 1;
		else y += 1;
	}
	return true;
}

var grid = new Grid();
grid.printGrid();

