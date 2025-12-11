print("Program starting.")
print("Testing decision structures.")

Feed = int(input("Insert an integer: "))
Value = Feed
print("Options:")
print("1 - In one multi-branched decision")
print("2 - In multiple independent if-statements")
print("0 - Exit")

Feed = input("Your choice: ")
Choice = int(Feed)
#Tämä on yksi tapa tehdä tuo int(input(XXXXX)) lauseke. 

if(Choice == 1):
    print("Using one multi-branched decision structure.")
    if(Value >= 400):
        Value += 44
    elif(Value >= 200):
            Value += 22
    elif(Value >= 100):
         Value += 11
    print(f"Result is {Value}")
elif(Choice == 2):
    if(Value >= 400):
         Value += 44
    if(Value >= 200):
         Value += 22
    if(Value >= 100):
        Value += 11
    print(f"Result is {Value}")
elif(Choice == 0):
    print("Exiting...")
else:
     print("Unknown option")
    
print("")
print("Program ending")
