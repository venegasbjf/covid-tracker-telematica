from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import os, pymysql

# initializations
app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = os.getenv('dbHOST')
app.config['MYSQL_USER'] = os.getenv('dbUSER')
app.config['MYSQL_PASSWORD'] = os.getenv('dbPASSWORD')
app.config['MYSQL_DB'] = os.getenv('dbNAME')
mysql = MySQL(app)

# Mysql Connection
# conn = pymysql.connect(
#             host=os.getenv('dbHOST'),
#             user=os.getenv('dbUSER'),
#             password=os.getenv('dbPASSWORD'),
#             database=os.getenv('dbNAME'),
#             cursorclass=pymysql.cursors.DictCursor
#         )
# cur=conn.cursor()



# settings
app.secret_key = "mysecretkey"

# routes
@app.route('/')
def Index():
    return "hola mundo"

"""@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contacts (fullname, phone, email) VALUES (%s,%s,%s)", (fullname, phone, email))
        mysql.connection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('Index'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-contact.html', contact = data[0])

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('Index'))"""

# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)