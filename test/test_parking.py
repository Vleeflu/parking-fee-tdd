import pytest
from src.fare import compute_bus_fare


def test_children_under_2_free():
    assert compute_bus_fare(
        age=1,
        day_type="weekday",
        hour=10,
        trip_duration=20,
        is_public_holiday=False
    ) == 0


def test_child_half_fare():
    assert compute_bus_fare(
        age=10,
        day_type="weekday",
        hour=10,
        trip_duration=20,
        is_public_holiday=False
    ) == 1.5


def test_senior_half_fare():
    assert compute_bus_fare(
        age=70,
        day_type="weekday",
        hour=10,
        trip_duration=20,
        is_public_holiday=False
    ) == 1.5


def test_adult_regular_fare():
    assert compute_bus_fare(
        age=30,
        day_type="weekday",
        hour=10,
        trip_duration=20,
        is_public_holiday=False
    ) == 3


def test_peak_hour_surcharge():
    assert compute_bus_fare(
        age=30,
        day_type="weekday",
        hour=8,
        trip_duration=20,
        is_public_holiday=False
    ) == 4.5


def test_weekend_flat_fare():
    assert compute_bus_fare(
        age=30,
        day_type="weekend",
        hour=10,
        trip_duration=20,
        is_public_holiday=False
    ) == 2


def test_short_trip_free():
    assert compute_bus_fare(
        age=30,
        day_type="weekday",
        hour=11,
        trip_duration=3,
        is_public_holiday=False
    ) == 0


def test_public_holiday_override():
    assert compute_bus_fare(
        age=30,
        day_type="weekday",
        hour=8,
        trip_duration=20,
        is_public_holiday=True
    ) == 5


def test_public_holiday_child():
    assert compute_bus_fare(
        age=10,
        day_type="weekday",
        hour=8,
        trip_duration=20,
        is_public_holiday=True
    ) == 3.5


def test_invalid_age():
    with pytest.raises(ValueError):
        compute_bus_fare(
            age=-1,
            day_type="weekday",
            hour=10,
            trip_duration=20,
            is_public_holiday=False
        )