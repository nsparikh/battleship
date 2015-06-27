import random

# Makes random guesses on the board
class RandomGuesser:
	# Returns a tuple of the next guess coordinates
	def next_guess(self):
		return (random.randint(0, 9), random.randint(0, 9))

# Makes guesses based on a probability density function estimate of the board
class PdfGuesser:
	def __init__(self):
		self.heatmap = [[]]

	# Returns a tuple of the next guess coordinates
	def next_guess(self):
		pass