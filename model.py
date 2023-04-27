from extension import db
import json
class User(db.Model):
  __tablename__ = 'users'
  _id = db.Column('id', db.Integer, primary_key=True)
  _email = db.Column('email', db.String(200))
  _first_name = db.Column('first_name', db.String(100))
  _last_name = db.Column('last_name', db.String(100))
  _password = db.Column('password', db.String(200))

  def __init__(self, email, first_name, last_name, password):
    self._email = email
    self._first_name = first_name
    self._last_name = last_name
    self._password = password

  @property
  def id(self):
    return self._id

  @id.setter
  def id(self, value):
    self._id = value

  @property
  def email(self):
    return self._email

  @email.setter
  def email(self, value):
    self._email = value

  @property
  def first_name(self):
    return self._first_name

  @first_name.setter
  def first_name(self, value):
    self._first_name = value

  @property
  def last_name(self):
    return self._last_name

  @last_name.setter
  def last_name(self, value):
    self._last_name = value

  @property
  def password(self):
    return self._password

  @password.setter
  def password(self, value):
    self._password = value

  def __str__(self):
    return f'User id: {self._id}: name: {self._first_name} {self._last_name} email:({self._email})'

  def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__,
                      sort_keys=True, indent=4)
