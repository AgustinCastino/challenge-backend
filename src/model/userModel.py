from bson import json_util, ObjectId
from config.mongo import mongo
from exceptions.exceptions import NotFoundError

def get_users(puesto, page, limit):

    try:
        if puesto:
            filtro = {"puesto": puesto}
        else:
            filtro = {}

        result = mongo.db.employees.find(filtro).skip((page - 1) * limit).limit(limit)

        if result is None:
            raise NotFoundError("No se encontraron empleados")
        return result
    except Exception as e:
        raise Exception(f"Error en la base: {str(e)}")

def get_user_by_id(userId):
    try:
        employee = mongo.db.employees.find_one({"_id": ObjectId(userId)})
        if employee is None:
            raise NotFoundError(f"Empleado con id {userId} no encontrado")
        return employee
    except Exception as e:
        raise Exception(f"Error en la base: {str(e)}")
    

def create_employee(newEmployee):
    try:
        result = mongo.db.employees.insert_one(newEmployee)
        response = {
            "id": str(result.inserted_id),
            "message": f"Empleado {newEmployee['nombre']} creado exitosamente",
        }
        return response
    except Exception as e:
        raise Exception(f"Error en la base: {str(e)}")
    
def update_employee(userId, updatedEmployee):
    try:
        result = mongo.db.employees.update_one(
            {"_id": ObjectId(userId)},
            {"$set": updatedEmployee}
        )
        if result.matched_count == 0:
            raise NotFoundError(f"Empleado con id {userId} no encontrado")
        return "Empleado actualizado exitosamente"
    
    except Exception as e:
        raise Exception(f"Error en la base: {str(e)}")

def delete_employee(employeeId):
    try:
        result = mongo.db.employees.delete_one({"_id": ObjectId(employeeId)})
        if result.deleted_count == 1:
            return "Empleado eliminado exitosamente"
        raise NotFoundError(f"Empleado con id {employeeId} no encontrado")
    except Exception as e:
        return {"success": False, "message": "Error al eliminar empleado", "error": str(e)}