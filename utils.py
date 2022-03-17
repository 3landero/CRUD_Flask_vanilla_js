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


from socket import MsgFlag
import sqlite3
from pymysql import DateFromTicks
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






#---------------USER MANAGING-------------------------------------


#-------CREATE USER --------------------
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


#------READ USER -------------------------
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
        return {'mensaje':'Error de Modulo: utils'}



#----TODO UPDATE USER ------------------------
def db_update_user(id, first_name, last_name, email, password, confirm_password):
    try:
        pass_cifr = generate_password_hash(password)
        same = check_password_hash(pass_cifr, confirm_password)
        print(same)
        if same:
            query = f"UPDATE users SET first_name= '{first_name}', last_name = '{last_name} ' , email= '{email}', password='{pass_cifr}' WHERE id = {id};"
            #query = ("UPDATE `users` SET VALUES (Null,?, ?, ?, ?) WHERE id = {id};")
            #parameters = (first_name, last_name, email, pass_cifr)
            c.execute(query)
            conn.commit()
            msg = f'Usuario {id} actualizado exitosamente'
            print(query)
        else:
            msg = 'Las contraseñas no coinciden'
    except Exception as ex: 
        return {'mensaje':'Error de Modulo: utils'}


#---- DELETE USER ------------------------

def db_delete_user(user):
    try:
        sql = f'DELETE FROM users WHERE id = {user};'
        c.execute(sql)
        conn.commit()
        msg = f'usuario {user} ha sido borrado exitosamente'
        return msg
    except Exception as ex:
        return {f'mensaje':'El usuario {user} no se ha encontrado'}
        



#-----TASKS MANAGING--------------------------------------------------------------
#-------CREATE TASK --------------------------

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


#-----READ TASK --------------------------------
def db_get_task(user):
    try:
        query = f"SELECT * FROM tasks WHERE user_asigned= {user};"
        c.execute(query)
        datos = c.fetchall()
        tasks = []
        for fila in datos :
            task= {'title': fila[1],'description': fila[2], 'isComplete':fila[3]}
            tasks.append(task)
            tareas = {'tareas':tasks,'msg':'Task list'}
        return tareas
    except Exception as err: 
        print(err)
        msg = 'mensaje Error  desde utils'
        return msg

#----UPDATE TASK ------------------------
def db_update_task(id_task,title, description, isCompleted, user_asigned):
    try:
        query = f"UPDATE tasks SET title= '{title}', description = '{description} ' , isCompleted= '{isCompleted}', 'user_asigned'='{user_asigned}' WHERE id_task  = {id_task};"
        c.execute(query)
        conn.commit()
        msg = f'Tarea {id_task} actualizada exitosamente'
        return msg
    except Exception as ex: 
        return {'mensaje':'Error de Modulo: utils'}


#----DELETE TASK ------------------------
def db_delete_task(id_task):
    try:
        sql = f'DELETE FROM tasks WHERE id_task = {id_task};'
        c.execute(sql)
        conn.commit()
        msg = f'La tarea num {id_task} ha sido borrada exitosamente'
        return msg
    except Exception as ex:
        return {f'mensaje':'La tarea {id_task} no se ha encontrado'}