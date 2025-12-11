########################################################
# Task A9_T2
# Developer Iiro Mantere
# Date 10.12.2025
########################################################

import sys

def main() -> None:

    print("Program starting.")
    Feed = input("Insert exit code (0-255): ")
    Exitcode = int(Feed)
    if Exitcode == 0:
        print("Clean exit.")
    else:
        print("Error code.")
    sys.exit(Exitcode)
    print("Program ending.")
    return None

main()