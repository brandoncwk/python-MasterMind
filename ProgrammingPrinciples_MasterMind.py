import random

# Welcome Menu/ Intro Screen function
def WelcomeMenu():
    print("   ")
    # Title
    print("//// WELCOME TO MASTER MIND")
    print("___________________________")
    print("   ")
    # Navigator menu
    print("NAVIGATOR:")
    print("___________________________")
    print("   ")
    print("Input a number to begin: ")
    print("1. Play MasterMind")
    print("2. More on how to play MasterMind")
    print("   ")
    print("Press any other key to quit")
    
    print("   ")
    # Capture string user input
    Selection = str(input("Input: "))
    # Converts user input to lower case and removes spaces
    SelectionLower = Selection.lower()
    SelectionLowerStripped = SelectionLower.strip()
    
    # User selection: 1 = run MasterMind; 2 = Look at how to play; anything else quits game
    if SelectionLowerStripped == str(1):
        NewGame()
    elif SelectionLowerStripped == str(2):
        Instructions()
    else:
        print("___________________________")
        print("   ")
        print("Aww... We're sorry to see you go! Do come back soon!")
        # Prompt user to play again when they're ready
        PlayAgain()

# Simple instructions function
def Instructions():
    print("   ")
    print("INSTRUCTIONS")
    print("___________________________")
    print("   ")
    print("1. I will make a secret list of four colors selected from the list of available colors")
    print("2. You will have to guess what colors I've chosen by typing your guesses out in sequence when prompted")
    print("3. If your color guess is spot-on, I'll say 'Match!'")
    print("4. If your color guess is in my list, but not in the right place, I'll say 'Close!'")
    print("5. If your color guess is not in my list at all, I'll say 'Nope!'")
    print("6. Get a full set of matches to win the game!")
    print("   ")
    print("___________________________")
    print("   ")
    # Press any key to exit and return to main menu
    a = input('Enter any key to return to the main menu: ')
    if a:
        WelcomeMenu()
    
# New game function to start a new round of Master Mind
def NewGame():

    # List of available colors
    AvailableColorsList = ['red', 'brown', 'orange', 'yellow', 'pink', 'cyan', 'green', 'lime', 'white']     

    # Brief instructions
    print("___________________________")
    print("   ")
    print("Master Mind is a fun puzzle game!")
    print("I will list four colors in secret from the list below.")
    print("Your job is to guess the correct colors in the correct sequence.")
    print("I'll let you know how many of your color guesses are a perfect MATCH or CLOSE.")
    print("You'll get a NOPE from me, if your color choice is totally off.")
    print("Exciting prizes await! If you're ready, let's begin!")
    print("   ")
    print("Choose four colors in sequence from the following list: ")
    print("   ")
    # Display available colors to player
    print(AvailableColorsList)

    # Generates four random colors from AvailablecColors list
    GeneratedColors = random.sample(AvailableColorsList, 4)

    # Display generated colors for presentation purposes
    print("   ")
    print("Demo Purposes", GeneratedColors)

    # Loop counter to count number of tries needed to win
    LoopCounter = 0
    # List for storing user's color choices
    StoredInput = []

    # Loop continues so long as a perfect match isnt generated
    while "Close!" or "Nope!" in ReturnResults:

        # Appends StoredInput list with user's color choices (lower case, remove spaces)
        print("   ")    
        for i in range(4):
            InputText = input(str("Enter a color: "))
            UserInputLower = InputText.lower()
            UserInputLowerStripped = UserInputLower.strip()

            StoredInput.append(UserInputLowerStripped)

        # Display's list of user's color choices    
        StoredInput

        # New list generated comparing list of StoredInput vs GeneratedColors
        ReturnResults = []    

        # For each index item: return MATCH if perfect; CLOSE if color choice in GeneratedColors; NOPE if neither
        if GeneratedColors[0] == StoredInput[0]:
            ReturnResults.append("Match!")
        elif GeneratedColors[0] in StoredInput and GeneratedColors[0] != StoredInput[0]:
            ReturnResults.append("Close!")
        elif StoredInput[0] not in GeneratedColors or AvailableColorsList:
            ReturnResults.append("Nope!")

        if GeneratedColors[1] == StoredInput[1]:
            ReturnResults.append("Match!")
        elif GeneratedColors[1] in StoredInput and GeneratedColors[1] != StoredInput[1]:
            ReturnResults.append("Close!")
        elif StoredInput[1] not in GeneratedColors or AvailableColorsList:
            ReturnResults.append("Nope!")

        if GeneratedColors[2] == StoredInput[2]:
            ReturnResults.append("Match!")
        elif GeneratedColors[2] in StoredInput and GeneratedColors[2] != StoredInput[2]:
            ReturnResults.append("Close!")
        elif StoredInput[2] not in GeneratedColors or AvailableColorsList:
            ReturnResults.append("Nope!")

        if GeneratedColors[3] == StoredInput[3]:
            ReturnResults.append("Match!")
        elif GeneratedColors[3] in StoredInput and GeneratedColors[3] != StoredInput[3]:
            ReturnResults.append("Close!")
        elif StoredInput[3] not in GeneratedColors or AvailableColorsList:
            ReturnResults.append("Nope!")

        # Counts +1 attempt before generating results
        LoopCounter += 1

        # Displays list of results of player guesses
        print("___________________________")
        print("   ")
        print("Guess : ", StoredInput)
        print("   ")
        # MATCH and CLOSE ounter for player's results
        ReturnResults.count("Match!")
        ReturnResults.count("Close!")

        # Display summary of player's results
        
        print("Results: ", ReturnResults)
        print("   ")
        print("Correct colors in the correct place: ",ReturnResults.count("Match!"))
        print("Correct colors but in the wrong place: ",ReturnResults.count("Close!"))
        print("   ")
        print("___________________________")

        # If perfect score, display congratulations message and guesses needed
        if GeneratedColors == StoredInput:
            print("   ")
            print("Congratulations! You're a MasterMind!")
            print("Tries you took to get the correct answer: ", LoopCounter)
            
            #Break loop
            break

        # Reset ReturnResults and StoredInput lists for new loop if not a perfect score
        ReturnResults.clear()
        StoredInput.clear()


    # Generate random prize for winner and round conclusion message
    AvailableExcitingPrizes = ['A BRAND NEW CAR!!!', 'A HOLIDAY IN SPAIN!!!', 'A TRIP TO ITALY!!!', 'A JETSKI!!!', '$1,000,000 IN DOGECOIN!!!', '$1,000,000 IN BITCOIN!!!', 'A CRUISE IN THE CARRIBBEANS!!!']
    ExcitingPrize = random.choice(AvailableExcitingPrizes)

    print("You have won ", ExcitingPrize, "Wow!")
    print("   ")
    print("Thanks for playing!")

    #Prompt user if they want to play again or exit
    PlayAgain()

# Prompt user if they want to play every time a game ends. 
def PlayAgain():
    # Input '1' to start new game, else return to main menu
    print("___________________________")
    print("   ")
    print("Do you want to play again? Input '1' to start a new game.")
    print("Input anything else to return to the main menu.")
    print("   ")
    PlayAgain = str(input("What would you like to do?: "))
    PlayAgainLower = PlayAgain.lower()
    PlayAgainLowerStripped = PlayAgainLower.strip()
    if PlayAgainLowerStripped == str(1):
        NewGame()
    else:
        WelcomeMenu()

# Execute program
WelcomeMenu()
