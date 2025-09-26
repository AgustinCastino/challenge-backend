from service import userService
from flask import request, jsonify

def getEmployees():
    puesto = request.args.get('puesto', default=None, type=str)
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=5, type=int)
    try:
        employees = userService.getEmployees(puesto, page, limit)
        return jsonify({"success": True, "data": employees}), 200
    except Exception as e:
        return jsonify({"success": False, "message": e.message, "error": str(e)}), e.http_status

def getEmployeeById(employeeId):
    try:
        employee = userService.getEmployeeById(employeeId)
        return jsonify({"success": True, "data": employee}), 200
    except Exception as e:
        return jsonify({"success": False, "message": e.message, "error": str(e)}), e.http_status

def newEmployee():
    newEmployee = request.get_json()
    try:
        result = userService.newEmployee(newEmployee)
        return jsonify({"success": True, "data": result}), 201
    except Exception as e:
        return jsonify({"success": False, "message": e.message, "error": str(e)}), e.http_status

def updateEmployee(userId):
    updatedEmployee = request.get_json()
    try:
        result = userService.updateEmployee(userId, updatedEmployee)
        return jsonify({"success": True, "data": result}), 200
    except Exception as e:
        return jsonify({"success": False, "message": e.message, "error": str(e)}), e.http_status

def deleteEmployee(userId):
    try:
        result = userService.deleteEmployee(userId)
        return jsonify({"success": True, "data": result}), 200
    except Exception as e:
        return jsonify({"success": False, "message": e.message, "error": str(e)}), e.http_status