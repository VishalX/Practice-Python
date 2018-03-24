""" Text based game : Rock-Paper-Scissors-Lizard-Spock """

# Import random module : Used to simulate computer input
import random

# Define a function to convert a name string to a number
def name_to_number(name):
    """
    Returns an integer representation of the input string name,
    For invalid name, returns None
    """
    if   name == "Rock"     : return 0
    elif name == "Spock"    : return 1
    elif name == "Paper"    : return 2
    elif name == "Lizard"   : return 3
    elif name == "Scissors"  : return 4
    else: return None   

# Define a function to convert a number to a name string
def number_to_name(number):
    """
    Returns an string representation of the input number
    For invalid number, returns None
    """
    if   number == 0  : return "Rock"
    elif number == 1  : return "Spock"
    elif number == 2  : return "Paper"    
    elif number == 3  : return "Lizard"
    elif number == 4  : return "Scissors"
    else : return None
    
# Define RPSLS function
def rpsls(user_input):
    """
    Prints out the winner among user and computer 
    based on following the game rules.

    Rules of "Rock-Paper-Scissors-Lizard-Spock"
    ------------------------------------------
    1. Scissors cuts Paper
    2. Paper covers Rock
    3. Rock crushes Lizard
    4. Lizard poisor Spock
    5. Spock smashes Scissors
    6. Scissors decapitates Lizard
    7. Lizard eats Paper
    8. Paper disproves Spock
    9. Spock vaporizes Rock
        & as it always has
    10. Rock crushes Scissors 
    """
    userin = name_to_number(user_input)
    # Check validity of user input
    if userin is None: 
        print("[ERROR] Invalid Input !")
        return
    
    # Get Computer input
    computerin = random.randrange(5)
    # Print User and Computer input
    print("[MESSG] User Chose     : ", user_input)
    print("[MESSG] Computer Chose : ", number_to_name(computerin))
    # Check who won
    diff = userin - computerin
    # For negative number, add 5
    if diff <= 0: diff += 5
    # Get remainder
    rem = diff % 5
    # Check for winner
    if   (rem == 1) or (rem == 2): print("[MESSG] User Won !")
    elif (rem == 3) or (rem == 4): print("[MESSG] Computer Won !")
    else : print("[MESSG] Tie !")

    ############################ End of rpsls function

# Caller
if __name__ == "__main__":
    user_inp = input("Enter your choice : ")
    # Call rpsls
    rpsls(user_inp)
