import sys, subprocess

class player:
    def __init__(self, name,  number, point):
        self.num = number
        self.point = point
        self.name = name

    def playerinfo(self):
        return f"Num: {self.num},Name: {self.name},Point: {self.point}"

class Table:
    def __init__(self, players):
        self.players = players
        self.pot = 0
        self.community_cards = []
        self.deck = []
        self.turn_index = 0

def clearconsole():
    os = sys.platform
    if os == 'linux' or 'darwin':
        command = 'clear'
    elif os == 'win32':
        command = 'cls'
    subprocess.run(command, shell = True)

def Lobby(Players):
    clearconsole()
    print ("This is Lobby!\nPlayers information:")
    checkstatus(Players)
    staged = input("Please enter number of the player that will join(x,y,...):").split(",")
    Joined = []
    for Nums in staged:
        if int(Nums) in Players:
            Joined.append(Players[int(Nums)])
    clearconsole()
    Tables(Joined)

def checkstatus(Players):
    for identity in Players.values():
        print(identity.playerinfo())

def Setup():
    Playercount = int(input("Please input number of players: "))
    Players =  {}
    startpoints = int(input("Please enter start money: "))

    for Playernum in range(Playercount):
        print(f"Please put Name of player{Playernum}: ")
        name = input()
        Players[Playernum] = player(name, Playernum, startpoints)
    clearconsole()
    checkstatus(Players)
    input("Enter to continue if information is correct.If not, control c to cancle")
    return Players

def Tables(Joined):
    clearconsole()
    Tabl = Table(Joined)
    print("This is Table, Joined player:")
    for PPL in Joined:
        print(PPL.playerinfo())

def main():
    Players = Setup()
    Lobby(Players)

main()
