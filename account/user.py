import json
import hashlib
import time


class Account:
    def __init__(self, username: str, password: str):
        if not any(c.islower() for c in password) or len(password) < 7:
            raise ValueError("Пароль должен содержать строчную букву и быть длиннее 6 символов.")
        self.username = username
        self.password = password
        self.hashed_password = hashlib.sha256(password.encode()).hexdigest()

    def save_data(self) -> None:
        try:
            with open("accounts.json", "r") as file:
                accounts_data = json.load(file)
        except FileNotFoundError:
            accounts_data = {"accounts": []}

        accounts_data["accounts"].append({"username": self.username, "hashed_password": self.hashed_password})

        with open("accounts.json", "w") as file:
            json.dump(accounts_data, file, indent=4)

    @staticmethod
    def load_account(username: str, password: str, attempts: int = 0) -> 'Account' or None:
        if attempts > 3:
            print("Попробуйте снова через 5 минут.")
            time.sleep(300)  # Ждем 5 минут
            return None

        try:
            with open("accounts.json", "r") as file:
                data = json.load(file)
                for account in data.get("accounts", []):
                    if account["username"] == username and account["hashed_password"] == hashlib.sha256(password.encode()).hexdigest():
                        return Account(account["username"], account["hashed_password"])

            return None

        except FileNotFoundError:
            print("Account not found")
            return None


# Пример использования класса Account
attempts = 0
while True:
    try:
        new_account = Account(input("Введите ваше имя пользователя: "), input("Введите ваш пароль: "))
        new_account.save_data()
        break
    except ValueError as e:
        print(e)
        attempts += 1
        if attempts > 2:
            print("Попробуйте снова через 5 минут.")
            time.sleep(300)  # Ждем 5 минут
            break

existing_account = Account.load_account(input("Введите имя пользователя для загрузки аккаунта: "),
                                        input("Введите ваш пароль: "), attempts)

if existing_account:
    print(f"Username: {existing_account.username}")
    print(f"Hashed Password: {existing_account.hashed_password}")

# Сравнение значения common_name с введенным словом пользователя
existing_plants = []
try:
    with open('plants.json', 'r') as file:
        existing_plants = json.load(file)
except FileNotFoundError:
    pass

# Сравнение значения common_name с введенным словом пользователя
user_input = input("Введите слово для сравнения: ")
found = any(plant.get("common_name") == user_input for plant in existing_plants)
if found:
    print(f"Слово '{user_input}' найдено в данных аккаунта.")
else:
    print(f"Слово '{user_input}' не найдено в данных аккаунта.")

plant_data = {"common_name": user_input}

# Открываем файл для записи или создаем новый, если не существует
new_plants_data = [plant_data]

# Открываем файл для записи
with open('items.json', 'w') as file:
    # Записываем только данные об этом растении
    json.dump(new_plants_data, file, indent=4)