import pytest
from src.parking import calculate_parking_fee

def test_motorcycle_base_fee():
    assert calculate_parking_fee("motorcycle", 2, "weekday", False) == 2

def test_car_base_fee():
    assert calculate_parking_fee("car", 5, "weekday", False) == 5

def test_truck_base_fee():
    assert calculate_parking_fee("truck", 10, "weekday", False) == 10

def test_unknown_vehicle_type_invalid():
    with pytest.raises(ValueError):
        calculate_parking_fee("bicycle", 2, "weekday", False)

def test_duration_above_24_invalid():
    with pytest.raises(ValueError):
        calculate_parking_fee("car", 25, "weekday", False)

def test_negative_duration_invalid():
    with pytest.raises(ValueError):
        calculate_parking_fee("car", -1, "weekday", False)

def test_unknown_day_type_invalid():
    with pytest.raises(ValueError):
        calculate_parking_fee("car", 2, "monday", False)

def test_under_one_hour_is_free():
    assert calculate_parking_fee("car", 0.5, "weekday", False) == 0

def test_weekend_surcharge_car():
    assert calculate_parking_fee("car", 2, "weekend", False) == 8

def test_weekend_surcharge_truck():
    assert calculate_parking_fee("truck", 2, "weekend", False) == 13