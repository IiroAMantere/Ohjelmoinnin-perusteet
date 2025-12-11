
from A8_T1Lib import activatePause

def askUser() -> int:
    return int(input("Your Choice: "))

def showOption() -> None:
    print("Options:")
    print("1 - Set pause duration: ")
    print("2 - Activate pause")
    print("0 - Exit")

    return None

def chooseActivity() -> None:
    duration = 0
    while True:
        showOption()
        choice = askUser()
        print(choice)
        match choice:
            case 1:
                duration = int(input("Insert pause duration (s): "))
            case 2:
                activatePause(duration)
            case 0:
                print("Exiting program.")
        break
        return None

def main() -> None:
    print("Program starting.")
    chooseActivity()
    print("Program ending.")
    return None


main()