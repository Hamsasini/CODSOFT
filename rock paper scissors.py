import random
def play_game():
    choices = ["rock", "paper", "scissors"]
    userchoice = input("Choose rock,paper or scissors: ").lower()
    computerchoice = random.choice(choices)

    print("Computer chose",computerchoice.capitalize())

    if userchoice == computerchoice:
        return "Game tie!"
    elif (userchoice == "rock" and computerchoice == "scissors") or (userchoice == "paper" and computerchoice == "rock") or(userchoice == "scissors" and computerchoice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    userscore = 0
    computerscore = 0

    while True:
        result = play_game()
        print(result)

        if "You win" in result:
            userscore += 1
        elif "Computer wins" in result:
            computerscore += 1
        print("Score: User -",userscore, "Computer -",computerscore)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "no":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
