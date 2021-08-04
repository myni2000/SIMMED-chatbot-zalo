from config import *
import requests

def response(**kwargs):
  global data_res_format
  '''
  Parameters:
    + idmess (str): message id
    + user_id (str): user id
    + message (str): content of message (utf-8)

  Return:
    + Response signal
  '''
  # global access_token, headers, url

  
  if 'button' in kwargs: 
    '''
    Have button in message
    '''
    datares = data_res_format["button"]
    datares['recipient']['user_id'] = kwargs['user_id']
  else:
    datares = data_res_format['non_button']
    datares["recipient"]["message_id"] = kwargs['mess_id']
  
  datares["message"]["text"] = kwargs['text_res']
  response = requests.post(url, headers=headers, data=str(datares).encode('utf-8'))

  return response