print("Program starting.\n")
print("Options:\n")
print("1 - Celsius to Fahrenheit\n")
print("2 - Fahrenheit to Celcius\n")
print("0 - Exit")

choice = int(input("Your choice: "))
if (choice == 1):
    C = float(input("Insert the amount of Celsius: "))
    print(f"{C} °C equals to {round(C * 1.8 + 32, 1)} °F")
elif(choice == 2):
    F = float(input("Insert the amount of Fahrenheit: "))
    print(f"{F} °F equals to {round((F - 32) / 1.8, 1)} °C")
elif(choice == 0):
    print("Exiting...")
else:
    print("Unknown option.\n")
print("\nProgram ending.")