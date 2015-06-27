from battleship import *

# Runs the game play
# User can input the following commands:
# 	Make a guess at (X,Y): g X Y
# 	Add a ship of length L at (X,Y): s name L X Y isHorizontal
# 	Help: h
# 	Quit: q
def run():
	player_grid = Grid()
	opponent_grid = Grid(True)
	
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
			try:
				x = int(user_input[1])
				y = int(user_input[2])
				response_string = opponent_grid.make_guess(x, y)
				opponent_grid.print_grid(False)
				print response_string + '\n'
				if 'win' in response_string:
					restart_input = raw_input('Play again? (y / n): ')
					if restart_input == 'y':
						player_grid = Grid()
						opponent_grid = Grid(True)
					else:
						print 'Goodbye!'
						break
				# TODO: handle WIN case here
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