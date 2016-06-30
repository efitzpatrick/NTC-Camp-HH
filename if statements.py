#If Statements 

def soccer_league(age, gender):
	#13 and 17
	if gender == "female":
		if age < 13:
			print("You are too young!! Come back at age 13!")
		elif age > 17:
			print("You are too old! Send your future kids")
		else:
			print("You are eligable, sign up!!!!")

	else:
		print("You must be a girl to be in our soccer leauge!")


soccer_league(15, "female")
soccer_league(7, "female")
soccer_league(21, "female")
soccer_league(5, "male")