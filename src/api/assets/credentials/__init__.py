from os import path
import json

with open(path.join('api','assets','credentials','credentials.json')) as f:
    credentials = json.load(f)