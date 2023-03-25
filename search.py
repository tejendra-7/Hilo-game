low = 1
high = 1000

#take a number between 1 to 1000 and start searching the number using this code
# You can find the number you are searching with in 10 guesses (This is a Binary search algorithm)

print("Please think of a number between {} and {}".format(low,high))
input("Press ENTER to start")

guesses = 1
while low != high:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower"
                     "Enter h or l, or c if my guess is correct : "
                     .format(guess)).casefold()
    if high_low == "h":
        # Guess higher
        low = guess + 1
    elif high_low == "l":
        # Guess lower
        high = guess -1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")

    guesses = guesses + 1
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))