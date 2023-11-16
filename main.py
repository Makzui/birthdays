from datetime import date, datetime, timedelta

def get_birthdays_per_week(users, current_date = datetime.now()):
    if not users:  # Перевірка на пустий список користувачів
        return {}  # Повертаємо порожній словник

    # Отримуємо поточну дату
    today = current_date
    current_year = today.year

    # Створюємо словник для збереження імен користувачів за днями тижня
    birthdays_per_week = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}

    # Цикл по користувачам
    for user in users:
        name = user['name']
        birthday = user['birthday']

        birthday_in_current_year = datetime(today.year, birthday.month, birthday.day) 
        birthday_in_last_year = datetime(today.year - 1, birthday.month, birthday.day)
        # Якщо в минулому році ДР був за тиждень до поточного року. Переносимо привітання на понеділок   
        # Додаємо кілкість днів до ДР в минулому році шоб вийшов наступний тиждень і якщо наступний тиждень це поточний рік 
        # то др відбувся на тиждень до поточного року і переносимо на понеділок
        # тут краще можно зробити перевірку 
        # "І майте на увазі що може бути, наприклад, випадок коли сьогодні 26.12, а день народження 01.01. Тоді день народження переноситься на наступний рік"
        day_of_bf_last_year = birthday_in_last_year.weekday() + (7 - birthday_in_last_year.timetuple().tm_yday) + 1
        target_datetime = datetime(datetime.now().year, 1, 1) + timedelta(days=day_of_bf_last_year - 1)

        if target_datetime.year == today.year:
             birthdays_per_week['Monday'].append(name)
             continue

        day_week_bf = birthday_in_current_year.weekday()
        number_of_week_current = today.isocalendar()[1]
        birthday_week = birthday_in_current_year.isocalendar()[1]

        
        # Пропускаємо др якщо день не на наступному тижні або не на цьому
        # if(not (birthday_week == number_of_week_current + 1 or number_of_week_current == birthday_week)):
        if birthday_week not in (number_of_week_current + 1, number_of_week_current):
            continue

        if day_week_bf >= 5:
            day_week_bf = 0  # Понеділок


        # Визначаємо день тижня, коли народився користувач
        # Додаємо ім'я користувача до відповідного дня тижня
        if day_week_bf == 0:  # Понеділок
            birthdays_per_week['Monday'].append(name)
        elif day_week_bf == 1:  # Вівторок
            birthdays_per_week['Tuesday'].append(name)
        elif day_week_bf == 2:  # Середа
            birthdays_per_week['Wednesday'].append(name)
        elif day_week_bf == 3:  # Четвер
            birthdays_per_week['Thursday'].append(name)
        elif day_week_bf == 4:  # П'ятниця
            birthdays_per_week['Friday'].append(name)
    
    # філтр ключів, які не мають значень
    for key in list(birthdays_per_week):
        if not birthdays_per_week[key]:
            del birthdays_per_week[key]
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



