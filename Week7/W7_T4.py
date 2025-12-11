from dataclasses import dataclass

DELIMITER = ";"
@dataclass
class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float
    price: float

def readFile(PFilename: str, Timestamps: list[TIMESTAMP]) -> None:
    print(f'Reading file "{PFilename}".')

    Timestamps.clear()

    f = open(PFilename, "r")

    header = f.readline()

    for line in f:
        clean = line.rstrip()       
        if not clean.strip():        
            continue

        Columns = clean.split(DELIMITER)
        ts = TIMESTAMP(
            weekday = Columns[0],
            hour = Columns[1],
            consumption = float(Columns[2]),
            price = float(Columns[3])
        )
        Timestamps.append(ts)
        Columns.clear()

        f.close()

        return None

def displayTimestamps(Timestamps: list[TIMESTAMP]) -> None:
    print("Electricity usage:")
    for ts in Timestamps:
        total = ts.consumption * ts.price
        print(f" - {ts.weekday} {ts.hour}, price {ts.price:.2f} €, "
              f"consumption {ts.consumption:.2f} kWh, total {total:.2f} €")
    return None



def main() -> None:
    print("Program starting.")

    
    Timestamps: list[TIMESTAMP] = []

    
    Filename = input("Insert filename: ")

   
    readFile(Filename, Timestamps)

    
    displayTimestamps(Timestamps)

    print("Program ending.")
    return None

main()