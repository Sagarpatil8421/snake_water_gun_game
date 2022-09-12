# Snake water gun 
import random 

def game(comp, player):
    if comp == player:
        return None

    elif comp == 's':
        if player == 'w':
            return False
        elif player == 'g':
            return True

    elif comp == 'w':
        if player == 'g':
            return False
        elif player == 's':
            return True

    elif comp == 'g':
        if player == 's':
            return False
        elif player == 'w':
            return True


print("Computers turn Sanke(s) Water(w) and Gun(g) : ")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

player = input("Your turn Sanke(s) Water(w) and Gun(g) : ")
winner = game(comp, player)

print(f"Computer Choose {comp}")
print(f"You Choose {player}")

if(winner == None ):
    print("The game is Tie!")
elif winner:
    print("You Win!") 
else:
    print("You Lose!")

