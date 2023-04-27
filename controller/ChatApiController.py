from flask import request, jsonify, Blueprint

from service.CustomResponse import CustomResponse
import requests

chat_api_controller = Blueprint('chat', __name__)


@chat_api_controller.route('/chat/hello', methods=['GET'])
def helloTest():
  return 'Hello'


@chat_api_controller.route('/api/request', methods=['POST'])
def chatApiRequest():
  data = request.get_json()
  message = data.get('message')
  url = 'http://localhost:5001/api/response'
  response = requests.post(url, json={'message': message})
  return jsonify(response.json())


@chat_api_controller.route('/api/response', methods=['POST'])
def chatApiResponse():
  data = request.get_json()
  response = data.get('response')
  result = CustomResponse(200, 'Sucessful response!', str(response))
  return result.__dict__
