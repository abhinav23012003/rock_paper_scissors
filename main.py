import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Write your code below this line 👇

collections = [rock, paper, scissors]
print("Welcome to the GAME: Rock-Paper-Scissors.")
choice = int(input("Enter 1 for Rock, 2 for Paper and 3 for Scissors.\n"))
computer_choice = random.randint(0, 2)
if choice == 1:
    print(f"Your choice is {rock}")
    print(f"Computer's choice is {collections[computer_choice]}")

elif choice == 2:
    print(f"Your choice is {paper}")
    print(f"Computer's choice is {collections[computer_choice]}")

elif choice == 3:
    print(f"Your choice is {scissors}")
    print(f"Computer's choice is {collections[computer_choice]}")

else:
    print("Wrong Input...")

if choice - 1 == computer_choice:
    print("Match Draw")
elif choice == 1 and computer_choice == 2:
    print("You Win")
elif choice == 3 and computer_choice == 0:
    print("You Lose")
elif choice - 1 > computer_choice:
    print("You Win")
elif choice - 1 < computer_choice:
    print("You Lose")
else:
    print("Something Wrong!")
