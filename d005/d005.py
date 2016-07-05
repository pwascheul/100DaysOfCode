import sys
import random
auto_num =0;
nb_guess=0;
guessCount=0;

def guess(number):
	if number == auto_num:
		print "CONGRATULATIONS, you got the number in %i guesses! " % guessCount
		return True
	else:
		if number > auto_num:
			print "Sorry, thats not the number, try guessing lower"
			return False
		else:
			print "Sorry,thats not the number, try guessing higher"
			return False

max_attempt = raw_input("Welcome, Please put your number of tentative : ")
max_attempt = int(max_attempt)
auto_num = random.randint(1, 100)
success = False
while success == False:
	if guessCount == max_attempt :
		print "You did not succeed to find it; the answer was %i !" % auto_num
		sys.exit(0)
	playerInput = raw_input("Please enter your guess [1-100]: ")
	playerInput = playerInput.strip()
	if not playerInput.isdigit():
		print "You did not enter a valid number, please try again"
	else:
 		success = guess(int(playerInput))
		guessCount +=1
	
