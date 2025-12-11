def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")

def AskChoice():
    Choice1 = input("Your choice: ")
    if  Choice1.isnumeric():
        return int(Choice1)
    else:
        print("Unknown option!\n")
        return -1
def main():
    print("Program starting.")
    Count = 0
    Choice = -1
    while Choice != 0:
        showOptions()
        Choice = AskChoice()
        if Choice == 1:
            print(f"Current count - {Count}\n")
        elif Choice == 2:
            Count += 1
            print("Count increased!\n")
        elif Choice == 3:
            print("Cleared count!\n")
            Count = 0
        elif Choice == 0:
            print("Exiting program.")
        elif Choice != -1:
            print("Unknown option!\n")
    print("\nProgram ending.")    

main()