access_token = "FLlHHZZXhZeyMDD3C-oWEJjIsaq-yFTtPo_OT2_lwt1wLST5A8_kRK1WdM8QhRzOU7MyBGAscovSRxunL9EN4m5DiJSHgPyVTMtWQoEWXbzoJuLu7FAt36izf2Spxi8ZOWlnAoVrm59O0y9HEkJuT6nUyL0pkCztOLRrVHUnv49Z3y1C2FRwMcmvXq8wsgXgRYAHJG79bp9FSBqwEyYYFc8gln4udeuaJYU10KlYc0iHCRqEPFAGCH4CjZ8QuxKf2YFFKG2SvbnJQ9HY6BJcIHP2nKXRXC5lL74zZ4jCC_chFm"

headers = {
     'Content-type': 'application/json',
     "access_token": access_token,
     'Accept-Charset': 'UTF-8'
}

url = "https://openapi.zalo.me/v2.0/oa/message"
rasa_api = "https://hraidev.gbsmarter.com:5057/webhooks/rest/webhook"

data_res_format = {
  "button": {
    "recipient": {
    "user_id": None
    },
    "message": {
      "text": None,
      "attachment": {
          "type": "template",
          "payload": {
              "buttons": [
                  {
                      "title": "Tư vấn bác sĩ",
                      "type": "oa.query.show",
                      "payload": "Tư vấn bác sĩ"
                  },
                  {
                      "title": "Đặt lịch khám",
                      "type": "oa.query.show",
                      "payload": "Đặt lịch khám"
                  },
                  {
                      "title": "Giải đáp thắc mắc",
                      "type": "oa.query.show",
                      "payload": "Giải đáp thắc mắc"
                  },    
              ]
          }
      }
    }
  },
  "non_button": {
    "recipient": {
      "message_id": None
      }, 
    "message":{
        "text": None
      }
  }
}