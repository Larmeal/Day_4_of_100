import random
import Game_Paper_Rock_Scissors

Rock = Game_Paper_Rock_Scissors.rock
Paper = Game_Paper_Rock_Scissors.paper
Scissors = Game_Paper_Rock_Scissors.scissors

print("Welcome to the Paper, Rock and Scissor. Are you ready to play? ")
choose = int(input("Choose your weapon to fight, 0 for Paper, 1 for Rock and 2 for Scissor.\n"))

if choose < 3 and choose >= 0:
    print("\nYou chose: ")
else:
    print("\nYou try to cheat our game!!, That don't fare for everyone. You lose!!")

if choose == 0:
    print(Rock)
elif choose == 1:
    print(Paper)
elif choose == 2:
    print(Scissors)

print(f"\nComputer chose:")
com_choose = random.randint(0, 2)
if com_choose == 0:
    print(Rock)
elif com_choose == 1:
    print(Paper)
elif com_choose == 2:
    print(Scissors)

if choose == com_choose:
    print("You draw")
elif choose == 0  and com_choose == 1:
    print("You lose")
elif choose == 0 and com_choose == 2:
    print("You win")
elif choose == 1  and com_choose == 0:
    print("You win")
elif choose == 1 and com_choose == 2:
    print("You lose")
elif choose == 2  and com_choose == 0:
    print("You lose")
elif choose == 2 and com_choose == 1:
    print("You win")

