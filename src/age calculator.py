# The user will enter two different strings "name" and "birthdate".
# Given task is to calculate the age of the person in months and days.

name = input('Enter your name: ')
birth_date = str(input('Enter your birthdate in dd/mm/yyyy format: '))

current_day = '24'
current_month = '01'
current_year = '2022'

birth_day = (birth_date[0:2])
birth_month = (birth_date[3:5])
birth_year = (birth_date[6:])

birth_year = int(birth_year)
current_year = int(current_year)
birth_month = int(birth_month)
current_month = int(current_month)
birth_day = int(birth_day)
current_day = int(current_day)

if birth_year <= current_year:
    if birth_month <= current_month:
        if birth_day <= current_day:
            years = current_year - birth_year
            months = current_month - birth_month
            days = current_day - birth_day
        elif birth_day > current_day:
            years = current_year - birth_year
            months = (current_month - birth_month) - 1
            days = 31 + (current_day - birth_day)
    elif birth_month > current_month:
        if birth_day <= current_day:
            years = current_year - birth_year - 1
            months = 12 + (current_month - birth_month)
            days = current_day - birth_day
        elif birth_day > current_day:
            years = current_year - birth_year - 1
            months = 12 + (current_month - birth_month) - 1
            days = 31 + (current_day - birth_day)
    total_months = months + (12 * years)
    print(f'Hi, {name}. As of today, your age is {total_months} months and {days} days.')

else:
    print('INVALID INPUT. Birthdate cannot exceed the current date.')
