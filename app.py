
from tkinter import INSERT
from flask import Flask, flash, render_template, request, url_for, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '15411005'
app.config['MYSQL_DB'] = 'mysql'

mysql= MySQL (app)

@app.route ('/')
def index():
   return render_template ('index.html')

@app.route ('/addcontact', methods=['POST'])
def EDIT_CONTACT():
   if request.method == 'POST':
      name = request.form ['name']
      email = request.form ['email']
      cur= mysql.connection.cursor()
      cur.execute('INSERT INTO mysql.clientes (name, email) VALUES (%s, %s)',(name, email))
      mysql.connection.commit()
      flash("Contact add succefully")
      return redirect(url_for('index'))

if __name__ == '__main__':
   app.run(host='192.168.100.158', port=8000, debug=True)

    
