import datetime
from datetime import timedelta

def test_day_of_week():
    # Get today's date
    today = datetime.date.today()


    anyday = today + timedelta(days=2)

    # Get the day of the week
    assert anyday.strftime("%A")=="Monday"


def test_is_leap_year(year=2024):
    assert (year % 4 == 0)
    assert (year % 100 != 0 or year % 400 == 0)
