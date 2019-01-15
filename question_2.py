"""
We want a function which accepts a very large​ list of prices (pricesLst) and returns the
largest possible loss a client could have made with only a buy transaction followed by a sell
transaction. The largest loss is calculated as 

pricesLst[index2] - pricesLst[index1] where index1 < index2.

Please then write tests for this function to ensure it works as expected guarding against all edge
cases you can think of.
"""


from unittest import TestCase


def largest_possible_loss(pricesLst):
    if pricesLst:
        cleaned = [x for x in pricesLst if isinstance(x, int) | isinstance(x, float)]
        if cleaned:
            max_val = max(cleaned)
            min_val = min(cleaned)
            return max_val - min_val
    return 0


class TestLargestPossibleLoss(TestCase):
    
    def test_largest_possible_loss(self):
        pl_1 = [1, 2, 3, 4, 5]
        pl_2 = [5555, 2222, 1111, 4444, 3333]
        pl_3 = [55.55, 22.22, 11.11, 44.44, 33.33]
        pl_4 = ["55.55", 22.22, "11.11", 44.44, 33.33]
        pl_5 = []
        pl_6 = ["5", "2", "1", "4", "3"]
        pl_7 = [5]
        pl_8 = [8, 7.5]
        
        alpha = largest_possible_loss(pl_1)
        bravo = largest_possible_loss(pl_2)
        charlie = largest_possible_loss(pl_3)
        delta = largest_possible_loss(pl_4)
        echo = largest_possible_loss(pl_5)
        foxtrot = largest_possible_loss(pl_6)
        golf = largest_possible_loss(pl_7)
        hotel = largest_possible_loss(pl_8)

        self.assertEqual(alpha, 4)
        self.assertEqual(bravo, 4444)
        self.assertEqual(charlie, 44.44)
        self.assertEqual(delta, 22.22)
        self.assertEqual(echo, 0)
        self.assertEqual(foxtrot, 0)
        self.assertEqual(golf, 0)
        self.assertEqual(hotel, 0.5)

