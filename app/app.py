from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
from flask_mysqldb import MySQL
import sys

mysql = MySQL()
app = Flask(__name__)

try:
    app.config['MYSQL_HOST'] = sys.argv[1]
except:
    app.config['MYSQL_HOST'] = '127.0.0.1'
    app.config['MYSQL_PORT'] = 13306

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'tel_dir'
mysql.init_app(app)

@app.route("/")
def hello():
 return 'Hallo Benutzer Willkommen!. Please  check /tel_dir for telephone directory details'

@app.route("/tel_dir")
def index():
 cur = mysql.connection.cursor()
 cur.execute("SELECT * from details")
 rows = cur.fetchall()
 mysql.connection.commit()
 return render_template('test_table.html', table=rows)

if __name__=="__main__":
 app.run(
#  host="0.0.0.0",
#  port=5000
)
