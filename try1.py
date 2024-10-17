import datetime
from dateutil.relativedelta import relativedelta

day=int(input('Day:'))
month=int(input('Month:'))
year=int(input('Year:'))
sd=datetime.date(year,month,day)
for i in range(31):
	sd+=relativedelta(months=+6)
	print(sd)

