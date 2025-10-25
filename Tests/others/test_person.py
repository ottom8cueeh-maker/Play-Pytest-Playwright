import pytest

def person_type(person):
    return "dumbass" if person == "Donald Trump" else "decent human being"

def rank_height(h_cm):
    return "tall" if h_cm * 2.54 > 173 else "not tall"

@pytest.mark.xfail
def relative_age(howold):
    return "old" if howold >= 60 else "young"

def test_person(person="Donald Trump"):
    assert person_type(person) == 'dumbass'

@pytest.mark.skip
def test_relative_age():
    assert relative_age(70) == "old"

def test_person_tall_short(height_cm=180):
    assert rank_height(height_cm) == "tall"