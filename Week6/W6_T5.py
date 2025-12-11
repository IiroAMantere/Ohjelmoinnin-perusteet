import os
print("Current working directory:", os.getcwd())


SEPARATOR = ";"


def readValues(PFilename: str) -> str:
    """Reads numbers from the file and returns them as a semicolon-separated string."""
    values = ""

    with open(PFilename, "r") as file:
        for line in file:
            num = line.strip()

            if values == "":
                values = num
            else:
                values += SEPARATOR + num

    return values


def analyseNumbers(PValues: str) -> str:
    """Analyses the numbers and returns a semicolon-separated result string."""

    parts = PValues.split(SEPARATOR)
    numbers = [int(n) for n in parts]

    count = len(numbers)
    total = sum(numbers)
    greatest = max(numbers)
    average = total / count

    # Return results in CSV (semicolon-separated)
    result = (
        str(count)
        + SEPARATOR
        + str(total)
        + SEPARATOR
        + str(greatest)
        + SEPARATOR
        + "{:.2f}".format(average)
    )

    return result


def printReport(PFilename: str, PResults: str) -> None:
    """Prints the analysis report in required format."""
    print("#### Number analysis - START ####")
    print(f'File "{PFilename}" results:')
    print("Count;Sum;Greatest;Average")
    print(PResults)
    print()
    print("#### Number analysis - END ####")


def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")


    values = readValues(filename)


    results = analyseNumbers(values)


    printReport(filename, results)

    print("Program ending.")


if __name__ == "__main__":
    main()
