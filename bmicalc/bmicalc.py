#BMI calc

#Square a number
def square(num):
	return num * num

#Convert cm to meters (float)
def convert(cm):
	return cm / 100

#Is BMI within healthy range?
def ishealthy(x):
	if x > 18.5 and x < 24.9:
		return True

def calcbmi():
	try:
		print("Sander sin bmi calc!")
		userh = float(input("Height:"))
		userw = float(input("Weight:"))
	except:
		print("Thats not a number!")
		calcbmi()
	
	#Return the calculated bmi, rounted to two decimals
	return round( userw / square(convert(userh)) ,2)

def programstart():
	#Call func to get bmi data from user and store it as bmi
	bmi = calcbmi()

	#Print the bmi
	print("Your bmi is: " + str(bmi))

	#Check if bmi is within the healthy ranges and print the result
	if bmi > 18.5 and bmi < 24.9:
		print("Thats healthy!")
	else:
		print("Not Healthy!")

programstart()