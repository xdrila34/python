# from pydantic import BaseModel
# from fastapi import FastAPI
#
# app = FastAPI()
#
#"}
from http.client import responses

import requests

api_url = "http://127.0.0.1:8000/create_person"

person_data = {"name": "jon","age": "30"}
response = requests.post(api_url, json=person_data)

print("response code:", response.status_code)
print("response json", response.json)