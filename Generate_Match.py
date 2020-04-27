# Matthew Parnham

import faker
import mysql.connector as mysql
import MatchDetails
import random
import sys

# cmd args check
if len(sys.argv) != 3:
    print("Incorrect Usage.\nTry: python Generate_Match.py <output file name (csv)> <Match Count>")
    exit()

filePath = sys.argv[1]
matchCount = int(sys.argv[2])
#instantiate faker
fake = faker.Faker()

# Open credentials file and store credentials as variables
creds = []
with open('creds') as file:
    data = file.read()
    creds = data.split('\n')

# Connect to DB
db = mysql.connect(
    host = creds[0],
    user = creds[1],
    passwd = creds[2],
    database = 'Assignment3'
)

cursor = db.cursor()

# Function to get IDs from a table that contains a column of IDs and the names that match. e.g. Maps(MapID, MapName)
# We need a list of the IDs so that our fake data uses valid IDs
def getIDs(query):
    cursor.execute(query)
    output = cursor.fetchall()
    for i in range(len(output)):
        output[i] = int(output[i][0])
    return output

# get maps
maps = getIDs("SELECT MapID FROM Maps")

# get characters
heroes = getIDs("SELECT HeroID FROM Heroes")

# get weapons
weapons = getIDs("SELECT WeaponID FROM Weapons")

o = open(sys.argv[1], 'w')

o.write('Map,Win,RoundsWon,RoundsLost,Date,Scoreboard,Performance,Timeline\n')

for z in range(matchCount):
    # Create Match Details
    fakeMap = maps[random.randint(0,len(maps)-1)]
    fakeWin = bool(random.randint(0,1))
    fakeRoundsWon = 0
    fakeRoundsLost = 0
    # One team must reach 13 to win and with 25 total rounds, the losing team will have between 0 and 12 rounds
    if fakeWin:
        fakeRoundsWon = 13
        fakeRoundsLost = random.randint(0,12)
    else:
        fakeRoundsLost = 13
        fakeRoundsWon = random.randint(0,12)
    fakeDate = fake.date()

    matchDetails = MatchDetails.MatchDetails(2,fakeMap,fakeWin,fakeRoundsWon,fakeRoundsLost,fakeDate)

    # Generate Fake scoreboard entries
    scoreboard = []
    for i in range(10):
        scoreboard.append([fake.user_name(),heroes[random.randint(0,len(heroes)-1)],random.randint(100,340),random.randint(0,30),random.randint(0,25),random.randint(0,10),random.randint(30,100),random.randint(0,10),random.randint(0,5),random.randint(0,5)])

    # Generate fake performance entries
    performance = []
    for i in range(5):
        performance.append([scoreboard[i*2][0],random.randint(0,8),random.randint(0,8),random.randint(0,3)])

    # Generate fake timeline entries
    timeline = []
    for i in range(fakeRoundsWon + fakeRoundsLost):
        timeline.append([i+1,random.randint(0,500),random.randint(0,5),random.randint(0,2),random.randint(0,1),random.randint(0,43)*100,weapons[random.randint(0,len(weapons)-1)],random.randint(0,1)])

    o.write(str(matchDetails.Map) + ',' + str(int(matchDetails.Win)) + ',' + str(matchDetails.RoundsWon) + ',' + str(matchDetails.RoundsLost) + ',' + str(matchDetails.Date) + ',')
    o.write('"')
    for elem in scoreboard:
        o.write(str(elem[0]) + ',' + str(elem[1]) + ',' + str(elem[2]) + ',' + str(elem[3]) + ',' + str(elem[4]) + ',' + str(elem[5]) + ',' + str(elem[6]) + ',' + str(elem[7]) + ',' + str(elem[8]) + ',' + str(elem[9]) + '\n')
    o.write('","')
    for elem in performance:
        o.write(str(elem[0]) + ',' + str(elem[1]) + ',' + str(elem[2]) + ',' + str(elem[3]) + '\n')
    o.write('","')
    for elem in timeline:
        o.write(str(elem[0]) + ',' + str(elem[1]) + ',' + str(elem[2]) + ',' + str(elem[3]) + ',' + str(elem[4]) + ',' + str(elem[5]) + ',' + str(elem[6]) + ',' + str(elem[7]) + '\n')
    o.write('"\n')
o.close()