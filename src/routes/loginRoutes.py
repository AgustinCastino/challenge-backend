from flask import Blueprint
from controller import loginController

login = Blueprint('login', __name__)

# POST Endpoints
@login.route('/', methods=['POST'])
def login_user():
    return loginController.login()

