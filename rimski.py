# Brojevi: Prvi, srednji i zadnji: I V X
#                                  X L C
#                                  C D M
# Opsezi:
#   1 - 3: I II III => ako je manje ili jednako tri, saberi, i napisi tol'ko I
#   4: IV => ako je 4, napisi prvi + srednji
#   5 - 8: V VI VII VIII => ako je vece ili jednako 5, a manje ili jednako 8, oduzmi 5 od zbira, i nakaci toliko prvih na srednji (VII za 7: 7 - 5 = 2)
#   9: IX => ako je 9, napisi prvi + zadnji

def romanize(number, glyphs):
    if number >= 1 and number <= 3:
        return number*glyphs[0]
    elif number == 4:
        return glyphs[0] + glyphs[1]
    elif number >= 5 and number <= 8:
        return glyphs[1] + ((number - 5) * glyphs[0])
    elif number == 9:
        return glyphs[0]+glyphs[2]
    else:
        return ''

simboli_jedinica = ['I', 'V', 'X']
simboli_desetica = ['X', 'L', 'C']
simboli_stotina = ['C', 'D', 'M']

dalje = 'da'

while dalje != 'ne':
    broj = int(raw_input('Unesi broj: '))

    cifra_hiljade = broj / 1000
    cifra_stotine = broj % 1000 / 100
    cifra_desetice = broj % 100 / 10
    cifra_jedinice = broj % 10

    output = cifra_hiljade*'M'
    output += romanize(cifra_stotine, simboli_stotina)
    output += romanize(cifra_desetice, simboli_desetica)
    output += romanize(cifra_jedinice, simboli_jedinica)

    print output

    dalje = raw_input('Da li zelite da pretvorite jos jedan broj? ([da]/ne)')
