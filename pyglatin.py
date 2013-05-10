# 1 - ako rec pocinje sa samoglasnikom, dodaj 'ay' na kraj
# 2 - ako rec pocinje sa suglasnikom, odseci do prvog samoglasnika, prebaci to na kraj i dodaj 'ay' na kraj
# 3 - ako nema samoglasnika, dodaj 'ay'
vokali = ['a', 'e', 'i', 'o', 'u']

pitanje = 'da'

while pitanje == 'da':

    recenica = raw_input('Unesite recenicu: ')

    for reci in recenica.split():

        if reci[0] in vokali:
            reci += 'ay'
        else:
            ima_samoglasnik = False

            for slovo in reci:
                if slovo in vokali:
                    seci_do = reci.index(slovo)
                    reci = reci[seci_do:] + reci[0:seci_do] + 'ay'
                    ima_samoglasnik = True
                    break

            if ima_samoglasnik == False:
                reci += 'ay'

        print reci,

    print
    pitanje = raw_input('Da li zelite da unesete novu recenicu: ')