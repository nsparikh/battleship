import random
import numpy as np
from sklearn.naive_bayes import GaussianNB
from battleship import *

# Makes random guesses on the board
class RandomGuesser:
	# Returns a tuple of the next guess coordinates
	def next_guess(self):
		return (random.randint(0, 9), random.randint(0, 9))

# Models this as a classification problem
# Assigns each unguessed square with a probability value that it contains a ship
# Then selects the square with the maximal value
class NaiveBayesGuesser:
	def __init__(self, grid):
		self.grid = grid

		# Train the classifier on 10 randomly generated boards
		all_features = []
		all_labels = []
		for i in range(2):
			(features, labels) = create_training_data()
			all_features += features
			all_labels += labels
		np_features = np.array(all_features)
		np_labels = np.array(all_labels)

		self.classifier = GaussianNB().fit(np_features, np_labels)

	def next_guess(self):
		# Determine a prediction for every unguessed square in the grid
		predictions = [[0.0 for x in range(self.grid.w)] for y in range(self.grid.h)]
		for x in range(self.grid.w):
			for y in range(self.grid.h):
				feature_vector = []
				for (n_x, n_y) in get_neighbors(x, y):
					if not in_bounds(n_x, n_y):
						feature_vector.append(-1000)
						continue
					n = self.grid.grid_array[n_x][n_y]
					if n.isGuessed and n.ship is None:
						feature_vector.append(0.0) # Known miss
					elif n.isGuessed:
						feature_vector.append(1.0) # Known hit
					else:
						feature_vector.append(0.5) # Unguessed square
				predictions[x][y] = self.classifier.predict(feature_vector)

		# Select the square with the highest value
		max_x = 0
		max_y = 0
		max_val = 0.0
		for x in range(self.grid.w):
			for y in range(self.grid.h):
				if (predictions[x][y][0] > max_val and not
					self.grid.grid_array[x][y].isGuessed):
					max_x = x
					max_y = y
					max_val = predictions[x][y][0]
		return (max_x, max_y)

# Creates a set of labeled training data that can be used to train the classifiers
# Feature vectors length-8 vectors that represent the state of the current square's neighbors
# A value of 0=False (known miss), 1=True (known hit), 0.5=Unknown (unguessed)
# We will represent out-of-bounds squares with -1000
# The labels will be values of 0 (no ship) or 1 (has ship)
def create_training_data():
	grid = Grid(True)

	features = []
	labels = []

	for x in range(grid.w):
		for y in range(grid.h):
			feature_vector = []
			for (n_x, n_y) in get_neighbors(x, y):
				if not in_bounds(n_x, n_y):
					feature_vector.append(-1000)
				elif grid.grid_array[n_x][n_y].ship != None:
					feature_vector.append(1.0)
				else:
					feature_vector.append(0.0)
			features.append(feature_vector)
			labels.append(0.0 if grid.grid_array[x][y].ship == None else 1.0)

	# Return a tuple of the feature vectors and associated labels
	return (features, labels)


# Returns a list of neighboring square coordinates as tuples
# This list includes out-of-bounds coordinates
# Order traverses down each column starting in the top left corner
def get_neighbors(x, y):
	return ([(x2, y2) for x2 in range(x-1, x+2) 
		for y2 in range(y-1, y+2) 
		if (x != x2 or y != y2)])

# Returns True if the given coordinates are in bounds, False if not
def in_bounds(x, y):
	return (0 <= x < 10 and 0 <= y < 10)

