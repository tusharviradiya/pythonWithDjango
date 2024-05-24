import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

# get method
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    headers = {'Content-Type': 'application/json'}
    r = requests.get(url = URL,headers=headers, data = json_data)
    print(f"Status Code: {r.status_code}")
    print(f"Response Text: {r.text}")
    try:
        data = r.json()
        print(data)
    except json.JSONDecodeError:
        print("Response is not in JSON format")
# get_data()

# post method
def post_data():
    data = {
        'name': 'John',
        'roll': 30,
        'city': 'New York'
    }
    json_data = json.dumps(data)
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url = URL, headers=headers, data = json_data)
    print(f"Status Code: {r.status_code}")
    print(f"Response Text: {r.text}")
    try:
        data = r.json()
        print(data)
    except json.JSONDecodeError:
        print("Response is not in JSON format")
        print(f"Response Text: {r.text}")
# post_data()

# update method
def update_data():
    data = {
        'id': 8,
        'name': 'rogi',
        'city': 'nana ankadiya'
    }

    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)
# update_data()

# delete method
def delete_date():
    data = {
        'id': 8,
    }
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)
delete_date()