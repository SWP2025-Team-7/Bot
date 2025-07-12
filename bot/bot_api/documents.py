import os
import logging
import json
import requests as re
from datetime import datetime

def send_document(user_id, file_path):
    logging.info(f"Upploading document from user ID:{user_id}")
    try :
        data = {
            "user_id": user_id,
            "file_path": file_path
        }
        ans = re.post(f"http://{os.getenv('BACKEND_URL')}:8000/users/{user_id}/documents/upload", data=json.dumps(data),  headers={'Content-Type': 'application/json'})
        logging.info(f"Received data: {ans.json()}, code: {ans.status_code}")

    except Exception as e:
        logging.error(f"Connection Error while trying to uplad file from user ID:{user_id}")
        return False
    return ans.status_code, ans.json()
    