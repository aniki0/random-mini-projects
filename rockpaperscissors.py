# rock, paper, scissors

from random import randint

intro = "hi! welcome to this REALLY simple game of Rock, Paper, Scissors. To stop playing, enter 'k'."
print(intro)

while True:

    player = input("rock (r), paper (p), scissors (s)? ")

    if player not in ("r", "p", "s", "k"):
        print("please enter a correct input")

    elif player == "k":
        print("thank you for playing!")
        break
    
    else:
        chosen = randint(1, 3)
        
        if chosen == 1:
            comp = "r"
        elif chosen == 2:
            comp = "p"
        else:
            comp = "s"
        print(player, "vs", comp)

        if (player == "r" and comp == "r") or (player == "p" and comp == "p") or (player == "s" and comp == "s"):
            print("draw")
        elif (player == "r" and comp == "p") or (player == "p" and comp == "s") or (player == "s" and comp == "r"):
            print("you lost!")
        else:
            print("you win!")
