from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):

    # Якщо список пустий, повертається пустий словник
    if users == []:
        return {}

    # Створюємо інтервал в тиждень від сьогоднішнього дня
    current_day = date.today()
    one_weeks_interval = timedelta(weeks=1)
    period_for_week = current_day + one_weeks_interval

    # Створюємо інтервал в два дні для ДН у вихідні, що пройшли
    two_days_interval = timedelta(days=2)
    period_for_weekend = current_day - two_days_interval

    # Створюємо словник зі списками за замовчуванням за допомогою dict comprehension
    birthdays_per_week = {current_date.strftime('%A'): [] for current_date in (current_day + timedelta(days=i) for i in range(7))}

    for user in users:

        # перевірка, чи пройшов день народження в цьому році
        if user['birthday'].replace(year=current_day.year) >=  period_for_weekend:
             
            new_year = user['birthday'].replace(year=current_day.year)
        
            # перевірка, чи сьогодні не понеділок
            if current_day.weekday != 0:

                if current_day < new_year < period_for_week:            

                        # перевірка, чи день народження - не субота чи неділя
                        if new_year.weekday() != 5 and new_year.weekday() != 6:
                            
                            # додавання до відповідного ключа імені
                            name = user['name'].split(" ")
                            birthdays_per_week[new_year.strftime('%A')].append(name[0])
                        
                        # якщо субота чи неділя, просто додає до ключа "Понеділок"
                        else:

                            # додавання імені до ключа ПОНЕДІЛОК
                                name = user['name'].split(" ")
                                birthdays_per_week['Monday'].append(name[0])

            # Якщо сьогодні понеділок
            else:

                # Якщо день народження - не вихідний 
                if new_year.weekday() != 5 and new_year.weekday() != 6:

                    # додавання до відповідного ключа імені
                    name = user['name'].split(" ")
                    birthdays_per_week[new_year.strftime('%A')].append(name[0])

                else: 
                
                    # якщо день народження в вихідні до цього понеділка
                    if period_for_weekend < new_year < current_day:
                        
                        # додавання імені до ключа ПОНЕДІЛОК
                        name = user['name'].split(" ")
                        birthdays_per_week['Monday'].append(name[0])
        
        # перевірка, чи пройшов день народження в цьому році
        if user['birthday'].replace(year=current_day.year) <  period_for_weekend:

            # створюємо дату на наступний рік
            new_year = user['birthday'].replace(year=current_day.year + 1)

            # перевірка, чи сьогодні не понеділок
            if current_day.weekday != 0:

                if current_day < new_year < period_for_week:            

                        # перевірка, чи день народження - не субота чи неділя
                        if new_year.weekday() != 5 and new_year.weekday() != 6:
                            
                            # додавання до відповідного ключа імені
                            name = user['name'].split(" ")
                            birthdays_per_week[new_year.strftime('%A')].append(name[0])
                        
                        # якщо субота чи неділя, просто додає до ключа "Понеділок"
                        else:

                            # додавання імені до ключа ПОНЕДІЛОК
                                name = user['name'].split(" ")
                                birthdays_per_week['Monday'].append(name[0])

            # Якщо сьогодні понеділок
            else:

                # Якщо день народження - не вихідний 
                if new_year.weekday() != 5 and new_year.weekday() != 6:

                    # додавання до відповідного ключа імені
                    name = user['name'].split(" ")
                    birthdays_per_week[new_year.strftime('%A')].append(name[0])

                else: 
                
                    # якщо день народження в вихідні до цього понеділка
                    if period_for_weekend < new_year < current_day:
                        
                        # додавання імені до ключа ПОНЕДІЛОК
                        name = user['name'].split(" ")
                        birthdays_per_week['Monday'].append(name[0])

            
 
    # Створюємо новий словник без порожніх списків
    filtered_birthdays = {day: tasks for day, tasks in birthdays_per_week  .items() if tasks}
         

    return filtered_birthdays    


if __name__ == "__main__":
    users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 12, 30).date()},
        {"name": "Will Gates", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Kill Gates", "birthday": datetime(1969, 1, 2).date()},
        {"name": "Till Gates", "birthday": datetime(1937, 12, 31).date()}
        ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")