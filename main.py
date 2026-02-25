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

def get_int(prompt, min_val=None, max_val=None):
    while True:
        raw = input(prompt)

        try:
            value = int(raw)
        except ValueError:
            print("Invalid integer.")
            continue

        if min_val is not None and value < min_val:
            print("Too small.")
            continue

        if max_val is not None and value > max_val:
            print("Too large.")
            continue

        return value

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
    while True:
        clearconsole()
        Playercount = get_int("Please input number of players:",0, 10)
        clearconsole()
        confirmation = input(f"There will be {Playercount} players in this game.\nEnter r or R to reset, any key to confirm:").lower()
        if confirmation != "r":
            break
    clearconsole()
    Players =  {}
    Playerlist = []
    startpoints = int(input("Please enter start money: "))
    for Playernum in range(Playercount):
        name = input(f"Please put Name of player{Playernum}: ")
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
