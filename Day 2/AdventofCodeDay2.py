class BagGame:
    def __init__(self, gameNumber, roundList):
        self.gameNumber = gameNumber
        self.roundList = roundList
        self.maxBlue = 0
        self.maxRed =  0
        self.maxGreen = 0

class GameRound:
    def __init__(self, blue, red, green):
        self.blue = blue
        self.red = red
        self.green = green

allGames = []
lineWoutN = []

with open("day2input", "r") as gameInfo:
    lines = gameInfo.readlines()

    for i in lines:
        lineWoutN.append(i.replace("\n", ""))

#print(lineWoutN)

for j in lineWoutN:
    roundListInput = []
    colonPlacement = j.find(":")
    gameID = j[5:int(colonPlacement)]
    j = j.split(":")
    j = j[1]
    j = j.split(";")
    for rounds in j:
        blueInput = 0
        redInput = 0
        greenInput = 0
        if rounds.find("blue") != -1:
            blueInput = rounds[rounds.find("blue") - 3:rounds.find("blue") - 1]
        if rounds.find("red") != -1:
            redInput = rounds[rounds.find("red") - 3:rounds.find("red") - 1]
        if rounds.find("green") != -1:
            greenInput = rounds[rounds.find("green") - 3:rounds.find("green") - 1]
        gameRound = GameRound(int(blueInput), int(redInput), int(greenInput))
        roundListInput.append(gameRound)
    bagGame = BagGame(int(gameID), roundListInput)
    allGames.append(bagGame)

for games in allGames:
    blueMax = 0
    redMax = 0
    greenMax = 0
    for rounds in games.roundList:
        if(rounds.blue > blueMax):
            blueMax = rounds.blue
        if(rounds.red > redMax):
            redMax = rounds.red
        if(rounds.green > greenMax):
            greenMax = rounds.green
    games.maxBlue = blueMax
    games.maxRed = redMax
    games.maxGreen = greenMax

sum = 0
for games in allGames:
    redCubes = 12
    greenCubes = 13
    blueCubes = 14
    if games.maxRed <= redCubes and games.maxGreen <= greenCubes and games.maxBlue <= blueCubes:
        sum = sum + games.gameNumber

print(f"Game sum of the ID's is {sum}")

powerSum = 0
for games in allGames:
    powerSum = powerSum + (games.maxBlue*games.maxRed*games.maxGreen)

print(f"Sum of power of the game sets = {powerSum}")

print(f"Sum of power of the game sets = {powerSum}")
