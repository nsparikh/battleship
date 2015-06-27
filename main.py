from battleship import *
from battleship_ai import *

# Runs the game play
# User can input the following commands:
# 	Make a guess at (X,Y): g X Y
# 	Add a ship of length L at (X,Y): s name L X Y isHorizontal
# 	Help: h
# 	Quit: q
def run():
	player_grid = Grid()
	opponent_grid = Grid(True)
	opponent = RandomGuesser()
	
	# Listen for user input
	# Parse command and execute the appropriate actions if valid
	while True:
		user_input = raw_input('Enter a command (h for Help): ').split(' ')

		# User has entered a quit command, so end the game
		if user_input[0] == 'q':
			print 'Goodbye!'
			break

		# User enters an 'add ship' command
		elif user_input[0] == 's':
			if player_grid.check_if_ready():
				print 'Already added all 5 ships. Make a guess against your opponent!'
				continue
			try:
				name = user_input[1]
				length = int(user_input[2])
				x = int(user_input[3])
				y = int(user_input[4])
				isHorizontal = bool(user_input[5])
				if player_grid.add_ship(Ship(name, length, isHorizontal), x, y):
					player_grid.print_grid(True)
					print 'Ship added: ' + name + '\n'
				else:
					print 'Invalid ship placement.'
			except:
				print 'Invalid input. Please try again.'

		# User enters a 'make guess' command
		elif user_input[0] == 'g':
			if not player_grid.check_if_ready():
				print 'You must finish placing 5 ships on your board before making a guess.'
				continue
			try:
				x = int(user_input[1])
				y = int(user_input[2])
				response_string = opponent_grid.make_guess(x, y)
				opponent_grid.print_grid(False)
				print response_string + '\n'

				# If player has won, reset the game grids
				if 'win' in response_string:
					restart_input = raw_input('Play again? (y / n): ')
					if restart_input == 'y':
						player_grid = Grid()
						opponent_grid = Grid(True)
					else:
						print 'Goodbye!'
						break

				# Have the computer make a random guess
				(opp_x, opp_y) = opponent.next_guess()
				opponent_response = player_grid.make_guess(opp_x, opp_y)

				# TODO: find a cleaner way of doing this without the response string...
				while 'Already' in opponent_response:
					(opp_x, opp_y) = opponent.next_guess()
					opponent_response = player_grid.make_guess(opp_x, opp_y)
				print 'OPPONENT GUESS: '
				player_grid.print_grid(True)
				print '\n'

			except:
				print 'Invalid input. Please try again.'

		# User enters a 'help' command
		elif user_input[0] == 'h':
			print 'You may enter one of the following commands:'
			print 'q: Quit'
			print ('s name length X Y isHorizontal: ' +
				'add ship with name and length L at (X, Y) with horizontal orientation' +
				'if isHorizontal is True. Name must be one word.')
			print 'g X Y: make a guess at (X, Y)'

		# Invalid input
		else:
			print 'Invalid input. Please try again.'

run()