import utils
from flask import Flask, jsonify, request, render_template
from empleado import Empleado

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



empleados = 'http://127.0.0.1:5000/api/v1/user/get/allusers'
empleados_objects= []
for empleado in empleados:
    emp_obj = Empleado(empleado['id'],empleado['first_name'], empleado['last_name'], empleado['email'], empleado['password'] )
    empleados_objects.append(emp_obj)



#--------ROUTES MANAGING--------

#------API INDEX  http://127.0.0.1:5000/api/v1/  ------
@app.route(f'{PATH_BASE_API}/')
def index_api():
    data = {
        "code": 200,
        "msg": "Online"
    }
    return jsonify(data)


#------render INDEX HTML -------
@app.route('/')    
def index():
    return render_template('index.html')

@app.route('/registro')
def render_register():
    return render_template('form.html')


@app.route(f'{PATH_BASE_API}/create-tables')
def create_table():
    msg = utils.create_tables()
    resp = {"msg": msg}
    return resp

#------------- USER MANAGING--------------------------#

#-------- CREATE USER ---------------
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



#-------- READ USER ------------------
@app.route(f'{PATH_BASE_API}/user/get/<int:user_id>',methods = ['GET'])
def get_user(user_id):
    if request.method == 'GET':
        data = utils.db_get_user(user_id)
        return jsonify({'user':data,'mensaje':'Cliente encontrado'})
    elif request.method == 'POST':
        return  jsonify({'msg':'consulta disponible solo con metodo GET'})


@app.route(f'{PATH_BASE_API}/user/get/allusers',methods = ['GET'])
def get_all_users():
    if request.method == 'GET':
        data = utils.db_get_all_users()
        return jsonify({'user':data,'mensaje':'reporte exitoso'})
    elif request.method == 'POST':
        return  jsonify({'msg':'consulta disponible solo con metodo GET'})




# -----TODO UPDATE USER -------------
@app.route(f'{PATH_BASE_API}/user/update/<int:user_id>', methods=['POST', 'PUT'])
def update_user(user_id):
    if request.method == 'PUT':
        data = request.json
        print(data)
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password = data['password']
        confirm_password = data['confirm_password']
        msg = utils.db_update_user(user_id, first_name, last_name, email, password, confirm_password)
        print(msg)
    elif request.method == 'POST':
        msg = 'Este endpoint es para actualizar datos de usuarios preexistentes'
    return {
        "code": 200,
        "msg": msg
    }



#----- DELETE USER---------------

@app.route(f'{PATH_BASE_API}/user/delete/<int:user_id>', methods = ['DELETE', 'POST','PUT','GET'])
def delete_user(user_id):
    if request.method == 'DELETE':
        msg = utils.db_delete_user(user_id)
        return jsonify(msg)
    else:
        msg = "Por favor ejecute el metodo 'DELETE'"
        return jsonify(msg)




#-----TASKS MANAGING--------------------------------------------------

#--CREATE TASK-----
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

    
#----- READ TASKS PER USER -------
@app.route(f'{PATH_BASE_API}/task/mytasks/<int:user_id>', methods = ['GET', 'POST'])
def get_tasks(user_id):
    if request.method == 'GET':
        msg = utils.db_get_task(user_id)
        return jsonify(msg)
    elif request.method == 'POST': 
        msg = 'consulta disponible solo con metodo GET'
    return {
        "code": 200,
        "msg": msg
    }


#-----TODO DELETE TASK---------------
@app.route(f'{PATH_BASE_API}/task/delete/<int:id_task>', methods = ['DELETE', 'POST','PUT','GET'])
def delete_task(id_task):
    if request.method == 'DELETE':
        msg = utils.db_delete_task(id_task)
        return jsonify(msg)
    else:
        msg = "Por favor ejecute el metodo 'DELETE'"
        return jsonify(msg)


#-----TODO UPDATE TASK ---------------

@app.route(f'{PATH_BASE_API}/task/update/<int:id_task>', methods=['POST', 'PUT'])
def update_task(id_task):
    if request.method == 'PUT':
        data = request.json
        title = data['title']
        description = data['description']
        isCompleted = data['isCompleted']
        user_asigned = data['user_asigned']
        msg = utils.db_update_task(id_task, title, description, isCompleted, user_asigned)
        print(msg)
    elif request.method == 'POST':
        msg = 'Este endpoint es para actualizar datos de tareas preexistentes'
    return {
        "code": 200,
        "msg": msg
    }




if __name__ == '__main__':
    app.run(debug=True)
