import sys, subprocess

class player:
    def __init__(self, name,  number, point):
        self.num = number
        self.point = point
        self.name = name

def clearconsole():
    os = sys.platform
    if os == 'linux' or 'darwin':
        command = 'clear'
    elif os == 'win32':
        command = 'cls'
    subprocess.run(command, shell = True)

class game:
    def _init_(self, Ante = 0, ):
        self.Ante = Ante
        self.mainpot = Ante

def Table():
    print ("This is Game")

def checkstatus(Players):
    for identity in Players:
        print("Player",identity.name,"Num.",identity.num,"point: ",identity.point)

Playercount = int(input("Please input number of players: "))
Players =  ["x"] * Playercount
startpoints = int(input("Please enter start money: "))

for Playernum in range(Playercount):
    print(f"Please put Name of player{Playernum}: ")
    name = input()
    Players[Playernum] = player(name, Playernum, startpoints)

input("Enter to continue")
clearconsole()
checkstatus(Players)
