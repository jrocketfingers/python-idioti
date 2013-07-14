from random import randint

class InvalidRollOptionError(Exception):
    pass

class InvalidPlayerNameError(Exception):
    pass


class Rock:
    name = "rock"


class Paper:
    name = "paper"


class Scissors:
    name = "scissors"


Rock.stronger_than = Scissors
Rock.weaker_than = Paper
Paper.stronger_than = Rock
Paper.weaker_than = Scissors
Scissors.stronger_than = Paper
Scissors.weaker_than = Rock


class RollHandler:

    options = [Rock, Paper, Scissors]

    @staticmethod
    def Weigh(player1, player2):
        if player1.choice.stronger_than == player2.choice:
            return player1.name + " wins."
        elif player1.choice == player2.choice:
            return "It's a draw!"
        else:
            return  player2.name + " wins."


class AI:

    choice = None

    def __init__(self, name):
        if name is not None:
            self.name = name
        else:
            raise InvalidPlayerNameError

    def Roll(self):
        choice = randint(0,2)
        if choice < len(RollHandler.options) and choice >= 0:
            self.choice = RollHandler.options[choice]
            print self.name, "chooses", self.choice.name
            return self.choice
        else:
            raise IndexError


class Player:

    options = {"rock": Rock, "paper": Paper, "scissors": Scissors}

    choice = None

    name = "Player"

    def Input(self):
        choice = raw_input("Input <rock/paper/scissors>: ").lower()
        if self.options.has_key(choice):
            self.choice = self.options[choice]
            print "Player chooses", self.choice.name
            return self.choice
        else:
            raise InvalidRollOptionError