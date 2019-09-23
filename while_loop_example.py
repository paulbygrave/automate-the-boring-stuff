spam = 0
while spam < 5:
    spam = spam + 1
    # Use continue statement to jump back to the start of the loop
    if spam ==3:
        continue
    print ('spam is ' + str(spam))
