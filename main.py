from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import os, pymysql
from dotenv import load_dotenv, find_dotenv

# Load Enviroment Variables from .env file
load_dotenv(find_dotenv())

# initializations
app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = os.getenv('dbHOST')
app.config['MYSQL_USER'] = os.getenv('dbUSER')
app.config['MYSQL_PASSWORD'] = os.getenv('dbPASSWORD')
app.config['MYSQL_DB'] = os.getenv('dbNAME')


mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

# routes
@app.route('/')
def PagiP():
    return render_template('Pagina-principal.html')


# Modulo Administration
@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['firstName']
        lastName = request.form['lastName']
        idNumber = str(request.form['idNumber'])
        rol = request.form['rol']
        username = request.form['username']
        password = request.form['password']
        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO `Modulo administración` (Nombres,Apellidos,Cédula,Rol,Usuario,Contraseña) VALUES(%s,%s,%s,%s,%s,%s)',
        (name,lastName,idNumber,rol,username,password))
        mysql.connection.commit()

        return redirect(url_for('adminSuccess'))

@app.route('/admin_success')
def adminSuccess():
    return render_template('admin-success.html')
# END Modulo Administration

# Modulo Registro caso
@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/add_case', methods=['POST'])
def add_case():
    if request.method == 'POST':
        name = request.form['firstName']
        lastName = request.form['lastName']
        idNumber = str(request.form['idNumber'])
        Sexo = request.form['Sexo']
        FechaNacimiento = request.form['Fecha de nacimiento']
        DireccionResidencia = request.form['Direccion de residencia']
        DireccionTrabajo = request.form['Direccion trabajo']
        ResultadoExamen = request.form['ResultadoExamen']
        FechaExamen = request.form['Fecha examen']

        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO `Registro de Caso` (Nombres,Apellidos,Cédula,Sexo,Fecha de nacimiento,Dirección de residencia,Dirección Trabajo,Resultado Examen,Fecha examen) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
        (name,lastName,idNumber,Sexo,FechaNacimiento,DireccionResidencia,DireccionTrabajo,ResultadoExamen,FechaExamen))
        mysql.connection.commit()

        return redirect(url_for('registroSuccess'))

@app.route('/registro_Success')
def registroSuccess():
    return render_template('registro-Success.html')
# END Modulo Registro Caso

#Modulo Visualización
@app.route('/Visual')
def Mapa():
    return render_template('Mapa.html')
# END Modulo Visualización

# Modulo Busqueda
@app.route('/Gestionar')
def editar():
    return render_template('Gestion.html')
# END Modulo Busqueda

"""@app.route('/edit/<id>', methods = ['POST', 'GET'])
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