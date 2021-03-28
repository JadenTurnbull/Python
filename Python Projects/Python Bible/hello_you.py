#Ask user for name

name = input("What is your name? ")
print(name)

#Ask user for age

age = input("How old are you?: ")
print(age)

#Ask user for location

city = input("What city do you live in?")
print(city)

#Ask user what they enjoy

love = input("What things do you enjoy doing?: ")
print(love)

#Create output text

string = "Your name is {} and you are {} years old, you live in {} and you love {}"
output = string.format(name, age, city, love)
print(output)

#Print output to screen



