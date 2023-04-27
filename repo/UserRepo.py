from model import User
from extension import db
from werkzeug.security import generate_password_hash

from service.CustomException import CustomException


class UserRepo:

  def getUserBy(column, value):
    user = User.query.filter_by(**{column: value}).first()
    return user

  def addUser(new_user: User):
    hashed_password = generate_password_hash(new_user.password, salt_length=10)
    new_user.password = hashed_password
    try:
      db.session.add(new_user)
      db.session.commit()
      return new_user
    except Exception as e:
      db.session.rollback()
      raise CustomException(500, "Database query failed: {}".format(str(e)))
