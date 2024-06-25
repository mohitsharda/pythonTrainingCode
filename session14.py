import mysql.connector as db
from session13 import PlayStore

# Database username and password
# username = "root"
# password + ""

# # LocalHost
# Host = "127.0.0.1"
# Database = ""

connection = db.connect(user = "root",
                        password = "656434",
                        host = "127.0.0.1",
                        database = "project",
                    )

print("CONNECTION CREATED: ")
print(connection)

playstore = PlayStore()
playstore.addPlaystoreDetail()

# 2: create sql statement
# sql = "insert into playstore values(null, 'Recommeded', 'trending', 'kids', 'premium', 'games', 'apps', 'available','books', '120000.22')"
sql = "insert into playstore values(null, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {})".format(playstore.forYou, playstore.topCharts, playstore.kids, playstore.premium, playstore.games, playstore.apps ,playstore.offers, playstore.books, playstore.wallet)

# sql = "update playstore set forYou(null, 'Recommeded', 'trending', 'kids', 'premium', 'games', 'apps', 'available','books', '120000.22')"

cursor = connection.cursor()

cursor.execute(sql)

connection.commit()

print("SQL STATEMENT EXECUTED...........")