#не проходить тест 3, 4, 5

from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    if not users:  # Перевірка на пустий список користувачів
        return {}  # Повертаємо порожній словник

    # Отримуємо поточну дату
    today = date.today()
    current_year = today.year

    # Створюємо словник для збереження імен користувачів за днями тижня
    birthdays_per_week = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}

    # Цикл по користувачам
    for user in users:
        name = user['name']
        birthday = user['birthday']

        # Розраховуємо різницю між поточною датою та днем народження
        days_until_birthday = (birthday - today).days

        # Визначаємо день тижня, коли народився користувач
        birthday_weekday = birthday.weekday()  # 0 - понеділок, 1 - вівторок, і так далі

        # Враховуємо випадок, коли день народження вже минув у цьому році
        if days_until_birthday < 0:
            # Перевіряємо, чи всі дні народження вже минули у цьому році
            all_birthday_passed = True
            for user in users:
                if (user['birthday'] - today).days >= 0:
                    all_birthday_passed = False
                    break

            if all_birthday_passed:
                return {}  # Усі дні народження вже минули

            # Розраховуємо рік народження наступного року
            next_year_birthday = birthday.replace(year=current_year + 1)
            days_until_birthday = (next_year_birthday - today).days

        # Визначаємо день тижня, коли користувач святкуватиме день народження
        birthday_weekday = (birthday_weekday + days_until_birthday) % 7

        # Враховуємо випадок, коли день народження випадає на минулі вихідні (суботу або неділю)
        if birthday_weekday >= 5:
            birthday_weekday = 0  # Понеділок

        # Додаємо ім'я користувача до відповідного дня тижня
        if birthday_weekday == 0:  # Понеділок
            birthdays_per_week['Monday'].append(name)
        elif birthday_weekday == 1:  # Вівторок
            birthdays_per_week['Tuesday'].append(name)
        elif birthday_weekday == 2:  # Середа
            birthdays_per_week['Wednesday'].append(name)
        elif birthday_weekday == 3:  # Четвер
            birthdays_per_week['Thursday'].append(name)
        elif birthday_weekday == 4:  # П'ятниця
            birthdays_per_week['Friday'].append(name)

    return birthdays_per_week




if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
