import requests
import configuration
import data

def post_new_user():
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=data.user_body
    )

def get_user_token():
    response = post_new_user()
    return response.json()['authToken']

def post_new_kit(kit_body, auth_token):
    return requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers={'New Token': auth_token}
    )