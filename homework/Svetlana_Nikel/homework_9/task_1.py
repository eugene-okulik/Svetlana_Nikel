import datetime

my_date = 'Jan 15, 2023 - 12:05:33'
python_date = datetime.datetime.strptime(my_date, '%b %d, %Y - %H:%M:%S')
our_date_1 = python_date.strftime('%B')
our_date_2 = python_date.strftime('%d.%m.%Y, %H:%M')
print(our_date_1)
print(our_date_2)
