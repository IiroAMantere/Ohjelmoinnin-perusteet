########################################################
# Task A9_T3
# Developer Iiro Mantere
# Date 10.12.2025
########################################################
import sys

def main() -> None:
    print("Program starting")
    Filename = input("Insert filename: ").strip()
    try:
        with open(Filename, "r") as f:
            print(f"## {Filename} ##")
            for line in f:
                print(line.strip())
            print(f"## {Filename} ##")
    except FileNotFoundError:
        print(f"Couldn't read file \"{Filename}\"")
    print("Program ending.")
    return None

main()