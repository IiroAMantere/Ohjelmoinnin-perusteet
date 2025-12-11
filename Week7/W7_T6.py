import random
random.seed(1234)

Choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

def bot_choice() -> str:
    num = random.randint(1,3)
    return Choices[num]

def determine_winner(player: str, bot: str):
    if player == bot:
        return "draw"
    elif player == "Rock" and bot == "Scissors":
        return "player"
    elif player == "Scissors" and bot == "Paper":
        return "player" 
    elif player == "Paper" and bot == "Rock":
        return "player"
    else:
        return "bot"

def game(player_choice: int, player_name: str, bot_name: str) -> str:
    """Play a single round and return winner: 'player', 'bot', or 'draw'."""
    player = Choices[player_choice]
    bot = bot_choice()

    print("\nRock! Paper! Scissors! Shoot!\n")
    print("#"*25)
    print(f"{player_name} chose {player}.\n\n")
    print("#"*25)
    print(f"{bot_name} chose {bot}.\n\n")
    print("#"*25 + "\n")

    winner = determine_winner(player, bot)
    if winner == "draw":
        print(f"Draw! Both chose {player}.\n")
    elif winner == "player":
        print(f"{player_name} {player} beats {bot_name} {bot}.\n")
    else:
        print(f"{bot_name} {bot} beats {player_name} {player}.\n")

    return winner

def main() -> None:
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")

    player_name = input("Insert player name: ").strip()
    bot_name = "RPS-3PO"

    print(f"Welcome {player_name}!")
    print(f"Your opponent is {bot_name}.")
    print("Game starts...\n")

    wins = 0
    losses = 0
    draws = 0

    while True:
        print("Options:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("0 - Quit game")
        choice = input("Your choice: ").strip()

        if choice not in ("0", "1", "2", "3"):
            print("Invalid choice! Please select 0, 1, 2, or 3.\n")
            continue

        if choice == "0":
            break

        winner = game(int(choice), player_name, bot_name)
        if winner == "player":
            wins += 1
        elif winner == "bot":
            losses += 1
        else:
            draws += 1

    print("\nResults:")
    print(f"{player_name} - wins ({wins}), losses ({losses}), draws ({draws})")
    print(f"{bot_name} - wins ({losses}), losses ({wins}), draws ({draws})")
    print("\nProgram ending.")   

main()