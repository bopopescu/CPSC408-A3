import mysql.connector as mysql
import sys
import csv

if len(sys.argv) != 2:
    print("Incorrect Usage.\nTry: python ImportCsv.py <Csv File>")
    exit()

filePath = sys.argv[1]
data = list(csv.reader(open(filePath)))

matchDetails = data[2]
scoreboard = data[6:16]
performance = data[19:24]
roundCount = int(matchDetails[2]) + int(matchDetails[3])
timeline = data[27:27+roundCount]

creds = []
with open('creds') as file:
    data = file.read()
    creds = data.split('\n')

db = mysql.connect(
    host = creds[0],
    user = creds[1],
    passwd = creds[2],
    database = 'Assignment3'
)

cursor = db.cursor()

q = 'INSERT INTO MatchDetails(Map, Win, RoundsWon, RoundsLost, Date) VALUES (%s, %s, %s, %s, %s)'
val = (matchDetails[0],matchDetails[1],matchDetails[2],matchDetails[3],matchDetails[4])
cursor.execute(q, val)
db.commit()

cursor.execute("SELECT * FROM MatchDetails WHERE MatchID IN (SELECT MAX(MatchID) FROM MatchDetails)")

matches = cursor.fetchall()
matchID = matches[0][0]

q = 'INSERT INTO Scoreboard VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
val = []
for score in scoreboard:
    val.append((matchID,score[0],score[1],score[2],score[3],score[4],score[5],score[6],score[7],score[8],score[9]))
cursor.executemany(q,val)

q = 'INSERT INTO Performance VALUES (%s,%s,%s,%s,%s)'
val = []
for line in performance:
    val.append((matchID,line[0],line[1],line[2],line[3]))
cursor.executemany(q,val)

q = 'INSERT INTO Timeline VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
val = []
for line in timeline:
    val.append((matchID,line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]))
cursor.executemany(q,val)

db.commit()


