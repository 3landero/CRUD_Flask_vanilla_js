from ast import Return
import utils
from flask import Flask, jsonify, request, render_template

PATH_BASE_API = "/api/v1"
app = Flask(__name__)

lista_empleados = [
    {
        'id': '1',
        'nombre': 'Jhon Doe',
        'puesto': 'Full-Stack Developer'
    },
    {
        'id': '2',
        'nombre': 'Kate Doe',
        'puesto': 'Full-Stack Developer'
    }
]

@app.route(f'{PATH_BASE_API}/')
def index_api():
    data = {
        "code": 200,
        "msg": "Online"
    }
    return jsonify(data)



@app.route('/')    
def index():
    return render_template('index.html')




@app.route(f'{PATH_BASE_API}/create-tables')
def create_table():
    msg = utils.create_tables()
    resp = {"msg": msg}
    return resp



@app.route(f'{PATH_BASE_API}/user/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        data = request.json
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password = data['password']
        confirm_password = data['confirm_password']
        msg = utils.db_create_user(first_name, last_name, email, password, confirm_password)
    elif request.method == 'GET':
        msg = 'Este endpoint es para el registro de un nuevo usuario'
    return {
        "code": 200,
        "msg": msg
    }





@app.route(f'{PATH_BASE_API}/task/create/<int:user_id>', methods=['GET', 'POST'])
def create_task(user_id):
    if request.method == 'POST':
        data = request.json
        title = data['title']
        description = data['description']
        is_completed = data['is_completed']
        msg = utils.db_create_task(title, description,  is_completed,user_id)
    elif request.method == 'GET': 
        msg = 'Crea una nueva tarea'
    return {
        "code": 200,
        "msg": msg
    }

    
# TODO get task x user--------------------------------------------------------------------------------

@app.route(f'{PATH_BASE_API}/task/mytasks/<int:user_id>', methods = ['GET', 'POST'])
def get_tasks(user_id):
    if request.method == 'GET':
        msg = utils.db_get_task(user_id)
        return jsonify({msg})
    elif request.method == 'POST': 
        msg = 'consulta disponible solo con metodo GET'
    return {
        "code": 200,
        "msg": msg
    }

#-------------------------------------------------------------------------------------------------------


@app.route(f'{PATH_BASE_API}/user/get/<int:user_id>',methods = ['GET'])
def get_user(user_id):
    if request.method == 'GET':
        data = utils.db_get_user(user_id)
        return jsonify({'user':data,'mensaje':'Cliente encontrado'})
    elif request.method == 'POST':
        return  jsonify({'msg':'consulta disponible solo con metodo GET'})




if __name__ == '__main__':
    app.run(debug=True)
