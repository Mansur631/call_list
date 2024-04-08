import random
from datetime import datetime, timedelta

# Список имен
def get_random_names():
    names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Isabel', 'Jack']
    random_names = random.choice(names)
    return random_names


# Список фамилий
def get_random_surname():
    surnames = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
    random_surname = random.choice(surnames)
    return random_surname


# Список день рождений
def get_random_birtday():
    # Список для хранения дат
    dates = []

    # Генерация 10 случайных дат
    for _ in range(1):
        # Генерация случайной даты в диапазоне от 2000 до 2002 года
        random_date = datetime(random.randint(2000, 2002), random.randint(1, 12), random.randint(1, 28))
        # Форматирование даты в нужный формат
        formatted_date = random_date.strftime("%B %d, %Y")
        # Добавление отформатированной даты в список
        dates.append(formatted_date)

    # Вывод списка
    for date in dates:
        return date


# print(get_random_names(), get_random_surname(), get_random_birtday())