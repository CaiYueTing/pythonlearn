# import flask_testing
# import unittest
# from app import app
# from app.user.models import User


# class userTest(flask_testing.TestCase):
#     def setUp(self):
#         return app.run()

#     def test_create_user(self):
#         user = User('Test name', 'Test@email', 1)
#         uid = user.create()
#         usr = User.getUserById(uid)
#         self.assertEqual(uid, usr.id)


# if __name__ == '__main__':
#     unittest.main()
import pytest
import json
from app import app


@pytest.fixture(scope='session')
def client():
    app.config['Testing'] = True

    with app.test_client() as client:
        with app.app_context():
            app.test_client()
        yield client


def create_user(client, username, email, role):
    return client.post('/api/v1/users/', data=dict(
        name=username,
        email=email,
        role=role
    ), follow_redirects=True)


def get_user(client):
    return client.get('/api/v1/users/')


def update_user(client, userid, username, email, role):
    return client.patch('/api/v1/users/' + str(userid), data=dict(
        name=username,
        email=email,
        role_id=role
    ), follow_redirects=True)


def delete_user(client, user_id):
    return client.delete('/api/v1/users/' + str(user_id))


def test_create_user(client):
    response = create_user(client, 'Test name', 'Test@email', 1)
    data = json.loads(response.data.decode())
    assert data['data']['status'] == 'success'
    assert response.status_code == 201


def test_get_user(client):
    response = get_user(client)
    assert response.status_code == 200


def test_update_user(client):
    users = get_user(client)
    data = json.loads(users.data.decode())
    last_user = data['data'][0]['user']
    update_user(
        client, last_user['id'], 'new name', 'newmail@mail', '2'
    )
    users = get_user(client)
    data = json.loads(users.data.decode())
    last_user = data['data'][0]['user']
    assert last_user['name'] == 'new name'
    assert users.status_code == 200


def test_delete_user(client):
    users = get_user(client)
    data = json.loads(users.data.decode())
    last_user = data['data'][0]['user']
    response = delete_user(client, last_user['id'])
    assert response.status_code == 204
