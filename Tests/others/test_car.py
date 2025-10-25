def calculate_fuel_economy(litres_used, km_travelled):
    return 100 / km_travelled * litres_used

def calculate_distance_by_fuel(fuel_left, fuel_econ):
    return fuel_left/fuel_econ * 100        # distance can travel


def test_enough_fuel_for_trip(tripkm=100):
    assert calculate_distance_by_fuel(10, 5) >= tripkm

def test_fuel_economy():
    # A good fuel consumption rate is below (<) 6 litres per 100 kilometers
    assert calculate_fuel_economy(4, 90) <= 6

def dummy_func():
    assert 'a' == 'a'

def test_coder_changes():
    assert 1==1