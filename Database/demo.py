import MySQLdb

db = MySQLdb.connect(host="db4free.net",    # your host, usually localhost
                     user="transfer",         # your username
                     passwd="jazz3010",  # your password
                     db="transfer")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
#cur.execute("""INSERT INTO main (name, mobile, extra, abc) VALUES (%s,%s,%s,%s)""", (1,2,3,4))
cur.execute("""SELECT * FROM user""")
#db.commit()


# print all the first cell of all the rows
for row in cur.fetchall():
    print(row[0])

db.close()
