import random

# Printing heads or tails randomly
# random_num = random.randint(0, 1)
# if random_num == 0:
#     print("Heads.")
# else:
#     print("Tails.")
#
# Printing random names from a list
# friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]
# random_index = random.randint(0, len(friends) -1)
# print(friends[random_index], random.choice(friends))

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("")

user_choice = input("Welcome to Rock Paper Scissors, Type 1 for Rock, 2 for paper or 3 for scissors:\n")

random_choice = random.choice([rock, paper, scissors])
# print(f"Computer chose:\n{random_choice}")
choice = None
if user_choice == "1":
    choice = rock

elif user_choice == "2":
    choice = paper

elif user_choice == "3":
    choice = scissors
else:
    print("Invalid Input,please try again!")
    exit()
if random_choice == rock and choice == scissors:
    print(f"You chose:{choice}\n"
          f"Computer chose:{random_choice}"
          f"You lose!")
elif random_choice == scissors and choice == paper:
    print(f"You chose:{choice}\n"
          f"Computer chose:{random_choice}\n"
          f"You lose!")
elif random_choice == paper and choice == rock:
    print(f"You chose:{choice}\n"
          f"Computer chose: {random_choice}\n"
          f"You lose!")
elif random_choice == choice:
    print(f"You both chose:{choice}\n"
          f"It is a tie!")
else:
    print(f"You chose:{choice}\n"
          f"Computer chose:{random_choice}\n"
          f"You win!")
