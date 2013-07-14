from rps_oop import Rock, Paper, Scissors
import unittest

class RPSRelationCase(unittest.TestCase):
    def runTest(self):
        self.assertEqual(Rock.weaker_than, Paper)
        self.assertEqual(Rock.stronger_than, Scissors)
        self.assertEqual(Paper.weaker_than, Scissors)
        self.assertEqual(Paper.stronger_than, Rock)
        self.assertEqual(Scissors.weaker_than, Rock)
        self.assertEqual(Scissors.stronger_than, Paper)

if __name__ == "__main__":
    unittest.main()
