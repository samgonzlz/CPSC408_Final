import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="cpsc408",
  database='store',
  auth_plugin='mysql_native_password'
)

cur_obj = conn.cursor()

cur_obj.execute('''
    SELECT name, category,
    CAST(price AS FLOAT) AS price
    FROM products
    ''')

result = cur_obj.fetchall()

for row in result:
    print(row)

conn.close()

