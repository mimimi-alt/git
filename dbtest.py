import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=littlemore")
cur = conn.cursor()

cur.execute("SELECT * FROM test1;")
print(cur.fetchone())
conn.commit()
cur.close()
conn.close()
