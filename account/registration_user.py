import json


def register_user():
    """
    Регистрирует нового пользователя, проверяя пароль на соответствие требованиям.
    """

    while True:
        username = input("Введите имя пользователя,пример user123: ")
        if not username:
            print("Имя пользователя не может быть пустым.")
            continue

        password = input("Введите пароль (не менее 6 символов, с одной строчной буквой),пример Password1: ")
        if not any(c.islower() for c in password) or len(password) < 7:
            print("Пароль не соответствует требованиям. Попробуйте снова.")
            continue

        # Проверка, не существует ли уже пользователя с таким именем
        try:
            with open('users.json', 'r') as f:
                users = json.load(f)
                if username in users:
                    print(f"Пользователь с именем {username} уже существует. Выберите другое имя.")
                    continue
        except FileNotFoundError:
            pass  # Файл users.json не существует, значит пользователя с таким именем нет

        # Создание словаря пользователя
        user_data = {
            "username": username,
            "password": password
        }

        # Запись данных в JSON файл
        try:
            with open('users.json', 'r+') as f:
                try:
                    users = json.load(f)
                except json.JSONDecodeError:
                    users = {}
                users[username] = user_data
                f.seek(0)
                json.dump(users, f, indent=4)
                print(f"Пользователь {username} успешно зарегистрирован!")
                break
        except FileNotFoundError:
            with open('users.json', 'w') as f:
                json.dump({username: user_data}, f, indent=4)
                print(f"Пользователь {username} успешно зарегистрирован!")
                break


if __name__ == "__main__":
    register_user()
