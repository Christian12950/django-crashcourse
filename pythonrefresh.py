# C:\Users\Chris\OneDrive\Documents\GitHub\django-crashcourse

name = "Bruce"
status = True
age = 19

""" comment 
    for multiple lines"""

# sentence = "Hi my name is %s and I am %d years old" (name, age)
sentence = "Hi my name is {} and I am {} years old".format(name, age)

print(sentence)

if age > 18 and name == "Bruce":
    print("You old, {}".format(name))
elif age == 18:
    print("You young {}".format(name))

if status:
    print("yuh")


year = 2010 # When you check your solution, don't change this number

if year >= 2000 and year <= 2100:
    print("Welcome to the 21st century!")
else:
    print("You are before or after the 21st century")