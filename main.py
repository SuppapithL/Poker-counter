class player:
    def _init_(self, name,  number, point):
        self.num = number
        self.point = point
        self.name = name
class game:
    def _init_(self, Ante
Playercount = int(input("Please input number of players"))
Players =  ["x"] * Playercount
start points = int(input("Please enter start money:"))
Ante = int(input("Please enter Ante of this round:"))
for Playernum in range(Playercount):
    name = input("Please put Name of player:",Playernum)
    Players[Playernum] = player(name, Playernum, startpoints)
    input("Enter to continue")
def Table:
    print ("This is Game")
