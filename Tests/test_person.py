def person_type(person):
    return "douchbag" if person == "Donald Trump" else "dencent human being"

def rank_height(h_cm):
    return "tall" if h_cm * 2.54 > 173 else "not tall"

def relative_age(howold):
    return "old" if howold >= 60 else "young"


def test_person():
    person = "Donald Trump"
    person_character = person_type(person)
    assert person_character == 'douchbag'

def test_relative_age():
    assert relative_age(70) == "old"

def test_person_tall_short(height_cm=180):
    assert rank_height(height_cm) == "tall"