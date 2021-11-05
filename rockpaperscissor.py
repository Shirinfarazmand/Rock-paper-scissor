import random

userWins = 0
computerWins = 0
ties = 0
options = ["rock", "paper", "scissors"]

while True:
    userInput = input("Type rock/paper/scissors or q to quit: ").lower()
    if userInput == "q":
        quit("bye bye")

    if userInput not in options: 
        continue

    randomNum = random.randint(0,2)
    # rock:0 , paper:1 , scissors:2
    computerPick = options[randomNum] 
    print("Computer picked", computerPick + ".")

    if userInput == "rock" and computerPick == "scissors":
        print("YOU WON!")
        userWins +=1
    
    elif userInput == "paper" and computerPick == "rock":
        print("YOU WON!")
        userWins +=1

    elif userInput == "scissors" and computerPick == "paper":
        print("YOU WON!")
        userWins +=1
    
    elif userInput == computerPick :
        print("YOU  TIE!")
        ties +=1
    
    else:
            print("YOU LOST!")
            computerWins +=1

    print("You won", userWins ,"times")

    print("Computer won", computerWins ,"times")

    print("You tie", ties ,"times")

