print("Guess the Number\n")

num = 77000
attemp = 0

while True:
    answer = int(input("Input The Number of Me: "))
    if answer < 0:
        print("Please Input Number Positif!")
        exit()
    if answer < num:
        print("To Low")
        attemp += 1
    elif answer > num:
        print("Too High")
        attemp += 1
        continue
    elif answer == num:
        print("Correct")
        attemp += 1
        break
    else:
        print("That is not a number I recognize.")
    
    """ if answer == num:
        print("It took you", attemp, "guesses to get it correct!")
        exit()
    else:
        continue """
        
print("It took you", attemp, "guesses to get it correct!")
