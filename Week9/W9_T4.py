########################################################
# Task A9_T4
# Developer Iiro Mantere
# Date 10.12.2025
########################################################

TEMP_MIN = -273.15
TEMP_MAX = 1000


def CollectCelsius() -> float:

    Feed = (input("Insert Celsius: "))
    try:
        Celsius = float(Feed)
    except ValueError:
        raise ValueError(f"Could not convert string to float: {Feed}")

    if (Celsius < TEMP_MIN) or (Celsius > TEMP_MAX):
        raise Exception (f"{Celsius} temperature out of range.")
    return Celsius


def main() -> None:
    print("Progmram starting.")
    try:
        Temperature = CollectCelsius()
        print(f"You inserted {Temperature} °C")
    except ValueError as e:
        print(e)
    
    print("Program Ending.")
    return None

main()