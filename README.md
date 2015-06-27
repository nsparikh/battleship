# Battleship

To run this program, run the 'main.py' python file.

### Gameplay
This is a text-based battleship game. You may use the following commands:
- `s name length x-coord y-coord is_horizontal`: Adds a ship with the given name and length at the given x- and y-coordinates. If is_horizontal is True, will set the orientation of the ship to be horizontal. 
- `g x-coord y-coord`: Makes a guess on the opponent's (computer's) board at the given x- and y-coordinates.
- `q`: Quits the game.
- `h`: Displays the help text.

**The following restrictions apply:**
- You may only place 5 ships on your board. There must be one 5-length ship, one 4-length ship, two 3-length ships, and one 2-length ship.
- You may not place ships diagonally or overlapping with other ships.
- You may only make guesses within the bounds of the board (values 0-9).

#### Board Format
The board representation is printed out as follows:
- `X`: A 'hit' square (there is a ship occupying the space, and it has been guessed)
- `O`: A 'miss' square (there is nothing occupying the space, but it has been guessed)
- `_`: A unguessed square
- `*`: An unguessed square that has a ship occupying the space. This is only displayed on your own board (e.g. you cannot see the unguessed ship locations on your opponent's board)

### AI
I've begun to implement a basic Naive Bayes Classifier; however, this is still a work in progress and currently not fully functional. 
 
