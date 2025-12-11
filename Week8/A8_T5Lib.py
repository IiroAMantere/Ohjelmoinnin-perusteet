import hashlib
from typing import List, Tuple

CREDENTIALS_FILE = "credentials.txt"


def hashPassword(PPassword: str) -> str:
    """Returns an MD5 hex digest of the password."""
    md5 = hashlib.md5()
    md5.update(PPassword.encode("utf-8"))
    return md5.hexdigest()


def loadCredentials() -> List[Tuple[int, str, str]]:
    """
    Loads credentials from file.
    Returns a list of tuples: (id, username, password_hash).
    """

    credentials = []

    try:
        with open(CREDENTIALS_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue

                parts = line.split(";")
                user_id = int(parts[0])
                username = parts[1]
                passwd_hash = parts[2]

                credentials.append((user_id, username, passwd_hash))
    except FileNotFoundError:
        # If file doesn't exist yet, return empty list
        pass

    return credentials


def saveCredential(PUserId: int, PUsername: str, PPasswordHash: str) -> None:
    """Appends a new credential line to the credentials file."""
    with open(CREDENTIALS_FILE, "a") as file:
        file.write(f"{PUserId};{PUsername};{PPasswordHash}\n")


def registerUser(PUsername: str, PPassword: str) -> None:
    """Registers a new user and stores the credentials."""
    credentials = loadCredentials()

    # User ID = number of existing users
    new_id = len(credentials)

    hashed_pw = hashPassword(PPassword)

    saveCredential(new_id, PUsername, hashed_pw)


def authenticate(PUsername: str, PPassword: str):
    """
    Checks if a username/password matches.
    Returns (True, user_id, username) or (False, None, None)
    """

    credentials = loadCredentials()
    hashed_pw = hashPassword(PPassword)

    for user_id, username, saved_hash in credentials:
        if username == PUsername and saved_hash == hashed_pw:
            return True, user_id, username

    return False, None, None
