def cezar(sifra):
    temp  = sifra.upper()
    result = []
    for slovo in temp:
                order = ord(slovo)
    order -= 3
    if order < 65:
                order += 26

    result.append(chr(order))
    return ''.join(result)

print cezar(raw_input("sifra: "))