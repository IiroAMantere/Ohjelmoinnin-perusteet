# Virheenkäsittelyrakenne:
# try - yrittää toteuttaa toimenpiteen
# except- tarttuu paikkeukseen
# finally -vapaaehtoinen, tekee virheenkäsittelyn jälkeiset toimet



def main() -> None:
    Sum = 0 #Alusta muuttuja
    Value = -1  #Alustetaan toinen muuttuja
    print("Program starting.")
    while Value !=0:
        Feed = input("Insert a number, 0 to stop: ")
# print(float(Feed))    #Ei toimi, koska kirjoitettiinkin kirjaimia, eli stringiä, eikä float, eikä tämä osaa muuttaa stringiä floatiksi
#Kirjoitetaankin vaikka Jaska
# Tulee virhe, joka kuvattu rivillä 7.


        try:
            Value = float(Feed)
            Sum += Value
        except ValueError: #Tarttuu tyyppierroriin
            print("Selkeä tyyppivirhe")
        except Exception:
            print(f"\"{Feed}\" is not a number.")  #Nyt, kun kirjoittaa Jaska, tulee teksti " "Jaska" is not a number. "
        finally:
            print("Task completed.")  #Aina loppuun finally. Muuten ei toimi :)

    print(f"The sum of given numbers is: {Sum}")
    print("Program ending.")
    return None

main()