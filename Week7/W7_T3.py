WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)

def readFile(PFilename: str, PRows: list[str]) -> None:
    print(f"Reading file \"{PFilename}\".")
    # 0. Clear PRows list just in case
    PRows.clear()
    # 1. Open filehandle
    f = open(PFilename, "r")
        # Skip header row
    header = f.readline()
    # 2.1. Skip first line (header row)
    next(f)
    # 2.2. Check if line is empty '\n'
    for line in f:
        clean = line.rstrip("\n")       # Remove newline at the end
        if not clean.strip():           # Skip empty lines
                continue
        PRows.append(clean)

    # 2.3. Add non empty datarow without newline at the end.

    # 3. Close filehandle 
    f.close()
    return None

def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    # Append results to the PResults list

    # Initialise helper list 
    WeekdayTimestampAmount: list[int] = [0, 0, 0, 0, 0, 0, 0]
    for row in PRows:
         for i, weekday in enumerate(WEEKDAYS):
              if row.startswith(weekday):
                   WeekdayTimestampAmount[i] += 1
                   break

    # Iterate rows with i
    #   Iterate WEEKDAYS with j
    #      Check if the row starts with the weekday name
    #          Count the day in proper place
    # Iterate WEEKDAYS with i and append the daily results
    PResults.clear()
    PResults.append("### Timestamp analysis ###")
    for weekday, count in zip(WEEKDAYS, WeekdayTimestampAmount):
        PResults.append(f" - {weekday} {count} stamps")
    PResults.append("### Timestamp analysis ###")


    # Clear the helper list
    return None

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    # Iterate results and print for the user
    for line in PResults:
         print(line)
    return None

def main() -> None:
    # 1. Initialise
    # 1.1. Initialise rows list
    Rows: list[str]= []
    # 1.2. Initialise results list
    Results: list[str]= []
    # 2. Operate
    print("Program starting.")
    # 2.1. Ask user to define filename
    Filename = input("Insert filename: ")
    # 2.2. Read file
    readFile(Filename, Rows)
    print(f"Reading file \"{Filename}.\"")
    analyseTimestamps(Rows, Results)
    # 2.3. Analyse rows
    # 2.3. Display results
    displayResults(Results)
    # 3. Cleanup
    # 3.1. Clear lists
    Rows.clear()
    Results.clear()

    print("Program ending.")
    return None

main()