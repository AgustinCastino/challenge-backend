from config.mongo import mongo

def obtener_empleados():
    return mongo.db.employees.find()



         
