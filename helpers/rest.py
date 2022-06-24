import requests

base_url = 'https://hr-challenge.interactivestandard.com'


def get_list_of_ids_by_gender(gender, baseurl=base_url):
    return requests.get(baseurl + f'/api/test/users?gender={gender}')


def get_user_by_id(user_id, baseurl=base_url):
    return requests.get(baseurl + f'/api/test/user/{user_id}')
