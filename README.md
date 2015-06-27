# battleship

To run this program, run the 'main.py' python file.

### Gameplay
This is a text-based battleship game. You may use the following commands:
- `s *name length x-coord y-coord isHorizontal*`: Adds a ship with the given name and length at the given x- and y-coordinates. If isHorizontal is True, will set the orientation of the ship to be horizontal. 
- `g *x-coord y-coord*`: Makes a guess on the opponent's (computer's) board at the given x- and y-coordinates.

**The following restrictions apply:**
- You may only place 5 ships on your board. There must be one 5-length ship, one 4-length ship, two 3-length ships, and one 2-length ship.
- You may not place ships diagonally or overlapping with other ships.
- You may only make guesses within the bounds of the board (values 0-9).
 
