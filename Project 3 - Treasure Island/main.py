print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

      ''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('you\'re at a crossword, where do you want to go ? Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('you\'ve come to a lake. there is an island in the middle of the lake.Type "wait" to wait for a boat. Type "swim to swim across?\n').lower()
    if choice2 == "wait":
        choice3 = input('you\'ve arrived at the island unharmed.There is a house with three doors one red one yellow and one blue. Which colour do you choose?\n').lower()
        if choice3 == "red":
           print("it's a room full of fire.Game Over.")
        elif choice3 == "yellow":
           print("You found the treasure! You Win!")
        elif choice3 == "blue":
           print("You enter a room of beasts.Game Over.")
        else:
            print("You choose a door that doesn't exists.")
    else:
        print("You got attacked by the angry trout. Game Over")
else:
    print("You fell into a hole. Game Over.")
        