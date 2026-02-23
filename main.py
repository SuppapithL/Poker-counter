import sys, subprocess
import random

class player:
    def __init__(self, name,  number, point):
        self.num = number
        self.point = point
        self.name = name

    def playerinfo(self):
        return f"Num: {self.num},Name: {self.name},Point: {self.point}"

    def updateinfo(self, newpoint):
        self.point = newpoint

class Table:
    def __init__(self, players):
        self.players = players
        self.pot = 0
        self.turn_index = 0
        self.dealer = random.choice(players)
    
    def tableinfo(self):
        package = []
        for player in self.players:
            package.append(f"Num: {player.num},Name: {player.name},Point: {player.point},Dealer: {player == self.dealer}")
        return package

def clearconsole():
    os = sys.platform
    if os in ('linux', 'darwin'):
        command = 'clear'
    elif os == 'win32':
        command = 'cls'
    subprocess.run(command, shell = True)

def Lobby(Players):
    clearconsole()
    print ("This is Lobby!\nPlayers information:")
    for identity in Players:
        print(identity.playerinfo())
    staged = input("Please enter number of the player that will join(x,y,...):").split(",")
    Joined = []
    for Nums in staged:
        if int(Nums) < len(staged) + 1:
            Joined.append(Players[int(Nums)])
    clearconsole()
    Tables(Joined)

def Setup():
    Playercount = int(input("Please input number of players: "))
    Players =  {}
    Playerlist = []
    startpoints = int(input("Please enter start money: "))
    for Playernum in range(Playercount):
        print(f"Please put Name of player{Playernum}: ")
        name = input()
        Players[Playernum] = player(name, Playernum, startpoints)
    clearconsole()
    for identity in Players.values():
        Playerlist.append(identity)
    for identity in Playerlist:
        print(identity.playerinfo())
    input("Enter to continue if information is correct.If not, control c to cancle")
    return Playerlist

def Tables(Joined):
    clearconsole()
    Tabl = Table(Joined)
    print("This is Table, Joined player:")
    for element in Tabl.tableinfo():
        print(element)

def main():
    Players = Setup()
    Lobby(Players)

main()
