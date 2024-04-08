import random
from datetime import datetime, timedelta

# список имен
def get_random_names():
    names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Isabel', 'Jack']
    random_names = random.choice(names)
    return random_names


# список фамилий
def get_random_surname():
    surnames = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
    random_surname = random.choice(surnames)
    return random_surname


# список день рождений
def get_random_birtday():
    # список для хранения дат
    dates = []

    # генерация 10 случайных дат
    for _ in range(1):
        # генерация случайной даты в диапазоне от 2000 до 2002 года
        random_date = datetime(random.randint(2000, 2002), random.randint(1, 12), random.randint(1, 28))
        # форматирование даты в нужный формат
        formatted_date = random_date.strftime("%b %d, %y")
        # добавление отформатированной даты в список
        dates.append(formatted_date)

    # вывод списка
    for date in dates:
        return date


# print(get_random_names(), get_random_surname(), get_random_birtday())