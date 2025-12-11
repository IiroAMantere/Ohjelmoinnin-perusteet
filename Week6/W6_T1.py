def main() -> None:
    print("Program starting.")
    print("This Program can read a file.")
    filename = input("Insert filename: ")
    print(f'#### START "{filename}" ####')
    with open(filename, "r") as file:
        for line in file:
            print(line, end="")

    print(f'#### END "{filename}" ####')
    print("Ending program.")
    






if __name__ == "__main__":
    main()