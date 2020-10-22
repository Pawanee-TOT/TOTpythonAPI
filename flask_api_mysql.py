from flask import Flask, request, jsonify
import mysql_lib 
app = Flask(__name__)

@app.route('/all', methods=['GET']) 
def all():
    result = db_get_all()
    return jsonify(result)

def db_get_all():
    mysql_lib.connect()
    sql = "select * from source"
    data = mysql_lib.select(sql)
    mysql_lib.close()
    return data

#if __name__ == '__main__':
    #app.run(debug=True, port=80, host='0.0.0.0')

#SelectByid
@app.route('/by_id', methods=['GET']) 
def by_id():
    data = request.args
    id = data["id"]
    result = db_get_by_id(id)
    return jsonify(result)

def db_get_by_id(id):
    mysql_lib.connect()
    sql = "select * from source where id={}".format(id)
    print(sql)
    data = mysql_lib.select(sql)
    mysql_lib.close()
    return data

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')