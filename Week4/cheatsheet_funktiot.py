# print() # funktiokutsu
# print("Hello") # "Hello" on funktion parametri
# len()

# while true:
#     print("I can do this all all day")

    # def greet(name):
    #     print(f"Hello {name}")

    #     print("Here I am")
    #     greet("Mira")

# def greet(name):
#     return f"hello, {name}"

# print(greet("Mira"))

def greeting_airport(person, age):
    print(f"how do you do {person}")
    if age >= 18:
        print("Welcome to your flight")
    else:
        print(f"You need to wait for {18-age} years to fly solo.")
greeting_airport("Mira, 48")

# Tee ohjelma, joka kysyy käyttäjältä kokonaislukua. Testaa funktiolla, onko se alkuluku (prime number) vai ei.
# Kysy uutta lukua, kunnes käyttäjä pyytää lopettamaan kysymyksen.
