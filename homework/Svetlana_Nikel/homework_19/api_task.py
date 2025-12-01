import requests


def new_object():
    body = {
        "data": {"color": "black", "size": "full"},
        "name": "Broker"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://objapi.course.qa-practice.com/object', json=body, headers=headers).json()
    assert response["data"] == {"color": "black", "size": "full"}, "Data incorrect"
    assert response["name"] == "Broker", "Name incorrect"
    return response['id']


def clear(object_id):
    requests.delete(f'https://objapi.course.qa-practice.com/object/{object_id}')


def put_object():
    object_id = new_object()
    body = {
        "data": {"color": "white", "size": "short"},
        "name": "new_name"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'https://objapi.course.qa-practice.com/object/{object_id}',
                            json=body, headers=headers).json()
    assert response["data"] == {"color": "white", "size": "short"}, "Data incorrect"
    assert response["name"] == "new_name", "Name incorrect"
    clear(object_id)


def patch_object():
    object_id = new_object()
    body = {
        "data": {"color": "white", "size": "short"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'https://objapi.course.qa-practice.com/object/{object_id}',
                              json=body, headers=headers).json()
    assert response["data"] == {"color": "white", "size": "short"}, "Data incorrect"
    clear(object_id)


def delete_object():
    object_id = new_object()
    response = requests.delete(f'https://objapi.course.qa-practice.com/object/{object_id}')
    print(response.status_code)
