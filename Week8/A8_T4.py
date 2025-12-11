import A8_T4Lib

def showOptions() -> None:
    print("Options:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")

def askChoice() -> int:
    return int(input("Your choice: "))

def main() -> None:
    print("Program starting.")

    timestamps = []

    filename = input("Insert filename: ")
    A8_T4Lib.readTimestamps(filename, timestamps)

    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.")
            break

        elif choice == 1:
            year = int(input("Insert year: "))
            amount = A8_T4Lib.calculateYears(year, timestamps)
            print(f"Amount of timestamps during year '{year}' is {amount}\n")

        elif choice == 2:
            month = input("Insert month: ")
            amount = A8_T4Lib.calculateMonths(month, timestamps)
            print(f"Amount of timestamps during month '{month}' is {amount}\n")

        elif choice == 3:
            weekday = input("Insert weekday: ")
            amount = A8_T4Lib.calculateWeekdays(weekday, timestamps)
            print(f"Amount of timestamps during weekday '{weekday}' is {amount}\n")

        else:
            print("Invalid choice.\n")

    print("Program ending.")

if __name__ == "__main__":
    main()
