# print today's date
# print yesterday's date
# ask a user to enter a date
# print the date one week from the date entered

from datetime import datetime, timedelta

today = datetime.now()

print('Today is: {}'.format(str(today)))

one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: {}'.format(str(yesterday)))

user_input = input('Input a date (dd/mm/yyyy): ')
user_date = datetime.strptime(user_input, '%d/%m/%Y')

one_week = timedelta(days=7)
weekf_user = user_date + one_week
print('The date one week from user inputed: {}'.format(weekf_user))
