def userInput(first_player, second_player):

    if first_player == second_player:
        print("Tie the game!")

    elif first_player == "rock":
        if second_player == "paper":
            print("Player-2 won the game!")
        else:
            print("Player-1 won the game!")

    elif first_player == "scissors":
        if second_player == "rock":
            print("Player-2 won the game!")
        else:
            print("Player-1 won the game!")

    elif first_player == "paper":
        if second_player == "scissors":
            print("Player-2 won the game!")
        else:
            print("Player-1 won the game!")
    else:
        print("Enter valid rock/paper/scissors command")


while True:
    first_player = input("First player-Enter your word: ").lower()
    second_player = input("Second player- Enter your word: ")
    userInput(first_player, second_player)
