def get_years_word(age: int) -> str:
    if 11 <= age % 100 <= 19:
        return "лет"
    last_digit = age % 10
    if last_digit == 1:
        return "год"
    elif last_digit in (2, 3, 4):
        return "года"
    else:
        return "лет"


pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите его возраст: "))
pet_name = input("Введите его кличку: ")
owner_name = input("Введите имя владельца: ")

pets = {}

pet_info = {
    "Вид питомца": pet_type,
    "Возраст питомца": f"{pet_age} {get_years_word(pet_age)}",
    "Имя владельца": owner_name
}

pets[pet_name] = pet_info

for pet in pets.keys():
    pet_data = list(pets[pet].values())
    print(pet_data)
    print(f"Это {pet_data[0]} по кличке \"{pet}\". Возраст: {pet_data[1]}. Имя владельца: {pet_data[2]}")
