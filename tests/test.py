import requests
import json
import base64
import os
from PIL import Image
from io import BytesIO

base_url = 'http://localhost:5000' 

# 测试创建学生账户
def test_create_student_account():
    url = base_url + '/account/student'
    headers = {'Content-Type': 'application/json'}
    data = {
        "net_id": "student123",
        "name": "John Doe",
        "gain": 100,
        "password": "password123"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json())

# 测试获取学生账户信息
def test_get_student_account(net_id):
    url = base_url + f'/account/student/{net_id}'
    response = requests.get(url)
    print(response.json())

# 测试更新学生账户信息
def test_update_student_account(net_id):
    url = base_url + f'/account/student/{net_id}'
    headers = {'Content-Type': 'application/json'}
    data = {
        "name": "Updated Name",
        "gain": 150
    }
    response = requests.put(url, headers=headers, data=json.dumps(data))
    print(response.json())

# 测试删除学生账户
def test_delete_student_account(net_id):
    url = base_url + f'/account/student/{net_id}'
    response = requests.delete(url)
    print(response.json())

# 测试创建教师账户
def test_create_teacher_account():
    url = base_url + '/account/teacher'
    headers = {'Content-Type': 'application/json'}
    data = {
        "net_id": "teacher123",
        "name": "Jane Smith",
        "real_name": "Jane Doe",
        "gain": 200,
        "password": "password456"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json())

# 测试获取教师账户信息
def test_get_teacher_account(net_id):
    url = base_url + f'/account/teacher/{net_id}'
    response = requests.get(url)
    print(response.json())

# 测试更新教师账户信息
def test_update_teacher_account(net_id):
    url = base_url + f'/account/teacher/{net_id}'
    headers = {'Content-Type': 'application/json'}
    data = {
        "name": "Updated Teacher Name",
        "gain": 250
    }
    response = requests.put(url, headers=headers, data=json.dumps(data))
    print(response.json())

# 测试删除教师账户
def test_delete_teacher_account(net_id):
    url = base_url + f'/account/teacher/{net_id}'
    response = requests.delete(url)
    print(response.json())

# 测试创建管理员账户
def test_create_admin_account():
    url = base_url + '/account/admin'
    headers = {'Content-Type': 'application/json'}
    data = {
        "net_id": "admin123",
        "name": "Admin User",
        "real_name": "Admin Doe",
        "gain": 300,
        "password": "password789"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json())

# 测试获取管理员账户信息
def test_get_admin_account(net_id):
    url = base_url + f'/account/admin/{net_id}'
    response = requests.get(url)
    print(response.json())

# 测试更新管理员账户信息
def test_update_admin_account(net_id):
    url = base_url + f'/account/admin/{net_id}'
    headers = {'Content-Type': 'application/json'}
    data = {
        "name": "Updated Admin Name",
        "gain": 350
    }
    response = requests.put(url, headers=headers, data=json.dumps(data))
    print(response.json())

# 测试删除管理员账户
def test_delete_admin_account(net_id):
    url = base_url + f'/account/admin/{net_id}'
    response = requests.delete(url)
    print(response.json())

# 测试创建评论
def test_create_comment():
    url = base_url + '/comments'
    headers = {'Content-Type': 'application/json'}
    data = {
        "net_id": "user123",
        "book_id": "book456",
        "comment": "This book is great!",
        "score": 5,
        "time": 1645612345.678
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json())

# 测试获取评论
def test_get_comment(net_id, book_id):
    url = base_url + f'/comments/{net_id}/{book_id}'
    response = requests.get(url)
    print(response.json())

# 测试删除评论
def test_delete_comment(net_id, book_id):
    url = base_url + f'/comments/{net_id}/{book_id}'
    response = requests.delete(url)
    print(response.json())

# 测试验证账户
def test_verify_account():
    url = base_url + '/account/verify'
    headers = {'Content-Type': 'application/json'}
    data = {
        "net_id": "student123",
        "password": "password123",
        "account_type": "student"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json())

