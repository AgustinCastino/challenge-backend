from flask import  jsonify, request
from config.auth import SECRET_KEY
import jwt
 

def verify_token(func):
    def wrapper(*args, **kwargs):
        print(SECRET_KEY)
        token = request.headers.get('Authorization', '')
        if not token:
            return jsonify({'message': 'El token no fue enviado'}), 401
        token_parts = token.split(" ")
        if len(token_parts) != 2 or token_parts[0].lower() != 'bearer':
            return jsonify({'message': 'Formato de token invalido'}), 401
        token = token_parts[1]
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            request.username = payload['username']
            return func(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expirado'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token inválido'}), 403
    return wrapper