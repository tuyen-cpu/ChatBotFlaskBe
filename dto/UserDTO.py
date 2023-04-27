import json
class UserDTO:
  def __init__(self, email: str, first_name: str, last_name: str):
    self.email = email
    self.first_name = first_name
    self.last_name = last_name

  @staticmethod
  def from_model(user_model):
    return UserDTO(email=user_model._email, first_name=user_model._first_name, last_name=user_model._last_name)

  def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__,
                      sort_keys=True, indent=4)