def main() -> None:
    print("Program starting.")
    print("This program analyses a list of names from a file.")

    filename = input("Insert filename to read: ")
    print(f'Reading names from "{filename}".')

    names_str = ""

    # --- Read file and build semicolon-separated name string ---
    with open(filename, "r") as file:
        for line in file:
            name = line.strip()
            if name == "":
                continue
            if names_str == "":
                names_str = name
            else:
                names_str += ";" + name

    print("Analysing names...")

    # Split combined string back into list
    names = names_str.split(";") if names_str else []

    # --- Analysis calculations ---
    count = len(names)
    shortest = min(len(name) for name in names) if names else 0
    longest = max(len(name) for name in names) if names else 0
    avg_length = (sum(len(name) for name in names) / count) if count > 0 else 0

    print("Analysis complete!")

    # --- Build report using format specification mini-language ---
    report = (
        "#### REPORT BEGIN ####\n"
        f"Name count - {count}\n"
        f"Shortest name - {shortest} chars\n"
        f"Longest name - {longest} chars\n"
        f"Average name - {avg_length:.2f} chars\n"
        "#### REPORT END ####"
    )

    print(report)
    print("Program ending.")


if __name__ == "__main__":
    main()
