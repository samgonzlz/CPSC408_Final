from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
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

    conn.close()

    return render_template('index.html', products=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
