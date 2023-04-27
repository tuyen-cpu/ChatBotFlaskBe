from werkzeug.security import check_password_hash, generate_password_hash

from dto.UserDTO import UserDTO
from model import User
from service.CustomException import CustomException

from repo.UserRepo import UserRepo


class AuthenticationService:

  @staticmethod
  def register(new_user: User):
    try:
      user = UserRepo.addUser(new_user)
      print(user)
      userInformation = UserDTO.from_model(user)
      return userInformation
    except Exception as e:
      raise CustomException(str(e))

  @staticmethod
  def login(data):
    try:
      email = data.get('email')
      password = data.get('password')
      user = UserRepo.getUserBy('_email', email)
      if not user or not check_password_hash(user.password, password):
        return None
      else:
        return user
    except Exception as e:
      raise CustomException(500, str(e))

  @staticmethod
  def getUserBy(column, value):
      user = UserRepo.getUserBy(column, value)
      return user

