import random 

random_number = random.randint(1,10) # numbers 1-10 
guess = None 
while guess != random_number: 
	guess = input("Pick a number from 1 to 10: ")
	guess = int(guess)		
	if guess < random_number: 
		print("TOO LOW!")
	elif guess > random_number: 
		print("TOO HIGH!")
	else: 
		print("YOU WON!!")
		play_again = input("Do you want to play again (y/n) ")
		if play_again == 'y': 
			random_number = random.randint(1,10)
			guess = None 
		else: 
			print("Thanks for playing")
			break
	print(f"Correct number was: {random_number}")



# handle user guesses 
# 	if they guess correct, tell them they won 
# 	otherwise tell them if they are too high or too low 


#	 Bonus -let the player again if they want