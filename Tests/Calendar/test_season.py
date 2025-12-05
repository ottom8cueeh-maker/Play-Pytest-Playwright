from datetime import datetime

def current_season(month):
    match month:
        case 'Dec'|'Jan'|'Feb':
            return "Winter"
        case 'Mar'|'Apr'|'May':
            return "Spring"
        case 'Jun'|'Jul'|'Aug':
            return "Summer"
        case 'Sep'|'Oct'|'Nov':
            return "Fall"
        case _:
            return "Unknown Month"

def test_current_season():
    curr_season = current_season(datetime.now().strftime("%b"))
    assert curr_season == "Winter"
