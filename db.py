import psycopg2

conn = psycopg2.connect(
                    database="Frespo",
                    user="postgres",
                    password="88482",
                    host="localhost",
                    port="5432"
)

curr=conn.cursor()
curr.execute("select * from playlists;")
rows=curr.fetchall()
for row in rows:
    print(row)
curr.close()
conn.close()
# print("connection established")