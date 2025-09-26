from model import userModel
from flask_pymongo import Response
from exceptions.exceptions import HttpError, NotFoundError
from utils.handleError import handleError

def getEmployees(puesto, page, limit):
    try:
        employees = userModel.get_users(puesto, page, limit)
        return employees
    except Exception as e:
        return handleError(e)
        
def getEmployeeById(userId):
    try:
        employee = userModel.get_user_by_id(userId)
        return employee
    except Exception as e:
        return handleError(e)

def newEmployee(newEmployee):
    # Debería agregar una función para validar el json y solo pasar datos de empleado
    try:
        result = userModel.create_employee(newEmployee)
        return result
    except Exception as e:
        return handleError(e)

def updateEmployee(employeeId, updatedEmployee):
    try:
        result = userModel.update_employee(employeeId, updatedEmployee)
        return result
    except Exception as e:
        return handleError(e)

def deleteEmployee(employeeId):
    try:
        result = userModel.delete_employee(employeeId)
        return result
    except Exception as e:
        return handleError(e)
    
