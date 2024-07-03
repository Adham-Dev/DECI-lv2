import time
import sys

playerChoice = ""


#Delay function
# def delayedPrint(string):
#     print(string)
#     time.sleep(5)

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



#Just making it more customizable
def delayedPrint(string, int):
    print(string)
    time.sleep(int)


#Animation function
def animate():
    for i in range(1,10):
        sys.stdout.write('\rGame is loading |')
        time.sleep(0.1)
        sys.stdout.write('\rGame is loading /')
        time.sleep(0.1)
        sys.stdout.write('\rGame is loading -')
        time.sleep(0.1)
        sys.stdout.write('\rGame is loading \\')
        time.sleep(0.1)
    sys.stdout.write('\rGame loaded successfully!')
    print(" ---------------------------- ")


#Starting code
delayedPrint("===== Welcome \"THE LOST ARTIFACT\" Game =====", 0.7)
delayedPrint("== This game fully made py Adham ==", 1)
print(" ")
input("Press (Enter) to start game")
delayedPrint("===================================", 1)


animate()

