import utils
from flask import Flask, jsonify, request, render_template
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

PATH_BASE_API = "/api/v1"
app = Flask(__name__)




conn = sqlite3.connect("tasksapp.db", check_same_thread=False)
c = conn.cursor()



def db_create_user(first_name, last_name, email, password, confirm_password):
    pass_cifr = generate_password_hash(password)
    same = check_password_hash(pass_cifr, confirm_password)
    if same:
        query = ("INSERT INTO `users` VALUES (?, ?, ?, ?)")
        parameters = (first_name, last_name, email, pass_cifr)
        c.execute(query, parameters)
        conn.commit()
        last = c.lastrowid
        msg = f'Nuevo usuario creado {last + 1} '
    else:
        msg = 'Las contraseñas no coinciden'
    return msg



def db_create_task(user_id, title, description, is_completed):
    try:
        query = ("INSERT INTO `tasks` VALUES (?, ?, ?, ?)")
        parameters = (user_id, title, description, is_completed)
        c.execute(query, parameters)
        conn.commit()
        msg = 'Nueva tarea creada'
    except Exception as err:
        print(err)
        msg = 'Error al crear tarea'
    return msg

def db_get_task(user):
    try:
        query = f"SELECT * FROM tasks WHERE id= {user};"
        c.execute(query)
        datos = conn.fetchall()
        tasks = []
        for fila in datos :
            task= {'title': fila[1],'description': fila[2], 'isComplete':fila[3]}
            tasks.append(task)
            print(tasks)
        return {'tareas':tasks,'msg':'Task list'}
    except Exception as ex: 
        return {'mensaje':'Error'}



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
        msg = utils.db_create_task(user_id, title, description,  is_completed)
    elif request.method == 'GET': 
        msg = 'Crea una nueva tarea'
    return {
        "code": 200,
        "msg": msg
    }