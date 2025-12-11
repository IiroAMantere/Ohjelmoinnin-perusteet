import A8_T5Lib


def showMainMenu():
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")


def showUserMenu():
    print("User menu:")
    print("1 - View profile")
    print("2 - Change password")
    print("0 - Logout")


def main():
    print("Program starting.")

    while True:
        showMainMenu()
        choice = input("Your choice: ")

        if choice == "0":
            print("Exiting program.")
            break

        elif choice == "1":  # Login
            username = input("Insert username: ")
            password = input("Insert password: ")

            ok, uid, uname = A8_T5Lib.authenticate(username, password)
            if not ok:
                print("Authentication failed!\n")
                continue

            print("Authentication successful!\n")

            # User menu loop
            while True:
                showUserMenu()
                u_choice = input("Your choice: ")

                if u_choice == "1":
                    print(f"Profile ID {uid} - {uname}\n")

                elif u_choice == "2":
                    print("Change password feature not implemented.\n")

                elif u_choice == "0":
                    print("Logging out...\n")
                    break

                else:
                    print("Invalid choice.\n")

        elif choice == "2":  # Register
            username = input("Insert username: ")
            password = input("Insert password: ")

            A8_T5Lib.registerUser(username, password)
            print("User registration completed!\n")

        else:
            print("Invalid choice.\n")

    print("Program ending.")


if __name__ == "__main__":
    main()
