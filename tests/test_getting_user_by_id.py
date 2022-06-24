from allure import step
from hamcrest import assert_that, has_entries
from pytest import mark

from helpers.rest import get_list_of_ids_by_gender


class TestGettingListsOfIdsByGender:
    @mark.parametrize('gender', ('male', 'female'))
    def test_getting_lists_of_ids_by_gender_valid_data(self, gender):
        with step(f'Отправка запроса для получения списка идентификаторов пользователей по критерию gender={gender}'):
            response = get_list_of_ids_by_gender(gender)

        with step('Проверка ответа сервера'):
            assert response.status_code == 200, response.text
            assert_that(response.json(), has_entries(
                success=True,
                errorCode=0,
                errorMessage=None,
                result=[]
            ), 'Тело ответа не соответствует ожидаемому')

    def test_getting_lists_of_ids_by_gender_non_valid_data(self):
        gender = 'magic'
        with step(f'Отправка запроса для получения списка идентификаторов пользователей по критерию gender={gender}'):
            response = get_list_of_ids_by_gender('gender')

        with step('Проверка ответа сервера'):
            assert response.status_code == 400, response.text
            assert_that(response.json(), has_entries(
                success=False,
                errorCode=400,
                errorMessage='Bad request',
                result=None
            ), 'Тело ответа не соответствует ожидаемому')
