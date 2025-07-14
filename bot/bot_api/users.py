import os
import logging
import json
import requests as re

def create_user(user_id, alias):
    logging.info(f"Creating user ID:{user_id}, Alias:{alias}")
    try :
        data = {
            "user_id": user_id,
            "alias": alias
        }
        ans = re.post(url=f"http://{os.getenv('BACKEND_URL')}:8000/users/", data=json.dumps(data), headers={'Content-Type': 'application/json'})
        logging.info(f"Received data: {ans.json()}, code: {ans.status_code}")
    except Exception as e:
        logging.error(f"Connection Error while trying to register user ID:{user_id}, Alias:{alias}")
        return False
    return ans.status_code, ans.json()

def update_user(user_id, fields):
    logging.info(f"Registering user ID:{user_id}, Fields:{fields}")
    try :
        ans = re.patch(url=f"http://{os.getenv('BACKEND_URL')}:8000/users/{user_id}", data=json.dumps(fields), headers={'Content-Type': 'application/json'})
        logging.info(f"Received data: {ans.json()}, code: {ans.status_code}")
    except Exception as e:
        logging.error(f"Connection Error while trying to register user ID:{user_id}, Fields:{fields}")
        return False
    return ans.status_code, ans.json()