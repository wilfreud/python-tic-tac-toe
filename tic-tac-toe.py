from subprocess import run
from random import choice
from popGUI import screenMSG

# Set of positions
toe = {
    'L1':' ',
    'M1':' ',
    'R1':' ',
    'L2':' ',
    'M2':' ',
    'R2':' ',
    'L3':' ',
    'M3':' ',
    'R3':' '
}

# Pseudo-randon first player choose
toe['M2'] = choice(['X', 'O'])
if toe['M2'] == 'X':
    p1, p2 = ('Player 2', 'O'), ('Player 1', 'X')
else:
    p1, p2 = ('Player 1', 'X'), ('Player 2', 'O')

def toeDisplay(): # Function for toe display
    for _ in toe:
        print(f"[{toe[_]}]", end=" ")
        if _ == 'R1' or _ == 'R2' or _ == 'R3': print()

# Displaying Infos
def infoDisplay():
    run('cls', shell=True)
    print(f"Order:  {p1[0]}   {p2[0]}")
    
    # Notes
    print("""NOTES:
        The first player will be chosen randomly
        This is the configuration of the board
            [L1] [M1] [R1]
            [L2] [M2] [R2] 
            [L3] [M3] [R3]
        Requirements: A little abstraction in your mind <3
                      Make sure to use ONLY the notation shown above!
                      Player 1 has 'X' and player 2 has 'O'
                      Press 'CTRL + C' to end the game
                      """)
                      
    toeDisplay()
    print()
infoDisplay()

inList = ['M2'] # This list contains the cases already filled during the game

def ruleList():
    resuList = {
        1 : (toe['L1'], toe['L2'], toe['L3']) != (" ", " ", " ") and (toe['L1'] == toe['L2'] == toe['L3']),
        2 : (toe['M1'], toe['M2'], toe['M3']) != (" ", " ", " ") and (toe['M1'] == toe['M2'] == toe['M3']),
        3 : (toe['R1'], toe['R2'], toe['R3']) != (" ", " ", " ") and (toe['R1'] == toe['R2'] == toe['R3']),
        4 : (toe['L1'], toe['M1'], toe['R1']) != (" ", " ", " ") and (toe['L1'] == toe['M1'] == toe['R1']),
        5 : (toe['L2'], toe['M2'], toe['R2']) != (" ", " ", " ") and (toe['L2'] == toe['M2'] == toe['R2']),
        6 : (toe['L3'], toe['M3'], toe['R3']) != (" ", " ", " ") and (toe['L3'] == toe['M3'] == toe['R3']),
        7 : (toe['L1'], toe['M2'], toe['R3']) != (" ", " ", " ") and (toe['L1'] == toe['M2'] == toe['R3']),
        8 : (toe['R1'], toe['M2'], toe['L3']) != (" ", " ", " ") and (toe['R1'] == toe['M2'] == toe['L3'])
    }
    # Victory rules & return True when one is true
    for i in resuList:
        if resuList[i] == True: return "EOG"

role_log = [] # This list is like a log of the game. Contains the order in which players played

thisScript = __file__.replace('\\', '/').split('/')[-1]  # Gets curent file name

def exitCheck(tourCount0): # This function checks the condition for a game TIE
    exitCode = ruleList()
    if exitCode == "EOG":
        screenMSG(thisScript, role_log[-1])
    elif tourCount0 == 7: 
        screenMSG(thisScript)

# Filling the board
def playInput(message, markk, tourCount): # Function for player input
    exitCheck(tourCount)

    while True: # To make sure the playe will input ONLY an allowed value

        try: # This is for handling CTRL+C Keyboard Interruption
            x = input(f"{message}: ").upper()
        except KeyboardInterrupt:
            print("\n\tYou ended the game!")
            quit()

        try:
            toe[x]
            if x in inList:
                print(x, "Case not empty. Choose another")
            else: 
                inList.append(x)
                break
        except KeyError:
            print("Use the defined notation to refer to board cases")
        
    toe[x] = markk
    role_log.append(message)
    infoDisplay()

playcount = 0 # This variable simply counts the rounds

for _ in range(4): # Calling 'Input' function for each player
    playInput(p1[0].capitalize(), p1[1], playcount)
    playcount += 1
    playInput(p2[0].capitalize(), p2[1], playcount)
    playcount += 1
