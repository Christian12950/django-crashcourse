# C:\Users\Chris\OneDrive\Documents\GitHub\django-crashcourse

# HERE IS SOME QUICK EXAMPLES OF SIMPLE PYTHON CONCEPTS

"""
FORMAT AND PRINT

sentence = "Hi my name is %s and I am %d years old" (name, age)
sentence = "Hi my name is {} and I am {} years old".format(name, age)

print(sentence)
"""

"""
IF ELSE STATEMENTS
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
"""

""""
FUNCTIONS

def hello(inpoot):
    print("Hello {}".format(inpoot))


hello("Christian")
hello(25)
"""

"""
LISTS

myDudes = ["yo", "my", "dude", 24]
myDudes.insert(myDudes.__len__(), "Bada Bing")  # This will throw it at the end of the list
myDudes.insert(len(myDudes), "Bada Boom")  # Same here
del(myDudes[1])
print(myDudes)
"""

"""
LOOPS

for i in myDudes:
    print(myDudes)

for i in range(0, len(myDudes)):
    print(myDudes[i])


age = 0
while age < 18:
    print(age)
    age += 1
"""

""" 
DICTIONARY, KEY POINTS TO VALUE SIMILAR TO HASHMAP 

employee = {1: "Chris", 2: "Bruce", 3: "Charles"}
del employee[2]
employee[1] = "Not Chris"  # Changes name, not adds to 1 like a HM
employee["woah"] = 0
print(employee)

#Small example
words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]
cooldictionary = {}
for i in range(0, len(words)):
    cooldictionary[words[i]] = definitions[i]

print(cooldictionary)
"""

"""
class Dog:
    def __init__(self, namePassed, agePassed, breedPassed):
        self.name = namePassed
        self.age = agePassed
        self.breed = breedPassed

    def bark(self, inpt):
        print(inpt)


myDog = Dog("Mia", 14, "Golden Retriever")
myDog.bark("Woof")
myDog.gender = "Female"  # Python lets you define new class variables anywhere AFTER declaration

print(myDog.name)
print(myDog.breed)


# Another example
class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        return 2018 - self.year
"""