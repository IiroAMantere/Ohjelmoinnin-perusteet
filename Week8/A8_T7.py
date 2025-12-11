import math

def menu():
    print("Options: ")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Draw hexagon")
    print("4 - Save svg")
    print("0 - Exit")



def main():

    print("Program starting.")
    menu()
    while True:
        Choice = input("Your choice: ")
        if Choice == 0:
            print("Exiting program.")
print("Program ending.")
