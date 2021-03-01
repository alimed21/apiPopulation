import MySQLdb
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from flask import jsonify, make_response
from flask_cors import CORS

import yaml

app = Flask(__name__)
CORS(app)
# Configure db

db = yaml.load(open('mysql_config.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']


mysql = MySQL(app)
#Search for a person in the database using parameters
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and request.form.get('name') != '' and request.form.get('cni') != '' and request.form.get('datebirth') != '':
        # Fetch form data
        name = request.form.get('name')
        cni = request.form.get('cni')
        dateBirth = request.form.get('datebirth')
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        query = ("SELECT * FROM personne where name = '" + name + "'and cni = '" + cni + "' and brith = '" + dateBirth + "';")
        cur.execute(query)
        result = cur.fetchall()
        if len(result) > 0:
            return jsonify(result)
            #personDetails = cur.fetchall()
            #eturn render_template('person.html', personDetails=personDetails)
        else:
            #return False
            return render_template('erreur.html')

    return render_template('index.html')


#Returns the list of people

@app.route('/population', methods=['GET'])
def population():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    query = "SELECT name, cni, birth FROM person;"
    cur.execute(query)
    result = cur.fetchall()
    json = {'data': result}

    if len(result) > 0:
        return make_response(jsonify(json), 200)
    else:
        return False
        # return render_template('erreur.html')


if __name__ == '__main__':
    app.run(host='10.193.71.206')
    app.run(debug=True)
