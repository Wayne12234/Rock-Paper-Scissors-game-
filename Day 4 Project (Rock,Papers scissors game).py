print("Welcome to the rock, paper and scissors game\n")
import random
outputs=["Rock","Paper","Scissors"]
user_choose=random.choice(outputs)
print(f"You chose {user_choose}\n")

computer_choose=random.choice(outputs)
print(f"Computer chose {computer_choose}\n")

if user_choose==computer_choose:
    print("This is a draw")

elif user_choose=="Rock" and computer_choose=="Paper":
    print("You won")
elif user_choose=="Rock" and computer_choose=="Scissors":
    print("You won")

elif user_choose=="Paper" and computer_choose=="Scissors":
    print("Computer won")
elif user_choose=="Paper" and computer_choose=="Rock":
    print("You won")

elif user_choose=="Scissors" and computer_choose=="Paper":
    print("You won")
elif user_choose=="Scissors" and computer_choose=="Rock":
    print("Computer won")