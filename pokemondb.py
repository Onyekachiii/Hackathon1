import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Splendour01%'
DATABASE = 'Pokemon'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)

cursor = connection.cursor()

cursor.execute("SELECT * FROM players LIMIT 30;")

results = cursor.fetchall()

print(results)

connection.close()