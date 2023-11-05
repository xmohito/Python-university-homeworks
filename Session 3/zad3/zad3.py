import calendar
from datetime import datetime, timedelta
import holidays


def last_working_day_in_month(year):
    pl_holidays = holidays.CountryHoliday('PL', years=year)
    for month in range(1, 13):
        for day in range(calendar.monthrange(year, month)[1], 0, -1):
            last_day = datetime(year, month, day)
            if last_day in pl_holidays:
                continue

            if last_day.weekday() == 6:
                days_to_subtract = 2
            elif last_day.weekday() == 5 and day == calendar.monthrange(year, month)[1]:
                days_to_subtract = 1
            else:
                days_to_subtract = 0

            adjusted_date = last_day - timedelta(days=days_to_subtract)

            while adjusted_date.weekday() in {5, 6}:
                adjusted_date -= timedelta(days=1)

            payment_date = adjusted_date.strftime('%d-%m-%Y')
            month_name = adjusted_date.strftime('%B')

            print(f'{month_name}: {payment_date}')
            break


try:
    year = int(input('Enter the year: '))
    last_working_day_in_month(year)
except ValueError:
    print("Invalid input.")
