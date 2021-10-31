from api import PetFriends
from settings import *
import os

pf = PetFriends()


def test_get_api_key_invalid_email(email=wrong_user_email, password=user_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_api_key_invalid_password(email=user_email, password=wrong_user_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_add_pet_no_photo(name='Пух', animal_type='Страус',
                                     age='3'):
    _, auth_key = pf.get_api_key(user_email, user_password)
    status, result = pf.add_information_about_pet_no_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name


def test_delete_non_existing_pet():
    _, auth_key = pf.get_api_key(user_email, user_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/Ostrich.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    original_length = len(my_pets['pets'])
    pet_id = "9C4AEC87-37A4-4EE0-8F1B-3170C816536C"
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200
    #Проверяю изменилось ли число питомцев
    assert original_length == len(my_pets['pets'])


def test_add_new_pet_with_no_picture(name='Барбоскин', animal_type='двортерьер',
                                     age='4'):

    pet_photo = os.path.join(os.path.dirname(__file__))
    _, auth_key = pf.get_api_key(user_email, user_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name


def test_get_all_pets_with_invalid_key(_filter=''):
    status, result = pf.get_list_of_pets("ea738148a1f19838e1c5d1413877f3691a3731380e733e877b0ae729", _filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_successful_update_non_existing_pet_info(name='Мурзик', animal_type='Котэ', age=5):

    _, auth_key = pf.get_api_key(user_email, user_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = "9C4AEC87-37A4-4EE0-8F1B-3170C816536C"

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, pet_id, name, animal_type, age)

        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_update_photo_of_a_pet(pet_photo='images/Ostrich.jpg'):
    _, auth_key = pf.get_api_key(user_email, user_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_a_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
        assert status == 200
    else:
        raise Exception("There is no my pets")

def test_update_photo_of_a_pet_with_a_text_file(pet_photo='images/Text.txt'):
    _, auth_key = pf.get_api_key(user_email, user_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_a_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
        assert status == 200
    else:
        raise Exception("There is no my pets")

def test_add_new_pet_with_a_text_instead_of_a_photo(name='Барбоскин', animal_type='двортерьер',
                                     age='4', pet_photo='images/Text.txt'):

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(user_email, user_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
