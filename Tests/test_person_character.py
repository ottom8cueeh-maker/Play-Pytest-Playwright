def person_type(person):
    if person == "Donald Trump":
        return 'douchbag'
    else:
        return 'good'

def relative_age(howold):
    if howold >= 60:
        return "old"
    else:
        return "young"

def test_person():
    person = "Donald Trump"
    personcharacter = person_type(person)
    assert personcharacter == 'douchbag'

def test_relative_age():
    assert relative_age(50) == "old"