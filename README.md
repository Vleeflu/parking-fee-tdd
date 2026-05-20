# Online Parking Fee System

Hands-on assignment — **Git Collaboration & Test-Driven Development (TDD)**.

Implements `calculate_parking_fee(vehicle_type, parking_duration, day_type, is_public_holiday)`
following a strict RED → GREEN → REFACTOR loop.

## Business rules

| # | Rule |
|---|---|
| 1 | Vehicles parked for **under 1 hour** are free |
| 2 | Motorcycles: **$2** |
| 3 | Cars: **$5** |
| 4 | Trucks: **$10** |
| 5 | Weekend surcharge: **+$3** |
| 6 | Public holiday: **flat $15** for all vehicles |
| 7 | Parking duration **> 24 hours** is invalid (raises `ValueError`) |

### Rule precedence (resolved ambiguities)

Top-down — first match wins:

1. **Validation**: reject unknown `vehicle_type`, unknown `day_type`, or `parking_duration` outside `[0, 24]`.
2. **Under-1-hour rule**: free, overrides everything else (consistent with "Children under 2 ride free" pattern from the bus-fare reference).
3. **Public holiday**: flat $15, overrides weekend surcharge ("flat rate for *all* vehicles").
4. **Base + weekend**: vehicle base rate, plus $3 if weekend.

## Project layout

```
parking-fee-tdd/
├── pyproject.toml
├── README.md
├── .gitignore
├── src/
│   ├── __init__.py
│   └── parking.py
└── test/
    ├── __init__.py
    └── test_parking.py
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## Running tests

```bash
python -m pytest -v
```

## Git workflow

- `main` is protected — no direct pushes. All changes via Pull Request with ≥1 approval.
- Each member works on a `feature/<name>` branch.
- Commit messages follow the convention:
  - `test:` — add a failing test (RED)
  - `feat:` — implement the rule (GREEN)
  - `refactor:` — improve without changing behavior
  - `fix:` — bug fix or conflict resolution
  - `chore:` — non-code maintenance

## Group

| Member | Branch | Owned rules |
|---|---|---|
| A | `feature/base-rates` | Base rates + input validation |
| B | `feature/free-and-weekend` | Under-1h free + weekend surcharge |
| C | `feature/public-holiday` | Public holiday flat rate + precedence |
