print("Program starting.\n")

value1 = int(input("Insert starting value: "))
value2 = int(input("Insert stopping value: "))

print("\nStarting for-loop:")
for i in range(value1, value2 +1):
    if i != value2:
        print(i, end= " ")
    else:
        print(i)

print("\nProgram ending.")