import A8_T2Lib


def main() -> None:
    print("Program starting.")

    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.")
            break

        elif choice == 1:
            a = askValue("Insert first addend value: ")
            b = askValue("Insert second addend value: ")
            result = A8_T2Lib.add(a, b)
            print(f"{a} + {b} = {result}\n")

        elif choice == 2:
            a = askValue("Insert minuend value: ")
            b = askValue("Insert subtrahend value: ")
            result = A8_T2Lib.subtract(a, b)
            print(f"{a} - {b} = {result}\n")

        elif choice == 3:
            a = askValue("Insert multiplicand value: ")
            b = askValue("Insert multiplier value: ")
            result = A8_T2Lib.multiply(a, b)
            print(f"{a} * {b} = {result}\n")

        elif choice == 4:
            a = askValue("Insert dividend value: ")
            b = askValue("Insert divisor value: ")
            result = A8_T2Lib.divide(a, b)
            print(f"{a} / {b} = {result}\n")

        else:
            print("Invalid choice.\n")

    print("\nProgram ending.")



def showOptions() -> None:
    print("Options:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")

def askChoice() -> int:
    return int(input("Your choice: "))


def askValue(PPrompt: str) -> float:
    return float(input(PPrompt))





main()