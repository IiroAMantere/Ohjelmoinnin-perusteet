from datetime import datetime
from typing import List

MONTHS = (
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
)

WEEKDAYS = (
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"
)


def readTimestamps(PFilename: str, PTimestamps: List[datetime]) -> None:
    """Reads timestamps from a file and stores them into PTimestamps list."""

    PTimestamps.clear()

    with open(PFilename, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            # Format in dataset: YYYY-MM-DD HH:MM
            dt = datetime.strptime(line, "%Y-%m-%d %H:%M")
            PTimestamps.append(dt)


def calculateYears(PYear: int, PTimestamps: List[datetime]) -> int:
    """Counts timestamps that occur in the given year."""
    return sum(1 for ts in PTimestamps if ts.year == PYear)


def calculateMonths(PMonth: str, PTimestamps: List[datetime]) -> int:
    """Counts timestamps in a given month (full month name)."""
    if PMonth not in MONTHS:
        return 0

    month_index = MONTHS.index(PMonth) + 1  # datetime months are 1–12
    return sum(1 for ts in PTimestamps if ts.month == month_index)


def calculateWeekdays(PWeekday: str, PTimestamps: List[datetime]) -> int:
    """Counts timestamps in a given weekday (full weekday name)."""
    if PWeekday not in WEEKDAYS:
        return 0

    weekday_index = WEEKDAYS.index(PWeekday)  # Monday = 0
    return sum(1 for ts in PTimestamps if ts.weekday() == weekday_index)
