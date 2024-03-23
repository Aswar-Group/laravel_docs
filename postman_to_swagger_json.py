import argparse
import os

import requests
import json


def write_swagger_spec_if_different(new_spec, file_path='swagger.json'):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                existing_spec = json.load(file)
            except json.JSONDecodeError:
                existing_spec = None

        if existing_spec == new_spec:
            print("The new specification is the same as the existing one. No write needed.")
            return False

    with open(file_path, 'w') as file:
        json.dump(new_spec, file, indent=2)

    print("Swagger specification has been written to", file_path)
    return True


parser = argparse.ArgumentParser(description='Send a collection to a URL and get a visualizer template.')
parser.add_argument('postman_file', type=str, help='Path to the JSON file of the collection data')
parser.add_argument('API_KEY', type=str, help='Postman API Key')

# Parse arguments
args = parser.parse_args()

try:
    with open(args.postman_file, 'r') as file:
        collection = json.load(file)
    api_key = args.API_KEY
except json.JSONDecodeError as e:
    print("Error: The collection or api_key argument is not valid.", e)
    exit(1)

collection_json = json.dumps(collection)
url = "https://demo.postmansolutions.com/postman2swagger"

headers = {
    "Content-Type": "application/json",
    "X-API-Key": api_key
}

body = {
    "mode": "raw",
    "raw": collection_json
}

response = requests.post(url, headers=headers, json=body)

new_swagger_spec = response.json()
result = write_swagger_spec_if_different(new_swagger_spec)
print("Write operation result:", result)
if result:
    exit(0)
else:
    exit(1)
