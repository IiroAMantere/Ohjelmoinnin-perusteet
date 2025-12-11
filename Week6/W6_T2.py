def main():
    print("Program starting.")

    first_name = input("Insert first name: ")
    last_name = input("Insert last name: ")
    filename = input("Insert filename: ")

    with open(filename, "w") as file:
        file.write(first_name + "\n")
        file.write(last_name + "\n")
        file.write("\n")
    
    print("\nProgram ending.")

main()