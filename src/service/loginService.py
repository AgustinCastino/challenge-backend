import jwt
from flask import jsonify, request
from config.auth import SECRET_KEY

def login():
    print(SECRET_KEY)
    try:
        username = request.json.get('username')
        password = request.json.get('password')
        if username is None or password is None:
            return jsonify({'message': 'Falta usuario o contraseña'}), 400
        if username == "admin" and password == "123":
            token = jwt.encode({'username': username}, SECRET_KEY, algorithm='HS256')
            return jsonify({'token': token}), 200
        
        return jsonify({'message': 'Error al autenticar el usuario'}), 401
    except Exception as e:
        return jsonify({'message': 'Error del servidor'}), 500