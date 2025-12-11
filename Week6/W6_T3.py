def main() -> None:
    print("Program starting.")
    print("This program can copy a file.")

    origin = input("Insert source filename: ")
    destination = input("Insert destination filename: ")

    print(f"Reading file '{origin}' content.")
    with open(origin, "r") as src_file:
        content = src_file.read()
    print("File content already in memory.")

    print(f"Writing content into file '{destination}'.")
    with open(destination, "w") as dest_file:
        dest_file.write(content)

    print("Copying operation complete.")
    print("Program ending.")


main()