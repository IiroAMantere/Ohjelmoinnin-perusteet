def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")

    values: list[str] = []

    # Read and process file
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()      # remove newline & spaces
            if line != "":           # ignore empty rows
                values.append(line)

    # --- Vertical Output ---
    print("# --- Vertically --- #")
    for val in values:
        print(val)
    print("# --- Vertically --- #")

    # --- Horizontal Output ---
    print("# --- Horizontally --- #")
    print(", ".join(values))
    print("# --- Horizontally --- #")

    print("Program ending.")


if __name__ == "__main__":
    main()