# This is a Guess the Number game.
import random # allows to use the randint funtion for random guessing

guess_taken = 0 # Stores the number of guesses the player has made

# Get user to input their name and store it in the my_name variable
my_name = input("Hello! What is your name? ")

# returns a random integer btwn and including the two integers
number = random.randint(1, 20)
print(f"Well, {my_name}, I am thinking of a number between 1 and 20.")

for guess_taken in range(6): # Excutes the game for 6 times
    guess = input(("Take a guess: "))
    guess = int(guess)

    if guess < number:
        print("Your guess is too low.")

    elif guess > number:
        print("Your is guess is too high.")

    else:
        break

if guess == number: # Checks to see if player guessed correctly
# Also shows the number of attempts it took for the user to guess
    guess_taken = str(guess_taken + 1) # Add one b/c range starts at 0
    print(f"Great job, {my_name}! You guessed my number in {guess_taken}\
 guesses!")

if guess != number: # if player runs out of guesses
#Tells the player what the secret number was
    print(f"Nope. The number I was thinking of was {number}.")
