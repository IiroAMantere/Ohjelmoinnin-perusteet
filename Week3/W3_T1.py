#Make Python program and implement if-statements in proper places.

#Ask user to insert two integers
#Compare the integers and then announce the greater number
#Create sum of the two integers
#Check the parity of the sum (see modulo-operator ‘%’)
print("Program starting.")
print("Insert 2 numbers")
Number1 = int(input("Insert number 1: "))
Number2 = int(input("Insert number 2: "))
print("Comparing inserted integers")
if(Number1 > Number2):
    print("Number 1 is bigger")
elif(Number1 < Number2):
    print("Number 2 is bigger")
else:
    print("integers are the same")

sum = Number1 + Number2
print(f"{Number1} + {Number2} = {sum}")
print("")
remainder = sum % 2
print("Checking the parity of the sum...")
if remainder == 0:
    print("Sum is even.")
else:
    print("Number is odd.")

print("Program ending.")
