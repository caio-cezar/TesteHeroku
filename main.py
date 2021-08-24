DB_HOST = 'ec2-3-237-55-151.compute-1.amazonaws.com'
DB_NAME = 'd82oi9svhlh6ha'
DB_USER = 'bogtpylknervrq'
DB_PASS = '49bff7d96b31cfcffd7c0f7417c5e8c313c4161f8626274a4dc69139f40280f9'

import psycopg2

conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST)

cur = conn.cursor()

cur.execute('INSERT INTO pessoas (nome) VALUES(%s)', ("Luciano",))

conn.commit()

cur.close()

conn.close()

# print(cur.fetchall())

# cur.close()

# conn.close()
