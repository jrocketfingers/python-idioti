#==============================================================================#
# 3x+1 problem: svaki broj za koji se primeni x%2==0 => x/2 v x%2!=0 => 3x+1   #
# se u jednom trenutku svoje sekvence svodi na 1.                              #
#==============================================================================#

import os, fileinput

# Pocetni broj je hardkodovan (upisan u samom kodu)
# Moramo ga zabeleziti da bismo kasnije mogli nastaviti od zadnjeg broja na kom
# smo stali, jer je problem potencijalno neresiv.
broj = 221269363
# Neophodno je zadrzati prvi upotrebljeni broj da bismo ga posle mogli naci
# u kodu, i izvrsili zamenu sa novim zadnjim brojem (posto nastavljamo svaki put)
pocetni_broj = broj

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

    trix = fileinput.input(os.path.realpath(__file__), inplace=1)

    for line in trix:
        if line.startswith('broj ='):
            line = line.replace(str(pocetni_broj), str(broj))
        print line,