from typing import List

def readValuesFromFile(PFilename: str) -> List[float]:
    values: List[float] = []

    with open(PFilename, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue  # skip empty rows
            values.append(float(line))

    return values


def calcSum(PValues: List[float]) -> float:
    return round(sum(PValues), 1)


def calcAverage(PValues: List[float]) -> float:
    if len(PValues) == 0:
        return 0.0
    avg = sum(PValues) / len(PValues)
    return round(avg, 1)
