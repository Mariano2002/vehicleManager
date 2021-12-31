import math
from datetime import date
from datetime import datetime, timedelta

def days_between(d1, d2):
    return abs((d2 - d1).days)

hire_date = datetime.strptime('1/12/2021', '%d/%m/%Y')
end_date = datetime.strptime('6/1/2022', '%d/%m/%Y')
print(hire_date)
print(end_date)
print(hire_date < end_date)
# more_days = days_between(date.today(), hire_date) - math.floor(days_between(date.today(), hire_date)/7)
# weeks_to_pay = 0
to_pay = {}
start = hire_date
balance = 0
data = []
day_price = 20
while True:
    print(start + timedelta(days=6))
    end = start + timedelta(days=6)

    if start > datetime.today():
        break
    elif end < end_date:
        data.append([start, end])
    else:
        data.append([start, end_date])
        break

    start = start + timedelta(days=7)

for i in data:
    balance += (days_between(i[-1], i[0])+1)*day_price
print(balance)