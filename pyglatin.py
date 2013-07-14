# 1 - ako rec pocinje sa samoglasnikom, dodaj 'ay' na kraj
# 2 - ako rec pocinje sa suglasnikom, odseci do prvog samoglasnika, prebaci to na kraj i dodaj 'ay' na kraj
# 3 - ako nema samoglasnika, dodaj 'ay'
vokali = ['a', 'e', 'i', 'o', 'u']

play_again = 'da'

while play_again == 'da' or play_again == 'yes' or play_again == 'y':

    recenica = raw_input('Unesite recenicu: ')

    for rec in recenica.split():

        if rec[0] in vokali:
            rec += 'ay'
        else:
            for slovo in rec:
                if slovo in vokali:
                    seci_do = rec.index(slovo)
                    rec = rec[seci_do:] + rec[0:seci_do] + 'ay'
                    break
            else:
                rec += 'ay'

        print rec,

    print
    play_again = raw_input('Da li zelite da unesete novu recenicu: ')