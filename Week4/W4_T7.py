# Pyydä arvo ja muuta se integeriksi
# alusta muuttuja, joka laskee kierroksia
# tee while loop. joka looppaa niin kauan, kuin arvo ei ole 0
#     testaa, onko arvo pienenmpi kuin 10 > break
#     Muuta arvo integeriksi, jotta saamme yksittäiset luvut esiin
#     tee for loop joka käy läpi jokaisen stringiksi muutetun luvun
#         testaa, onko numero viimeinen
#         jos numero ei ole viimeinen, muista laittaa sinne kerto-merkki
#         tee laskutoimitus integereillä
#     printtaa kertolaskun tulos
#     muuta arvoksi edellisen kierroksen kertolaskun tulos
#     Jos arvo on nolla, printtaa   No more steps.
#     Lisää kierroslaskuriin +1

# printtaa kierrokset 
# printtaa program ending


# Voi kokeilla tehdä listan avulla!!!!!!!!!!!
print("Program starting.")

print("\nCheck multiplicative persistence.")
numero = int(input("Insert an integer: "))
loops = 0
while True:
        tulo = 1
        luvut = str(numero)
        if numero < 10:
            print("No more steps.")
            break
        if numero >= 10:
            for i in range(len(luvut)):
                n = int(luvut[i])
                tulo *= n
                if i != len(luvut) - 1:
                 print(luvut[i], end=" * ")
                else:
                    print(luvut[i], end=" = ")
        print(tulo)
        numero = tulo
        loops += 1

print(f"\nThis program took {loops} step(s)")

print("\nProgram ending.")