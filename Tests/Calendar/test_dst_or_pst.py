from datetime import datetime, timedelta
import pytz


def test_dst():
    # Choose your timezone
    tz = pytz.timezone("America/Vancouver")

    # Get current localized time
    nowdst = datetime.now(tz)

    # Check if DST is in effect
    assert nowdst.dst() != timedelta(0)

def test_not_pst():
    # Choose your timezone
    tz = pytz.timezone("America/Vancouver")

    # Get current localized time
    now = datetime.now(tz)

    # Check if standard time
    assert now.dst() != timedelta(0)
