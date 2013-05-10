#------------------------------------------------------------------------------#
# Ideja: napraviti tablicu svih mogucih kombinacija uz pomoc cezarove sifre    #
#------------------------------------------------------------------------------#

# Ucitavam enkriptovani string
enkriptovano = raw_input('Unesite enkriptovani podatak: ')

# Definisem funkciju za offestovanje slova
# u sustini je beskorisna, koristim je samo da bi kod bio iole jasniji
def offset_a_letter(letter, offset):
    return chr(ord(letter) + offset)

# Prebacujem sva slova u mala
# Ovo radim da bih koristio samo jednu velicinu slova
enkriptovano = enkriptovano.lower()

# Zanimljiv deo: Kako naci offset od kog poceti?
# Ako pocnemo sa t, treba da se vratimo 19 slova u nazad za a. Ali za koliko
# onda treba ici u nazad za neko drugo slovo?
#
# Problem #2: Ako za slovo t odgovara offset od 19 slova, sta ako u reci imamo
# slovo pre t? 'a' za 19 slova u nazad bi bilo veliko 'N'. I to je jos odlicno.
# Problem je u tome sto ASCII sadrzi karaktere van ovog opsega. Ako prekoracimo
# okvire malih slova (od 97 do 122), mozemo dobiti nepozeljne karaktere
# (ne slova).
#
# Resenje: Nadjemo slovo koje po ASCII vrednosti ima najvecu vrednost u sekvenci
# (u 'administratori', to bi bilo 't', posto je najdalje u abecedi). Tu najvisu
# vrednost cemo koristiti za odredjivanje najviseg offseta.
# Primer: ukoliko je slovo 'z' najvise, najvisi offset ce biti 0. Zasto?
# ako bi offset bio 1, dobili bi smo '{' kao znak, sto po cezarovoj sifri nije
# odgovarajuca, niti postojeca vrednost.
#
# Probajte da razumete problematiku najmanjeg broja, pa pisite na grupi sta ste
# skontali!
highest_letter_ascii = max(ord(letter) for letter in enkriptovano)
lowest_letter_ascii = min(ord(letter) for letter in enkriptovano)

# Inicijalni offset nam je prostor od prvog slova do slova a u azbuci.
initial_offset = ord('a') - lowest_letter_ascii
offset = initial_offset

# Current nam sluzi samo kao brojac, cisto radi licnog uvida u to koja je
# kombinacija trenutna.
current = 0

# (prva zagrada):
# Dok je offset - inicijalni offset razmak manji od 26 - jos uvek nismo prosli
# svih 26 potenijalnih kombinacija,
# (druga zagrada):
# i dok je najvisa ascii vrednost + offset manja od ascii vrednosti slova z,
# [da li je najvece slovo van opsega azbuke sa ovim offsetom?]:
#
# petljaj dalje!
while (offset - initial_offset < 26) and (highest_letter_ascii + offset <= ord('z')):
    # Ovde radimo citavu kombinaciju u cugu:
    # Citaj kao: [ofsetuj slovo] "slovo", za "offset", u "slovu iz enkriptovano"
    # u uglastim zagradama je operacija, pod navodnicima su varijable,
    # cisto da bih docarao da to nije recenica, vec ono sta se zaista kuca, ali
    # da se ne razlikuje od srpskog.
    # Ovakvo kucanje se zove *list comprehension*
    row = [offset_a_letter(letter, offset) for letter in enkriptovano]

    # Odstampaj taj red u formatu: trenutna kombinacija[offset kombinacije]: rec
    print "%d[%d]: %s" % (current, offset, str.join('', row))

    # Idi na sledeci offset
    offset += 1
    # Povecaj broj trenutne kombinacije za jedan
    current += 1


# BONUS: za one koji dobro citaju! Provalite u cemu je potencijalni nedostatak
# ovakvog pristupa izlistavanju. Probajte razne kombinacije pa utvrdite probleme
# na osnovu rezultata
# Hint: Cezar je ovo lako resio.
