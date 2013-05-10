enkriptovano = raw_input('Unesite enkriptovani podatak: ')

def offset_a_letter(letter, offset):
    if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
        if ord(letter) + offset > ord('z'):
            return chr(abs(ord('z') - ord(letter) - offset) + ord('a') - 1)
        return chr(ord(letter) + offset)
    else:
        return letter

enkriptovano = enkriptovano.lower()

offset = 0

while offset < ord('z') - ord('a') + 1:
    row = [offset_a_letter(letter, offset) for letter in enkriptovano]
    print "%d: %s" % (offset, str.join('', row))
    offset += 1
