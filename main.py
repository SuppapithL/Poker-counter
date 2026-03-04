import sys, subprocess
import random

class playerinit:
    def __init__(self, name,  number, point):
        self.num = number
        self.point = point
        self.name = name

    def playerinfo(self):
        return f"Num: {self.num},Name: {self.name},Point: {self.point}"

    def updatepoint(self, newpoint):
        self.point = newpoint
    
    def updatename(self, newname):
        self.name = newname

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
        clearconsole()
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
    rawplayers = []
    players = []
    while True:
        clearconsole()
        print(f'This is Player setup!\nCurrent players:')
        for identity in players:
            print(identity.playerinfo())
        print()
        command = input("a: add player\nr: remove player\nu: update player's information\nc: continue\nq: quit\nPlease enter your command:".lower())
        match command:
            case "a":
                players = addplayer(players)
            case "r":
                players = removeplayer(players)
            case "u":
                players = updateinfo(players)
            case "c":
                break
            case "q":
                exit()
            case _:
                input("Invalid command please try again") 
    return players

def addplayer(players):
    clearconsole() 
    print("This is add player!") 
    Name = input("Please enter player name:")
    Point = get_int("Please enter player starting point:")
    allindex = []
    for identity in players:
        allindex.append(identity.num)
    index = max([0]+allindex) + 1
    Player = playerinit(Name, index, Point)
    players.append(Player)
    return players

def removeplayer(players):
    while True:
        clearconsole()
        print("select players you want to remove!:")
        for identity in players:
            print(identity.playerinfo())
        command = int(input("enter player number who want to me removed or ""0"" to return:"))
        if command == 0:
            return players
        for number in players:
            if number.num == command:
                confirm = input(f"Do you want to remove player {number.name}? Y/N").lower()
                if confirm == "y":
                    players.remove(number)
                    return players
                elif confirm == "n":
                    return removeplayers(players)
        input("Invalid number, please try again")

def updateinfo(players):
    numbers = []
    for identity in players:
        numbers.append(identity.num)
    while True:
        clearconsole()
        for gamer in players:
            print(gamer.playerinfo())
        command = input("please enter number of player to update:")
        if command in numbers:
            while True:
                clearconsol()
                for player in players:
                    if player.num == command:
                        realplayer = player
                print("This is Player information:")
                print(player.playerinfo())
                print("p for point update, n for name update, q to quit")
                choice = input("Please choose that wanted to change:").lower()
                if choice == "p":
                    newpoint = int(input("Please enter new point:"))
                    player.updatepoint(newpoint)
                elif choice == "n":
                    newname = int(input("Please enter new name:"))
                    player.updatepoint(newname)
                elif choice == "q":
                    break
                else:
                    input("invalid input. Please try again")
        else:
            input("invalid input. Please try again")

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
