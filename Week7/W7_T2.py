def askIntegers(Values: list[int]) -> None:
    Feed = input("Insert comma separated integers: ")
    
    for Value in Feed.split(','): #Split inputs by comma
        if Value.isnumeric():
            Values.append(int(Value)) #Convert to int and add to the end of the list
        else:
            print(f"Invalid value '{Value}' detected.")
            continue
    return None

def Analyze(Values: list[int]) -> None:
        Sum = 0
        if len(Values) == 0:
            print("No values to analyze.")
        else:
            for Value in Values:
                 Sum += Value
            print(f"There are {len(Values)} integers in the list.")
            Parity ='even' if Sum % 2 == 0 else 'odd'
            print(f"Sum of integers is {Sum} and it's {Parity}.")
    #Check if list is empty
    #If not, loop through the list
        #Sum values
        #Show count
        #Check parity
            return None

def main():
      print("Program starting.")
      Values: list[int] = []
      askIntegers(Values) #jump to askIntegers function and sen a REFERENCE to the list as a function parameter.
      Analyze(Values) # Jump to analyze function and send a REFERENCE to the list as a function parameter.

      print("Program ending.")
      return None

if __name__ == "__main__":
    main()