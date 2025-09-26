from flask import Blueprint
from controller import userController
from middleware.authMiddleware import verify_token

users = Blueprint('users', __name__)

# GET Endpoints
@users.route("", methods=["GET"])
@users.route("/<string:employeeId>", methods=["GET"])
def getEmployees(employeeId=None):
    if employeeId:
        return userController.getEmployeeById(employeeId)
    return userController.getEmployees()

# POST Endpoints
@users.route("", methods=["POST"])
@verify_token
def newEmployee():
    return userController.newEmployee()

# PUT Endpoints
@users.route("/<string:employeeId>", methods=["PUT"])
def updateEmployee(employeeId):
    return userController.updateEmployee(employeeId)

# DELETE Endpoints
@users.route("/<string:employeeId>", methods=["DELETE"])
def deleteEmployee(employeeId):
    return userController.deleteEmployee(employeeId)