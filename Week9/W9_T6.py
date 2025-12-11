def main() -> None:
    lines = []
    print("Program starting.")

    try:
        while True:
            print("\nOptions:")
            print("1 - Insert line")
            print("2 - Save lines")
            print("0 - Exit")

            try:
                choice = input("Your choice: ")
            except KeyboardInterrupt:
                # CTRL + C during menu
                print("\nKeyboard interrupt and unsaved progress!")
                if not lines:
                    print("Closing suddenly.")
                    break
                save = input("Save before quit(y/n)?: ")
                if save == "y":
                    filename = input("Insert filename: ")
                    with open(filename, "w") as f:
                        for l in lines:
                            f.write(l + "\n")
                    print(f"Lines saved to {filename}.")
                break
            if choice == "1":
                try:
                    text = input("Insert text: ")
                    lines.append(text)
                except KeyboardInterrupt:
                    print("\nKeyboard interrupt and unsaved progress!")
                    if not lines:
                        print("Closing suddenly.")
                        break
                    save = input("Save before quit(y/n)?: ")
                    if save == "y":
                        filename = input("insert filename: ")
                        with open(filename, "w") as f:
                            for l in lines:
                                f.write(l + "\n")
                            print(f"Lines saved to {filename}.")
                        break

            elif choice == "2":
                if not lines:
                    print("No lines to save.")
                else:
                    filename = input("Insert filename: ")
                    with open(filename, "w") as f:
                        for l in lines:
                            f.write(l + "\n")
                    print(f"Lines saved to {filename}.")
            elif choice == "0":
                break
            else:
                print("Unknown option!")

    except KeyboardInterrupt:
        print("\nKeyboard interrupt and unsaved progress!")           
main()