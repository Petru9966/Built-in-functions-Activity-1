#ask the user to input a single character
print("\n\t\t\tProgram started")
print("\n\tEnter a single one standard character,\t please!")
#define the user's answer as an input
character=input()
#make sure there is a single character inputed, otherwise terminate the program and tell the warn the User
if (len(character))!=1:
  print("You supposed to enter A SINGLE ONE CHARACTER!")
else:
  print("The ASCII code for" , character, "is", ord(character))