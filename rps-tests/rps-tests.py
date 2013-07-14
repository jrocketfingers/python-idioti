from rps_oop import Rock, Paper, Scissors, RollHandler, Player, AI
from rps_oop import InvalidRollOptionError, InvalidPlayerNameError
import rps_oop
import unittest
import random

class RPSRelationCase(unittest.TestCase):
    def runTest(self):
        """Test the relations between options."""

        self.assertEqual(Rock.weaker_than, Paper, "Rock is not weaker than Paper")
        self.assertEqual(Rock.stronger_than, Scissors, "Rock is not stronger than Scissors")
        self.assertEqual(Paper.weaker_than, Scissors, "Paper is not weaker than Scissors!")
        self.assertEqual(Paper.stronger_than, Rock, "Paper is not stronger than Rock")
        self.assertEqual(Scissors.weaker_than, Rock, "Scissors are not weaker than Rock")
        self.assertEqual(Scissors.stronger_than, Paper, "Scissors are not weaker than Paper")


class RPSAIRollCase(unittest.TestCase):
    def setUp(self):
        self.AI = AI('name')

    def testAIRandRange(self):
        """Test the roll options."""
        self.assertIn(self.AI.Roll(), [Rock, Paper, Scissors])

    def testAITweakedInput(self):
        """Test the out of range values for exceptions."""
        rps_oop.randint = lambda x,y: len(RollHandler.options)
        self.assertRaises(IndexError, self.AI.Roll)

        rps_oop.randint = lambda x,y: -1
        self.assertRaises(IndexError, self.AI.Roll)

    def tearDown(self):
        rps_oop.randint = random.randint


class RPSPlayerInputCase(unittest.TestCase):
    def setUp(self):
        self.Player = Player()

    def testPlayerInvalidInput(self):
        """Test if an exception arises for invalid input."""
        rps_oop.raw_input = lambda _: 'whatever'
        self.assertRaises(InvalidRollOptionError, self.Player.Input)

    def testPlayerValidInput(self):
        """Test if a valid input returns appropriate class."""
        rps_oop.raw_input = lambda _: 'scissors'
        self.assertEquals(self.Player.Input(), Scissors)

        rps_oop.raw_input = lambda _: 'rock'
        self.assertEquals(self.Player.Input(), Rock)

        rps_oop.raw_input = lambda _: 'paper'
        self.assertEquals(self.Player.Input(), Paper)

    def testPlayerValidInputInvalidCase(self):
        """Test if a valid input given in improper letter case works."""
        rps_oop.raw_input = lambda _: 'sciSsors'
        self.assertEquals(self.Player.Input(), Scissors)

        rps_oop.raw_input = lambda _: 'roCk'
        self.assertEquals(self.Player.Input(), Rock)

        rps_oop.raw_input = lambda _: 'paPer'
        self.assertEquals(self.Player.Input(), Paper)

class RPSPlayerNameCase(unittest.TestCase):
    def setUp(self):
        self.AI = AI('AIname')

    def testAIName(self):
        self.assertEquals(self.AI.name, 'AIname')

    def testAIInsufficientArguments(self):
        self.assertRaises(TypeError, AI)

    def testAINoneName(self):
        self.assertRaises(InvalidPlayerNameError, AI, None)


class RPSWeightCase(unittest.TestCase):
    def setUp(self):
        pass

    def test2Players(self):
        """Test the weight victory condition."""

        self.assertEqual(RollHandler.Weigh(Rock, Scissors), "Player 1 wins.")
        self.assertEqual(RollHandler.Weigh(Rock, Paper), "Player 2 wins.")
        self.assertEqual(RollHandler.Weigh(Rock, Rock), "It's a draw!")

    def test3Players(self):
        pass

    def testMorePlayers(self):
        pass


if __name__ == "__main__":
    unittest.main(buffer=True)
