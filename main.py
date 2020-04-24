import faker
import mysql.connector as mysql
import MatchDetails

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

cursor.execute("SELECT * FROM MatchDetails")

matches = cursor.fetchall()

for match in matches:
    m = MatchDetails.MatchDetails(match[0],match[1],match[2],match[3],match[4],match[5])
    print(m)