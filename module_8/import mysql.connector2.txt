import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Ostrich%2020",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue. . . ")

except mysql.connector.Error as err:
        
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("*  The supplied username or password are invalid  *")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("*  The specified database does not exist  *")

    else:
                print(err)

finally:
        db.close()

cursor = db.cursor()

cursor.execute("SELECT team_id, team_name, mascot FROM team")

teams = cursor.fetchall()

print("-- DISPLAYING TEAM RECORDS --")
for team in teams:
    print("Team ID: {}".format(team[1]))
    print("Team Name: {}".format(team[2]))
    print("Mascot: {}".format(team[3]))

cursor.execute("SELECT player_id, first_name, last_name, team_id FROM players")

players = cursor.fetchall()

print("-- DISPLAYING PLAYER RECORDS --")
for team in teams:
    print("Player ID: {}".format(players[1]))
    print("First Name: {}".format(players[2]))
    print("Last Name: {}".format(players[3]))
    print("Team ID: {}".format(players[4]))

input("\n\n Press any key to continue. . . ")