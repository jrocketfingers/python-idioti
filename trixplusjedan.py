broj = 200480903

max_koraka = 0
max_broj = 1

try:
    while True:
        racun = broj

        broj_koraka = 0

        while racun != 1:
            if (racun % 2) == 0:
                racun = racun / 2
            else:
                racun = 3 * racun + 1
            broj_koraka += 1

        if broj_koraka > max_koraka:
            max_koraka = broj_koraka
            max_broj = broj


       # print broj, 'se zavrsava sa 1, sa', broj_koraka, 'koraka'
       # print
        broj += 1
except KeyboardInterrupt:
    print
    if broj_koraka > max_koraka:
        max_koraka = broj_koraka
        max_broj = broj
        print 'Obracun ovog broja jos nije gotov! Potencijalni najduzi/neresivi!'

    print 'Najveci broj koraka (%d) je bio za broj %d' % (max_koraka, max_broj)
    print 'A poslednji broj je', broj