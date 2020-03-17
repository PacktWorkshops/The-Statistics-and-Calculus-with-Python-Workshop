import unittest
import import_ipynb
import numpy as np

class Test(unittest.TestCase):
	def setUp(self):
		import exercise_8_1
		self.exercise = exercise_8_1

	def test_cards(self):
		cards = self.exercise.cards
		self.assertEqual(52, len(cards))

	def test_deal_hands(self):
		deal_hands = self.exercise.deal_hands
		result_1 = deal_hands()
		self.assertEqual(2,len(result_1))
		self.assertEqual(5, len(result_1[0]))
		
if __name__ == '__main__':
	unittest.main()
	