# 测试创建预约
def test_create_reservation():
    url = base_url + '/reservations'
    headers = {'Content-Type': 'application/json'}
    data = {
        "net_id": "user123",
        "book_id": "book456",
        "time": 1645612345.678
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json())

# 测试获取预约
def test_get_reservation(net_id, book_id):
    url = base_url + f'/reservations/{net_id}/{book_id}'
    response = requests.get(url)
    print(response.json())

# 测试删除预约
def test_delete_reservation(net_id, book_id):
    url = base_url + f'/reservations/{net_id}/{book_id}'
    response = requests.delete(url)
    print(response.json())

# 测试创建借书记录
def test_create_borrow_book():
    url = base_url + '/borrowbook'
    headers = {'Content-Type': 'application/json'}
    data = {
        "net_id": "user123",
        "book_id": "book456",
        "time": "2024-06-16T12:00:00Z"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json())

# 测试获取借书记录
def test_get_borrow_book(net_id, book_id):
    url = base_url + f'/borrowbook/{net_id}/{book_id}'
    response = requests.get(url)
    print(response.json())

# 测试删除借书记录
def test_delete_borrow_book(net_id, book_id):
    url = base_url + f'/borrowbook/{net_id}/{book_id}'
    response = requests.delete(url)
    print(response.json())

# 测试创建书籍记录
def test_create_book():
    url = base_url + '/books'
    headers = {'Content-Type': 'application/json'}

    # 读取图像文件并转换为Base64编码字符串的函数
    def image_to_base64(image_path):
        with open(image_path, 'rb') as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        return base64_image

    # 示例图像文件路径，请替换为实际的图像文件路径
    # 获取当前脚本所在目录的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 构建完整的图片文件路径
    image_path = os.path.join(current_dir, 'img.jpg')
    base64_image = image_to_base64(image_path)

    data = {
        "book_id": "book123",
        "book_name": "Python Programming",
        "book_image": base64_image,
        "book_author": "Guido van Rossum",
        "book_location": "Library A",
        "book_score": 4.5,
        "book_storage": "Shelf B",
        "book_reservation_time": 3600.0,
        "book_reservation_location": "Desk 1"
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json())

def test_get_book(book_id):
    url = f"{base_url}/books/{book_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        book_data = response.json()

        # 如果返回的书籍信息中包含封面数据，将其解码并显示
        if 'book_image' in book_data:
            image_data = base64.b64decode(book_data['book_image'])
            image = Image.open(BytesIO(image_data))
            image.show()  # 在默认图像查看器中显示图像
            # 可以选择保存图像到本地文件
            # image.save('book_cover.jpg')

        return book_data  # 可以选择返回处理后的书籍信息
    except requests.exceptions.RequestException as e:
        print(f"Error fetching book: {e}")
        return None  # 处理请求异常的情况


# 测试删除书籍记录
def test_delete_book(book_id):
    url = base_url + f'/books/{book_id}'
    response = requests.delete(url)
    print(response.json())


# 执行测试示例
if __name__ == '__main__':
    #测试学生账户相关操作
    test_create_student_account()
    test_get_student_account('student123')
    test_update_student_account('student123')
    test_delete_student_account('student123')

    # 测试教师账户相关操作
    test_create_teacher_account()
    test_get_teacher_account('teacher123')
    test_update_teacher_account('teacher123')
    test_delete_teacher_account('teacher123')

    # 测试管理员账户相关操作
    test_create_admin_account()
    test_get_admin_account('admin123')
    test_update_admin_account('admin123')
    test_delete_admin_account('admin123')

    # 测试评论相关操作
    test_create_comment()
    test_get_comment('user123', 'book456')
    test_delete_comment('user123', 'book456')

    # 测试账户验证
    test_verify_account()

    # 测试预约相关操作
    test_create_reservation()
    test_get_reservation('user123', 'book456')
    test_delete_reservation('user123', 'book456')

    # 测试借书记录相关操作
    test_create_borrow_book()
    test_get_borrow_book('user123', 'book456')
    test_delete_borrow_book('user123', 'book456')

    # 测试书籍相关操作

    test_create_book()
    test_get_book('book123')
    test_delete_book('book123')
