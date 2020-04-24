import faker
import mysql.connector as mysql
import MatchDetails
import random
import time
import sys

if len(sys.argv) != 2:
    print("Incorrect Usage.\nTry: python Generate_Match.py <output file name>")
    exit()

fake = faker.Faker()


creds = []
with open('creds') as file:
    data = file.read()
    creds = data.split('\n')

db = mysql.connect(
    host = creds[0],
    user = creds[1],
    passwd = creds[2]
)

cursor = db.cursor()
cursor.execute("USE Assignment3")

# get maps
cursor.execute("SELECT MapID FROM Maps")
maps = cursor.fetchall()
for i in range(len(maps)):
    maps[i] = int(maps[i][0])


# get characters
cursor.execute("SELECT HeroID FROM Heroes")
heroes = cursor.fetchall()
for i in range(len(heroes)):
    heroes[i] = int(heroes[i][0])


# get weapons
cursor.execute("SELECT WeaponID FROM Weapons")
weapons = cursor.fetchall()
for i in range(len(weapons)):
    weapons[i] = int(weapons[i][0])


# Create Match Details
fakeMap = maps[random.randint(0,len(maps)-1)]
fakeWin = bool(random.randint(0,1))
fakeRoundsWon = 0
fakeRoundsLost = 0
if fakeWin:
    fakeRoundsWon = 13
    fakeRoundsLost = random.randint(0,12)
else:
    fakeRoundsLost = 13
    fakeRoundsWon = random.randint(0,12)
fakeDate = fake.date()

matchDetails = MatchDetails.MatchDetails(2,fakeMap,fakeWin,fakeRoundsWon,fakeRoundsLost,fakeDate)


scoreboard = []
for i in range(10):
    scoreboard.append([fake.user_name(),heroes[random.randint(0,len(heroes)-1)],random.randint(100,340),random.randint(0,30),random.randint(0,25),random.randint(0,10),random.randint(30,100),random.randint(0,10),random.randint(0,5),random.randint(0,5)])

performance = []
for i in range(5):
    performance.append([scoreboard[i*2][0],random.randint(0,8),random.randint(0,8),random.randint(0,3)])

timeline = []
for i in range(fakeRoundsWon + fakeRoundsLost):
    timeline.append([i+1,random.randint(0,500),random.randint(0,5),random.randint(0,2),random.randint(0,1),random.randint(0,43)*100,weapons[random.randint(0,len(weapons)-1)],random.randint(0,1)])

o = open(sys.argv[1],'w')

o.write('Match Details\n')
o.write('Map,Win,RoundsWon,RoundsLost,Date\n')
o.write(str(matchDetails.Map) + ',' + str(int(matchDetails.Win)) + ',' + str(matchDetails.RoundsWon) + ',' + str(matchDetails.RoundsLost) + ',' + str(matchDetails.Date) + '\n')
o.write('\n')
o.write('Scoreboard\n')
o.write('PlayerName,Hero,AVGCombatScore,Kills,Deaths,Assists,EconRating,FirstBloods,Plants,Defuses\n')
for elem in scoreboard:
    o.write(str(elem[0]) + ',' + str(elem[1]) + ',' + str(elem[2]) + ',' + str(elem[3]) + ',' + str(elem[4]) + ',' + str(elem[5]) + ',' + str(elem[6]) + ',' + str(elem[7]) + ',' + str(elem[8]) + ',' + str(elem[9]) + '\n')
o.write('\n')
o.write('Performance\n')
o.write('PlayerName,Kills,Deaths,Assists\n')
for elem in performance:
    o.write(str(elem[0]) + ',' + str(elem[1]) + ',' + str(elem[2]) + ',' + str(elem[3]) + '\n')
o.write('\n')
o.write('Timeline\n')
o.write('RoundNum,Score,Kills,Assists,Died,MoneySpent,Weapon,Won\n')
for elem in timeline:
    o.write(str(elem[0]) + ',' + str(elem[1]) + ',' + str(elem[2]) + ',' + str(elem[3]) + ',' + str(elem[4]) + ',' + str(elem[5]) + ',' + str(elem[6]) + ',' + str(elem[7]) + '\n')


o.close()