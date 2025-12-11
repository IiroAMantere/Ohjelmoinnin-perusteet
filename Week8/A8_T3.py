import A8_T3Lib

def showOptions() -> None:
    print("Options:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")

def askChoice() -> int:
    return int(input("Your choice: "))

def main() -> None:
    print("Program starting.")
    
    values = []

    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.")
            break

        elif choice == 1:
            filename = input("Insert filename: ")
            values = A8_T3Lib.readValuesFromFile(filename)
            print()

        elif choice == 2:
            print(f"Amount of values {len(values)}\n")

        elif choice == 3:
            result = A8_T3Lib.calcSum(values)
            print(f"Sum of values {result}\n")

        elif choice == 4:
            result = A8_T3Lib.calcAverage(values)
            print(f"Average of values {result}\n")

        else:
            print("Invalid choice.\n")

    print("Program ending.")

if __name__ == "__main__":
    main()