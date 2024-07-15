import random

print(("""
Type 1 for ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)       
"""))
print("""
Type 2 for SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
print("""
Type 3 for PAPER
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
user = input()
computer = random.randint(1,3)

print(computer)
fuser = int(user)

if fuser == 1 and computer == 2:
  print("you won.")
elif fuser == computer:
  print("draw")
elif fuser == 2 and computer == 3:
  print("you won.")
elif fuser == 3 and computer == 1:
  print("you won.")
else:
  print("you loose.")
