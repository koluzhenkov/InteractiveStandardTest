from allure import step
from hamcrest import assert_that, has_entries
from pytest import mark

from helpers.rest import get_user_by_id


def test_getting_user_by_gender_existing_user():
    user_id = 5
    with step(f'Отправка запроса для получения информации о пользователе по его идентификатору: {user_id}'):
        response = get_user_by_id(user_id)

    with step('Проверка ответа сервера'):
        assert response.status_code == 200, response.text
        assert_that(response.json(), has_entries(
            success=True,
            errorCode=0,
            errorMessage=None,
            result={
                'id': 5,
                'name': 'Ann',
                'gender': 'female',
                'age': 22,
                'city': 'Novosibirsk',
                'registrationDate': '2017-04-12T18:30:01.000000021'
            }
        ), 'Тело ответа не соответствует ожидаемому')


@mark.parametrize('user_id', (0, 6))
def test_getting_user_by_gender_non_existing_user(user_id):
    with step(f'Отправка запроса для получения информации о пользователе по его идентификатору: {user_id}'):
        response = get_user_by_id(user_id)

    with step('Проверка ответа сервера'):
        assert response.status_code == 404, response.text
        assert_that(response.json(), has_entries(
            success=False,
            errorCode=404,
            errorMessage='Not found',
            result=None
        ), 'Тело ответа не соответствует ожидаемому')


@mark.parametrize('user_id', (-6, 'text'))
def test_getting_user_by_gender_non_valid_format(user_id):
    with step(f'Отправка запроса для получения информации о пользователе по его идентификатору: {user_id}'):
        response = get_user_by_id(user_id)

    with step('Проверка ответа сервера'):
        assert response.status_code == 400, response.text
        assert_that(response.json(), has_entries(
            success=False,
            errorCode=400,
            errorMessage='Bad request',
            result=None
        ), 'Тело ответа не соответствует ожидаемому')
