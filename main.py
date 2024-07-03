import time

#Delay function
# def delayedPrint(string):
#     print(string)
#     time.sleep(5)


#Just making it more customizable
def delayedPrint(string, int):
    print(string)
    time.sleep(int)


#Starting code
delayedPrint("===== Welcome \"THE LOST ARTIFACT\" Game =====", 0.7)
delayedPrint("== This game fully made py Adham ==", 1)
print(" ")
input("Press (Enter) to start game")
delayedPrint("===================================", 1)

