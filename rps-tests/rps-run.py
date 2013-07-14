from rps_oop import Player, AI, RollHandler, InvalidRollOptionError

if __name__ == "__main__":
    player = Player()
    ai = AI('Computer')

    question = 'yes'

    while question != 'n':
        try:
            print player.name + " chooses " + player.Input().name + "."
            print ai.name + " chooses " + ai.Roll().name + "."
            print RollHandler.Weigh(player, ai)
        except InvalidRollOptionError:
            print "Invalid choice. Please choose from rock/paper/scissors."

        print

        question = raw_input("Do you wanna go for another roll? [y]/n: ")

        print
