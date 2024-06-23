# 测试函数
import requests

def test_user_registration():
    url = 'http://127.0.0.1:5000/api/users/register'
    user_data = {
        'username': 'newuser',
        'password': 'password123',
        'email': 'newuser@example.com',
        'role': 'student'
    }
    response = requests.post(url, json=user_data)
    print(response.json())

# 调用测试函数
test_user_registration()
