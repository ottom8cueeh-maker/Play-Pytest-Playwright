import datetime


def test_day_of_week():
    """test the day of the week for today's date"""
    # Get today's date
    today = datetime.date.today()

    # Get the day of the week
    assert today.strftime("%A") == "Thursday"

  
def test_is_leap_year(year=2024):
    """test if a given year is a leap year"""
    assert (year % 4 == 0)
    assert (year % 100 != 0 or year % 400 == 0)
