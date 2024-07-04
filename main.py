import time
import sys

#Advanced de
def delayedPrint(string, int):
    print(string)
    time.sleep(int)


playerChoice = ""


#Player choice
def choice():
    global playerChoice
    playerChoice = input("Enter your choice (1 or 2):\n--> ")
    playerChoice = int(playerChoice)


#Check player choice
def check():
    while True:
        if playerChoice in range(1,3):
            print(" ", end=" ")
            break

        else:
            print("your input is incorrect")
            choice()


#Animation function
def animate():
    for i in range(1,6):
        sys.stdout.write('\rGame is loading |')
        time.sleep(0.1)
        sys.stdout.write('\rGame is loading /')
        time.sleep(0.1)
        sys.stdout.write('\rGame is loading -')
        time.sleep(0.1)
        sys.stdout.write('\rGame is loading \\')
        time.sleep(0.1)
    sys.stdout.write('\rGame loaded successfully!')
    time.sleep(1)
    sys.stdout.write('\r ')
    

#Starting code
delayedPrint("===== Welcome to \"TITAN'S HOLLOW QUEST\" Game =====", 0.7)
delayedPrint("======== This game fully made py Adham ========", 1)
print(" ")
input("Press (Enter) to start game")
delayedPrint("===================================", 1)


animate()


#Game:

