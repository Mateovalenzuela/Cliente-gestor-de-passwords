import requests, json


def get_passwords():
    try:
        response = requests.get('http://localhost:5000/api/passwords/')
        if response.status_code == 200:
            return response.json()
        else:
            return response.reason
    except Exception as ex:
        raise Exception(ex)


def get_password(id):
    try:
        response = requests.get(f'http://localhost:5000/api/passwords/{id}')
        if response.status_code == 200:
            return response.json()
        else:
            return response.reason
    except Exception as ex:
        raise Exception(ex)


def add_password(data: dict):
    try:
        dataJson = json.loads(json.dumps(data))
        response = requests.post('http://localhost:5000/api/passwords/add', json = dataJson)
        if response.status_code == 200:
            return response.json()
        else:
            return response.reason
    except Exception as ex:
        raise Exception(ex)


def update_password(data: dict):
    try:
        dataJson = json.loads(json.dumps(data))
        id = data['id']
        response = requests.put(f'http://localhost:5000/api/passwords/update/{id}', json = dataJson)
        if response.status_code == 200:
            return response.json()
        else:
            return response.reason
    except Exception as ex:
        raise Exception(ex)


def delete_password(id: str):
    try:
        response = requests.delete(f'http://localhost:5000/api/passwords/delete/{id}')
        if response.status_code == 200:
            return response.json()
        else:
            return response.reason
    except Exception as ex:
        raise Exception(ex)


if __name__ == '__main__':
    # passwords = get_passwords()
    # print(passwords)

    # password = get_password('4de53f0a-7be0-41bb-9d2a-6f58978705d7')
    # print(password)

    data = {
        "id": "51bd64b7-0615-4a21-a7f4-ea7e92be92ce",
        "descripcion": "",
        "titulo": "Adidas",
        "url": "",
        "usuario": "messi@gmail.com",
        "password": "messi10"
    }
    # response = update_password(data)
    # response = add_password(data)
    id = '51bd64b7-0615-4a21-a7f4-ea7e92be92ce'
    response = delete_password(id)
    print(response)
