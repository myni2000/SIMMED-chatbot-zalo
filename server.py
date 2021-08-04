from flask import Flask, render_template, request, jsonify
from flask_ngrok import run_with_ngrok 
import requests
from config import *
import utils

app = Flask(__name__)
run_with_ngrok(app)

@app.route("/simmed", methods=['POST'])
def solve():
  '''
  When /simmed is called, this function will operate.
  '''
  global access_token, headers, url, rasa_api
  data = request.get_json(force=True)
  if 'event_name' in data: # check api event
    if data['event_name'] == "user_send_text": # check whether user send text
      user_id = data['sender']['id']
      mess_id = data['message']['msg_id']
      message = data['message']['text']
      rasa = requests.post(rasa_api, json={"sender": user_id, "message": message})
      print("User send message '{}' với id '{}'".format(message, mess_id))
      rasa_json = rasa.json()
      try:
        text_res = rasa_json[0]['text']
        if 'buttons' in rasa_json[0]:
          r = utils.response(user_id=user_id, text_res=text_res, button=True)
        else:
          r = utils.response(mess_id=mess_id, text_res=text_res)
        return {'message': 'Send successfully'}
      except Exception as e:
        print('Error: ', e)
    else:
        return {'message': 'Receive user msg successfully'}
  else:
      return {'message': 'Connect successfully'}

if __name__ == "__main__":
  app.run()