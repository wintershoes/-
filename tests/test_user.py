# 测试函数
import requests
token = None
id = None

def test_user_registration():
    url = 'http://127.0.0.1:5000/api/users/register'
    user_data = {
        'username': 'newuser8',
        'password': 'password123',
        'email': 'newuser@example.com',
        'role': 'student'
    }
    response = requests.post(url, json=user_data)
    print(response.json())

def test_user_login():
    global token
    global id
    url = 'http://127.0.0.1:5000/api/users/login'
    user_data = {
        'username': 'newuser8',
        'password': 'password123',
    }
    response = requests.post(url, json=user_data)
    token = response.json().get('token')
    id = response.json().get('userId')
    print(response.json())

def test_get_user_info():
    global token
    global id
    url = f'http://127.0.0.1:5000/api/users/{id}'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, headers=headers)
    print(response.json())

def test_update_user_info():
    global token
    global id
    url = f'http://127.0.0.1:5000/api/users/{id}'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    user_data = {
        'email': 'updated_email@example.com'
    }
    response = requests.put(url, json=user_data, headers=headers)
    print(response.json())

# 调用测试函数
# test_user_registration()
test_user_login()
test_get_user_info()