import os
import logging
import json
import requests as re

def send_document(user_id, file_in_bytes):
    logging.info(f"Upploading document from user ID:{user_id}")
    try :
        data = {
            "userId": user_id,
            "file_in_bytes": str(file_in_bytes, encoding="latin-1")
        }
        ans = re.post(f"http://{os.getenv('BACKEND_URL')}:8000/documents/upload", data=json.dumps(data),  headers={'Content-Type': 'application/json'})
    except Exception as e:
        logging.error(f"Connection Error while trying to uplad file from user ID:{user_id}")
        return False
    return True
    