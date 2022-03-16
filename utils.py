"""
------------------------------------------------------------------------
Este archivo fue creado para cargar las operaciones que se realizarán   
en la base de datos                                                     
                                                                        
Creado por: Jhon Doe                                                    
Fecha de creación: 12 de Marzo 2022                                     
Contacto: jhondoe@loopgk.com +529371303699                              
                                                                        
Cómo utilizarlo:
    import utils                                                                                                                            
------------------------------------------------------------------------
"""


import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


# Connect to Database
conn = sqlite3.connect("tasksapp.db", check_same_thread=False)
c = conn.cursor()

def create_tables():
    """Función para crear tablas. \n
    
    Cómo utilizar::

        import utils
        msg = utils.create_tables()

    """
    query = """
        CREATE TABLE users(
            id INT(11)  NOT NULL AUTO_INCREMENT,
            first_name TEXT ,
            last_name TEXT ,
            email TEXT ,
            password TEXT
            PRIMARY KEY (id)
        );
        
        CREATE TABLE tasks (
            id_task INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            isCompleted INTEGER,
            user_asigned INTEGER
        );
    """
    try:
        c.execute(query,)
        msg = "Tablas creadas exitosamente"
    except:
        msg = "Las tablas ya existen"
    return msg

def db_create_user(first_name, last_name, email, password, confirm_password):
    pass_cifr = generate_password_hash(password)
    same = check_password_hash(pass_cifr, confirm_password)
    if same:
        query = ("INSERT INTO `users` VALUES (Null,?, ?, ?, ?)")
        parameters = (first_name, last_name, email, pass_cifr)
        c.execute(query, parameters)
        conn.commit()
        last = c.lastrowid
        msg = f'Nuevo usuario creado {last } '
    else:
        msg = 'Las contraseñas no coinciden'
    return msg



def db_create_task(title, description, is_completed, user_asigned):
    try:
        query = ("INSERT INTO `tasks` VALUES (Null, ?, ?, ?, ?)")
        parameters = (title, description, is_completed, user_asigned)
        c.execute(query, parameters)
        conn.commit()
        msg = 'Nueva tarea creada exitosamente'
    except Exception as err:
        print(err)
        msg = 'Error al crear tarea en utils'
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
        return {'mensaje':'Error  desde utils'}


def db_get_user(user):
    try:
        sql = f'SELECT * FROM USERS WHERE ID = {user}'    
        c.execute(sql)
        datos = c.fetchone()
        if datos != None:
            user= { 'id':datos[0], 'nombre': datos[1],'apellido': datos[2], 'email':datos[3], 'password':datos[4]}
            print (user)
            return user
        else:
                return {'mensaje':'cliente no encontrado'}
    except Exception as ex: 
        return {'mensaje':'Error de utils'}
