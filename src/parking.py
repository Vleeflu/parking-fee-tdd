_BASE_RATES = {"motorcycle": 2, "car": 5, "truck": 10}
_VALID_DAYS = {"weekday", "weekend"}

def calculate_parking_fee(vehicle_type, parking_duration, day_type, is_public_holiday):
    if vehicle_type not in _BASE_RATES:
        raise ValueError(f"Unknown vehicle_type: {vehicle_type!r}")
    if day_type not in _VALID_DAYS:
        raise ValueError(f"Unknown day_type: {day_type!r}")
    if parking_duration < 0 or parking_duration > 24:
        raise ValueError("parking_duration must be in [0, 24]")
    if parking_duration < 1:
        return 0
    return _BASE_RATES[vehicle_type]