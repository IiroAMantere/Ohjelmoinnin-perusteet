########################################################
# Task A9_T1
# Developer Iiro Mantere
# Date 10.12.2025
########################################################

def main():
    Sum = 0
    Number = -1

    print("Program starting.")
    while Number !=0:
        Feed = input("insert a floating-point value (0 to stop): ")
        try:
            Number = float(Feed)
            Sum += Number
        except:
            print(f"ERROR! {Feed} couldn\'t be converted to float.")
        finally:
            print("")
    print(f"The sum of given numbers is: {Sum}")
    print("Program ending.")
    return None        
main()