print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You are at crossroad, where do you want to go "right" and "left"\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake, there is an iceland middle of the lake type wait to "wait" for the boat.'
                    ' or type "swim " to swim to cross\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrived at the iceland not harmed. there is a house with three doors. one red,"
                        " one yellow, one blue. which color do you choose.\n").lower()
        if choice3 == "red":
            print("Burned by fire. Game Over.")
        elif choice3 == "yellow":
            print("Congratulation! You won.")
        elif choice3 == "blue":
            print("Eaten by Beats. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attack by trout. Game Over.")
else:
    print("Fall in the hole. Game Over.")
