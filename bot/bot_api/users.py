import os
import logging
import json
import requests as re

def register_user(user_id, username):
    logging.info(f"Registring user ID:{user_id}, Alias:{username}")
    try :
        data = {
            "new_bot_user": {
                "user_id": user_id,
                "username": username
            }
        }
        ans = re.post(url=f"http://{os.getenv('BACKEND_URL')}:8000/bot_users/register", data=json.dumps(data), headers={'Content-Type': 'application/json'})
        logging.info(f"Received data: {ans.json()}, code: {ans.status_code}")
    except Exception as e:
        logging.error(f"Connection Error while trying to register user ID:{user_id}, Alias:{username}")
        return False
    return ans.status_code, ans.json()