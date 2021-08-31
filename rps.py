from rndm import randint
t = [ "Rock" , "Paper" , "Scissors"]

computer = t[randint(0,2)]

player = False

while player == False"
    player = input( "Rock" , "Paper" , "Scossors")
    if player == computer:
        print("Tie")
    elif player == "Rock": 
        if computer == "Paper":
            print("You lose" , computer , "covers" , player)   
                else: 
                    print(" You win")
    elif player == "Paper": 
        if computer == "Scissors":
            print("You lose" , computer , "cut" , player)   
                else: 
                    print(" You win")   
    elif player == "Scissors": 
        if computer == "Rock":
            print("You lose" , computer , "smashed" , player)   
                else: 
                    print(" You win")    
    else:
    print ("That is not a valid play. Check your spelling")

    player = False
    computer = t[randint(0,2)]            

