print("Program starting.")
word = input("Insert fahrenheits: ")
word =float(word)
celcius = float(word - 32) / 1.8
print(f"{round(word ,2)}°F is {round(celcius ,2)}°C")
print("Program ending.")