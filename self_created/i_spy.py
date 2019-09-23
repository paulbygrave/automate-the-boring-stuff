# A game of "I, Spy"
import sys

attempts = 0
guess = ''
while guess != 'desk' and attempts < 5:
    attempts = attempts + 1
    if attempts == 5:
        print("You didn't guess it!"); sys.exit()
    else:
        print('I spy with my little eye, something beginning with d...')
        guess = input()
print('You got it!')


