from rps_oop import Player, AI, RollHandler

if __name__ == "__main__":
    player = Player()
    ai = AI('Computer')

    question = 'yes'

    while question != 'n':
        player.Input()
        ai.Roll()
        print RollHandler.Weigh(player.choice, ai.choice)

        question = raw_input("Do you wanna go for another roll? [y]/n: ")
