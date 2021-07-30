#This will be a simple rock paper scissors game!
#I'm building this to practice my skills
#So don't expect nothing complex
#Enjoy!


import random

user = int(input('Welcome to Rock, Paper, Scissors. Choose 0 for rock, 1 for paper and 2 for scissors.\n'))

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

randomness = random.randint(0,2)

if user == 0:
    print(f"You choose rock \n {rock}")
elif user == 1:
    print(f'You choose paper \n {paper}')
else:
    print(f'You choose scissors \n {scissors}')


print('The computer chooses...')

if randomness == 0:
    print(f"Rock! \n {rock}")
elif randomness == 1:
    print(f'Paper! \n {paper}')
else:
    print(f'Scissors! \n {scissors}')

whowins = ''

if user == 0 and randomness == 2:
    print('Rock beats scissors! You won!')
elif user == 1 and randomness == 2:
    print("Scissors beats paper. You lost!")
elif user == 2 and randomness == 2:
    print("Both choose scissors. It's a tie!")
elif user == 0 and randomness == 0:
    print ("Both choose rock. Its a tie.")
elif user == 1 and randomness == 0:
    print("Paper beats rock. You won!")
elif user == 2 and randomness == 0:
    print('Rock beats scissors! You lost!') 
elif user == 0 and randomness == 1:
    print("Paper beats rock. You lost!")
elif user == 1 and randomness == 1:
    print("Both choose paper. It's a tie.")
elif user == 2 and randomness == 1:
    print("Scissors beats paper. You won!")
else:
    print('Something went wrong.')



