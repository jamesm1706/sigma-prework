from datetime import datetime

birthday = datetime.strptime(input(
    'When is your birthday? Please separate dates with a hyphen: '), '%d-%m-%Y')
current_date = datetime.now()
age = current_date - birthday
age = age.days/365
print(f'You are {int(age)} years old.')
