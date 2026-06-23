import collections


pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел",
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша",
        },
    },
}


def get_suffix(age: int) -> str:
    if 11 <= age % 100 <= 19:
        return "лет"
    last_digit = age % 10
    if last_digit == 1:
        return "год"
    elif last_digit in (2, 3, 4):
        return "года"
    else:
        return "лет"


def get_pet(pet_id):
    """функция, с помощью которой вы получите информацию о питомце в виде словаря
    сделайте проверку, если питомца с таким ID нету в нашей "базе данных"
    верните в этом случае False
    а если питомец всё же есть в "базе данных" - верните информацию о нём"""

    return pets[pet_id] if pet_id in pets.keys() else False

def input_pet_data():
    pet_type = input("Введите вид питомца: ")
    pet_age = int(input("Введите его возраст: "))
    pet_name = input("Введите его кличку: ")
    owner_name = input("Введите имя владельца: ")

    return {
        'pet_type': pet_type,
        'pet_age': pet_age,
        'pet_name': pet_name,
        'owner_name': owner_name
    }

def create_pet(pet_data):
    pet_type = pet_data['pet_type']
    pet_age = pet_data['pet_age']
    pet_name = pet_data['pet_name']
    owner_name = pet_data['owner_name']

    pet_info = {
        "Вид питомца": pet_type,
        "Возраст питомца": f"{pet_age} {get_suffix(pet_age)}",
        "Имя владельца": owner_name,
    }

    return {pet_name: pet_info}


def create():
    last = collections.deque(pets, maxlen=1)[0]
    pets[last + 1] = create_pet(input_pet_data())


def update():
    pet_id = int(input("Введите индентификатор: "))
    if get_pet(pet_id):
        pets[pet_id] = create_pet(input_pet_data())


def delete():
    pet_id = int(input("Введите индентификатор: "))
    if pet_id in pets.keys():
        del pets[pet_id]


def read():
    pet_id = int(input("Введите индентификатор: "))
    print(get_pet(pet_id))

def pets_list():
    for pet in pets:
        print(pets.get(pet))

command = "process"

while command != "stop":
    command = input("Введите команду: ")
    if command == "read":
        read()
    elif command == "create":
        create()
    elif command == "delete":
        delete()
    elif command == "update":
        update()
    elif command == "list":
        pets_list()
