print('How many dogs do you have?')
numDogs = input()
try:
    if int(numDogs) >= 5:
        print('That is quite a few dogs...')
    else:
        print('That is not enough dogs. You need more dogs!')
except ValueError:
    print("You didn't enter a number!")
