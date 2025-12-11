import sys

def readValues(PFilename: str, PValues: list[int]) -> None:
    """Reads integers from file, strips and filters empty rows."""
    try:
        with open(PFilename, "r") as file:
            for line in file:
                clean = line.strip()
                if clean != "":
                    PValues.append(int(clean))
    except Exception as e:
        print(f"ERROR: Cannot read file '{PFilename}'.")
        sys.exit(1)
    return None


def sumOfValues(PValues: list[int]) -> int:
    total = 0
    for v in PValues:
        total += v
    return total

def productOfValues(PValues: list[int]) -> int:
    product = 1
    for v in PValues:
        product *= v
    return product


def main() -> None:
    # ---- 1. Initialize ----
    Values: list[int] = []

    # ---- 2. Operate ----
    print("Program starting.")
    filename = input("Insert filename: ")

    # 2.2 read
    readValues(filename, Values)

    # 2.3 & 2.4 calculate
    total = sumOfValues(Values)
    product = productOfValues(Values)

    # ---- 2.5 Display results ----
    print("# --- Sum of numbers --- #")
    print(total)
    print("# --- Sum of numbers --- #")

    print("# --- Product of numbers --- #")
    print(product)
    print("# --- Product of numbers --- #")

    # ---- 3. Cleanup ----
    Values.clear()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
