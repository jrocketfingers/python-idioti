# Brojevi: Prvi, srednji i zadnji: I V X
#                                  X L C
#                                  C D M
# Opsezi:
#   1 - 3: I II III => ako je manje ili jednako tri, saberi, i napisi tol'ko I
#   4: IV => ako je 4, napisi prvi + srednji
#   5 - 8: V VI VII VIII => ako je vece ili jednako 5, a manje ili jednako 8, oduzmi 5 od dobijene vrednosti, i nakaci toliko prvih na srednji (VII za 7: 7 - 5 = 2)
#   9: IX => ako je 9, napisi prvi + zadnji
#
#
# romanize - pretvara cifru u rimski ekvivalent
# digitize - pretvara broj u set cifara
# digits_to_roman - poziva romanize za svaki clan seta cifra koji nam vraca digitize

"""
"""

def romanize(digit, glyphs):
    """
    >>> romanize(5, ['I','V','X'])
    'V'
    >>> romanize(6, ['I','V','X'])
    'VI'
    >>> romanize(3, ['I','V','X'])
    'III'
    >>> romanize(4, ['I','V','X'])
    'IV'
    >>> romanize(9, ['I','V','X'])
    'IX'
    >>> romanize(5, ['X','L','C'])
    'L'
    >>> romanize(6, ['X','L','C'])
    'LX'
    >>> romanize(3, ['X','L','C'])
    'XXX'
    >>> romanize(4, ['X','L','C'])
    'XL'
    >>> romanize(9, ['X','L','C'])
    'XC'
    """
    if 1 <= digit <= 3:
        return digit*glyphs[0]
    elif digit == 4:
        return glyphs[0] + glyphs[1]
    elif digit >= 5 and digit <= 8:
        return glyphs[1] + ((digit - 5) * glyphs[0])
    elif digit == 9:
        return glyphs[0]+glyphs[2]
    else:
        return ''

def digitize(number):
    thousands = number / 1000
    hundreds = number % 1000 / 100
    tens = number % 100 / 10
    ones = number % 10

    return (ones, tens, hundreds, thousands)

def digits_to_roman(digits):
    ones_glyphs = ['I', 'V', 'X']
    tens_glyphs = ['X', 'L', 'C']
    hundreds_glyphs = ['C', 'D', 'M']

    output = digits[3]*'M'
    output += romanize(digits[2], hundreds_glyphs)
    output += romanize(digits[1], tens_glyphs)
    output += romanize(digits[0], ones_glyphs)

    return output


if __name__ == '__main__':
    dalje = 'da'

    while dalje != 'ne':
        broj = digits_to_roman(digitize(int(raw_input('Unesi broj: '))))

        print broj

        dalje = raw_input('Da li zelite da pretvorite jos jedan broj? ([da]/ne)')
