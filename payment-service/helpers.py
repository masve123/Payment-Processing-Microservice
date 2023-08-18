import os
import requests

USER_SERVICE_URL = os.environ.get("USER_SERVICE_URL", "http://127.0.0.1:5000")


def validate_user(user_id):
    user_service_endpoint = f"{USER_SERVICE_URL}/get_user/{user_id}"
    response = requests.get(user_service_endpoint)
    return response.status_code == 200
