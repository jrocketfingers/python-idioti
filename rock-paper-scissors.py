from random import randint

again = 'Y'

choices = [ \
        { \
            'type': 'rock', \
            'weaker': 2, \
            'stronger': 1 \
        }, \
        { \
            'type': 'paper', \
            'weaker': 0, \
            'stronger': 2 \
        }, \
        { \
            'type': 'scissors', \
            'weaker': 1, \
            'stronger': 0 \
        }]

mapping = {'rock': 0, 'paper': 1, 'scissors': 2}

while again != 'n':

    chosen = raw_input('Chooose from rock, paper, scissors. Type in without spelling errors: ')

    if mapping.has_key(chosen):

        computer_choice = randint(0, 2)

        if computer_choice == mapping[chosen]:
            print 'It\'s a draw! (%s,%s)' % (choices[computer_choice]['type'], choices[mapping[chosen]]['type'])
        elif mapping[chosen] == choices[computer_choice]['weaker']:
            print '%s beats %s! Computer wins!' % (choices[computer_choice]['type'], choices[mapping[chosen]]['type'])
        elif  mapping[chosen] == choices[computer_choice]['stronger']:
            print '%s beats %s! Player wins!' % (choices[mapping[chosen]]['type'], choices[computer_choice]['type'])
        else:
            print 'ERROR', mapping[chosen], computer_choice

    else:
        print 'Invalid input! Please make sure to type the names exactly!'

    again = raw_input('Go again? (Y/n): ')