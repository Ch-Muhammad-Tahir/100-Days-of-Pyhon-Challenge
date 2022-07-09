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

# Write your code below this line 👇

player_choose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
game_items = [rock, paper, scissors]
if player_choose == "0":
    print(game_items[0])
elif player_choose == "1":
    print(game_items[1])
elif player_choose == "2":
    print(game_items[2])

print("Computer Choose ")
computer_choose = random.choice(game_items)
print(computer_choose)
