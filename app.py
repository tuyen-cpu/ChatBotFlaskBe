from flask import Flask

from controller.AuthenticationController import auth_controller
from controller.ChatApiController import chat_api_controller
from flask_cors import CORS
from extension import db

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/chatbot'
app.secret_key = "1993"
db.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
  return 'Hellowwwwww World!'


app.register_blueprint(auth_controller)
app.register_blueprint(chat_api_controller)

if __name__ == '__main__':
  app.run(debug=True)
