import requests
import pytest

work_url = 'https://objapi.course.qa-practice.com/object'


@pytest.fixture(scope="session", autouse=True)
def all_tests_messages():
    print("\nStart testing")
    yield
    print("\nTesting completed")


@pytest.fixture(autouse=True)
def each_test_messages():
    print("\nbefore test")
    yield
    print("after test")


@pytest.fixture()
def new_object():
    body = {
        "data": {"color": "black", "size": "full"},
        "name": "Broker"
    }
    response = requests.post(work_url, json=body, timeout=10)
    object_id = response.json()["id"]
    yield object_id
    requests.delete(f"{work_url}/{object_id}", timeout=10)


@pytest.mark.critical
@pytest.mark.parametrize(
    "data, name",
    [
        ({"color": "black", "size": "full"}, "Broker"),
        ({"color": "white", "size": "short"}, "Bread"),
        ({"color": "grey", "size": "part"}, "Water")
    ]
)
def test_create_object(data, name):
    body = {
        "data": data,
        "name": name
    }
    response = requests.post(work_url, json=body, timeout=10)
    assert response.status_code == 201
    response_json = response.json()
    assert response_json["data"] == data
    assert response_json["name"] == name
    requests.delete(f"{work_url}/{response_json['id']}")


@pytest.mark.medium
def test_put_object(new_object):
    body = {
        "data": {"color": "white", "size": "short"},
        "name": "new_name"
    }
    response = requests.put(f"{work_url}/{new_object}", json=body, timeout=10)
    assert response.status_code == 200
    assert response.json()["name"] == "new_name"
    assert response.json()["data"] == body["data"]


def test_patch_object(new_object):
    body = {
        "data": {"color": "white", "size": "short"}
    }
    response = requests.patch(f'{work_url}/{new_object}', json=body, timeout=10)
    assert response.status_code == 200
    assert response.json()["data"] == body["data"]


def test_delete_object(new_object):
    delete_response = requests.delete(f'{work_url}/{new_object}', timeout=10)
    assert delete_response.status_code == 200
