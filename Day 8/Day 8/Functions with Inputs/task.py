def greet():
    print("hello")
    print("welcome")
    print("Bye")


#function that allow input
def greet_with_name(name):
    print(f"Hello {name}.")
    print(f"Welcome {name} to python series.")
    print(f"How are you {name}?")
#greet_with_name("Angela")

#funtion with two parameter
def greet_with_name_location(name,location):
    print(f"Your name is {name},and your location is {location}")
greet_with_name_location("tabrez","Delhi")