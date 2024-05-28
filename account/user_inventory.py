import json
import re


def authenticate_user():
    """
    Проверяет аутентификацию пользователя, используя данные из файла users.json.
    """
    while True:
        username = input("Введите имя пользователя: ")
        if not username:
            print("Имя пользователя не может быть пустым.")
            continue

        password = input("Введите пароль: ")
        if not password:
            print("Пароль не может быть пустым.")
            continue

        try:
            with open('users.json', 'r') as F:
                users = json.load(F)
                if username in users and users[username]["password"] == password:
                    print(f"Добро пожаловать, {username}!")
                    return True
                else:
                    print("Неверный логин или пароль.")
                    continue  # Повторить ввод данных
        except FileNotFoundError:
            print("Файл пользователей не найден.")
            return False  # Выйти из функции


# Пример использования
top_plant_name = ["Роза", "Лилия", "Тюльпан", "Орхидея"]

# Запись значений из top_plant_name в JSON файл (предполагаем, что users.json уже существует)
with open('plants_inventory.json', 'w') as f:
    json.dump(top_plant_name, f, indent=4)

# Запрашиваем имя пользователя и пароль
if authenticate_user():
    # Если аутентификация прошла успешно, выводим значения из plants.json
    with open('plants_inventory.json', 'r') as f:
        plants = json.load(f)
        print("Теперь растение есть в твоем инвентаре:")
        for plant in plants:
            print(plant)
