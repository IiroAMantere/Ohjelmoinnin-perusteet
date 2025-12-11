from dataclasses import dataclass

DELIMITER = ";"
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")



class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float
    price: float

class DAY_USAGE:
    weekday: str
    total_consumption: float
    total_cost: float

def readFile(PFilename: str, Timestamps: list[TIMESTAMP]) -> None:
    print(f'Reading file "{PFilename}".')
    Timestamps.clear()
    f = open(PFilename, "r")
    header = f.readline()  # skip header
    for line in f:
        clean = line.rstrip()  #Säilyttää siistityn version ilman ylimääräisiä merkkejä
        if not clean.strip():
            continue
        columns = clean.split(DELIMITER)
        ts = TIMESTAMP(
            weekday=columns[0],
            hour=columns[1],
            consumption=float(columns[2]),
            price=float(columns[3])
        )
        Timestamps.append(ts)
    f.close()
    return None

def analyseTimestamps(Timestamps: list[TIMESTAMP], DayUsages: list[DAY_USAGE]) -> None:
    print("Analysing timestamps.")

    DayUsages.clear()
    for weekday in WEEKDAYS:
        total_consumption = 0.0
        total_cost = 0.0
        for ts in Timestamps:
            if ts.weekday == weekday:
                total_consumption += ts.consumption
                total_cost += ts.consumption * ts.price
        day_usage = DAY_USAGE(
            weekday=weekday,
            total_consumption=total_consumption,
            total_cost=total_cost
        )
        DayUsages.append(day_usage)
    return None

def displayResults(DayUsages: list[DAY_USAGE], Results: list[str]) -> None:
    print("Displaying results.")
    Results.clear()
    Results.append("### Electricity consumption summary ###")
    for day in DayUsages:
        Results.append(f" - {day.weekday} usage {day.total_consumption:.2f} kWh, cost {day.total_cost:.2f} €")
    Results.append("### Electricity consumption summary ###")
    for line in Results:
        print(line)
    return None

def main() -> None:
    print("Program starting.")

    # Initialise lists
    Timestamps: list[TIMESTAMP] = []
    DayUsages: list[DAY_USAGE] = []
    Results: list[str] = []

    Filename = input("Insert filename: ").strip()
    readFile(Filename, Timestamps)  #Lukee tiedoston
    analyseTimestamps(Timestamps, DayUsages)  #Analysoi tiedoston
    displayResults(DayUsages, Results)  #Tulokset

    Timestamps.clear()
    DayUsages.clear()
    Results.clear()

    print("Program ending.")
    return None

main()