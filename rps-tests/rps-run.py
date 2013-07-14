from rps_oop import Player, AI, RollHandler

if __name__ == "__main__":
    player = Player()
    ai = AI('Computer')

    question = 'yes'

    while question != 'n':
        print player.name + " chooses " + player.Input().name + "."
        print ai.name + " chooses " + ai.Roll().name + "."
        print RollHandler.Weigh(player, ai)

        question = raw_input("Do you wanna go for another roll? [y]/n: ")
