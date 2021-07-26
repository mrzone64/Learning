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

#Takes input from user
#height = int(input("Height:"))
#weight = int(input("Weight:"))

#bmi gets calculated
#bmi = weight / square(convert(height))

def calcbmi():
    try:
        print("Sander sin bmi calc!")
        userh = float(input("Height:"))
        userw = float(input("Weight:"))

        return userw / square(convert(userh))
    except:
        print("Thats not a number!")
        calcbmi()

bmi = calcbmi()

#output bmi with 2 decimals
print("Your bmi is: " + str(bmi))

#Healthy or not?
if ishealthy(bmi):
    print("Thats healthy!")
else:
    print("Not Healthy!")