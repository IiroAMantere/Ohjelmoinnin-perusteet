# Muuta annettu arvo integeriksi.
# Luku muuttuu loopin aikana
# Tee while - loop, joka looppaa niin kauan, kuin luku ei ole 1.
#     Printtaa alkuperäinen luku ja lisää loppuun ->
#     Testaa onko luku parillinen       remainder = sum % 2
#         Jaa arvo kahdella
#     muussa tapauksessa 
#         kerro luku kolmella ja lisää yksi

#     lisää kierroksiin +1

# printtaa kierrokset
print("Program starting.")
numero = int(input("Insert a positive integer: "))
steps = 0
current = numero
while current != 1:
    print(current, end=' -> ')
    if current % 2 == 0:
            current = current // 2
    else:
        current = current * 3 + 1
    steps += 1
print("1")
print(f"Sequence had {steps} total steps.")
print("\nProgram ending.")



