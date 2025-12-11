def Color_picker(name: str) -> int:
    value_str = input(f"Insert {name}: ")
    try:
        value = int(value_str)
    except ValueError:
        print(f'"{value_str}" is non-numeric value.')
        raise
    if not (0 <= value <= 255):
        print(f'Value "{value}" is out of the range 0-255.')
        raise Exception("Out of range")
    return value

def main() -> None:
    print("Program starting.")
    try:
        red = Color_picker("red")
        green = Color_picker("green")
        blue = Color_picker("blue")
        print("RGB Details:")
        print(f"- Red {red}")
        print(f"- Green {green}")
        print(f"- Blue {blue}")
        print(f"- Hex #{red:02x}{green:02x}{blue:02x}")
    except Exception:
        print("Couldn't perform the designed task due to the invalid input values.")
    print("Program ending.")

main()
