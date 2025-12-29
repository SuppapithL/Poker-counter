class player:
    def _init_(self, name,  number, point):
        self.num = number
        self.point = point
        self.name = name
class game:
    def _init_(self, Ante = 0):
        self.Ante = Ante
Playercount = int(input("Please input number of players:"))
Players =  ["x"] * Playercount
startpoints = int(input("Please enter start money:"))
Ante = int(input("Please enter Ante of this round:"))
for Playernum in range(Playercount):
    name = input("Please put Name of player")
    Players[Playernum] = player(name, Playernum, startpoints)
    input("Enter to continue")
    table()
def Table():
    print ("This is Game")
