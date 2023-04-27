from flask import request, jsonify, Blueprint
import pytz
from model import User
from service.CustomException import CustomException
from service.CustomResponse import CustomResponse
from service.AuthenticationService import AuthenticationService as authService
from constant.Messages import Messages
import re
from constant.Regex import Regex
from constant.Utilities import Utilities
import jwt
from datetime import datetime, timedelta

auth_controller = Blueprint('auth', __name__)

@auth_controller.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        validatedResult = Utilities.validate(data)
        if len(validatedResult.get('errorMessages')) > 0 and validatedResult.get('error') is True:
            raise CustomException(validatedResult.get('errorMessages'), 404, "empty or null")
        if not (re.match(Regex.EMAIL_LIMIT_40, email)):
            raise CustomException(Messages.EMAIL_VALID, 404, email)
        if not 5 < len(password) < 21:
            raise CustomException(Messages.PASSWORD_VALID, 404, password)
        if not 2 < len(first_name) < 51:
            raise CustomException(Messages.FIRST_NAME_VALID, 404, first_name)
        if not 2 < len(last_name) < 51:
            raise CustomException(Messages.LAST_NAME_VALID, 404, last_name)
        if authService.getUserBy('_email', email):
            raise CustomException(Messages.USER_EXIST.format(email=data.get('email')), 500, data.get('email'))
        user = User(**data)
        userRes= authService.register(user)
        response = CustomResponse(200, Messages.REGISTRATION_SUCCESS.format(email=user.email), userRes.toJSON())
        return jsonify(response.__dict__)
    except Exception as e:
        return jsonify({'status': e.statusCode, 'message': e.message, 'value': e.error}), 500


@auth_controller.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        validatedResult = Utilities.validate(data)
        if len(validatedResult.get('errorMessages')) > 0 and validatedResult.get('error') is True:
            raise CustomException(validatedResult.get('errorMessages'), 404)
        if not (re.match(Regex.EMAIL_LIMIT_40, email)):
            raise CustomException(Messages.EMAIL_VALID, 404, email)
        if not 5 < len(password) < 21:
            raise CustomException(Messages.PASSWORD_VALID, 404, f"{password} have {len(password)} character")
        user = authService.login(data)
        if user is None:
            raise CustomException(Messages.LOGIN_FAILED, 404, "Email or Password")
        expirationTime = datetime.utcnow() + timedelta(minutes=10)
        localTimeZone = pytz.timezone('Asia/Ho_Chi_Minh')
        localExpirationTime = pytz.utc.localize(expirationTime).astimezone(localTimeZone)
        payload = {'email': email,
                   'issued_at': datetime.utcnow().isoformat(),
                   'expired': localExpirationTime.isoformat(),
                   }
        secret = '1993'
        token = jwt.encode(payload, secret, algorithm='HS256')
        userInfo = {
            'id': user.id,
            'firstName': user.first_name,
            'lastName': user.last_name,
            'email': user.email,
            'accessToken': token
        }
        response = CustomResponse(200, Messages.LOGIN_SUCCESS.format(name=userInfo.get('first_name')), userInfo)
        # return {'response': response.__dict__, 'token': token}
        return {**response.__dict__}
    except Exception as e:
        return jsonify({'status': e.statusCode, 'message': e.message, 'value': e.error}), 404
