#Harjoitus: Tee ohjelma, joka kertoo onko lämpötila liian korkea.
#print("Welcome to the temp app!")
#Temp = int(input("What is the themperature od CPU? "))

#if(Temp > 80):
    #print("Warning, temperature too high!")
#else:
   # print("All cool, keep on going!")

#Harjoitus: Tee ohjelma, joka kertoo onko annettu numero pariton vai parillinen.
#print("program starting")
#num = int(input("kirjoita numero "))

#if num % 2 == 0:
 #   print("Parillinen")
#else:
#    print("pariton")

#Useampi else ja if-lauseke
#Temp = int(input("What is the temperature of CPU? "))
#if(Temp > 80):
    #if(Temp > 90):
       # print("You are toast")
    #else:
        #print("Warning")
#else:
   # print("You are ok")
    
#   Tee ohjelma, joka kysyy kahta nimeä. Testaa, kumpi nimistä on pidempi, vai onko ne saman mittaisia. Vinkki: len()

#ALKAA#
#Name1 = input("kirjoita ensimmäinen nimi ")
#Name2 = input("kirjoita toinen nimi ")
#if len(Name1) > len(Name2): print("First name is longer")
#elif len(Name1) < len(Name2): print("Second name is longer")
#else: print("Names are equal length")
#LOPPUU#

#Monta asiaa
#Town = "Lahti"
#Street = "Mukulankatu"
#Building = 19

#if(Town == "Lahti" and Street == "Mukulankatu" and Building == 19):
  #  print("You are at LAB")
#elif(Town == "Lahti" and (Street != "Mukulankatu" or Building !=19)):
   # print("You are in the correct town, but check the street address again")
#elif not(Town == "Lahti" and Street == "Mukulankatu" and Building == 19):
   # print("You are completely lost...")

#import random

#print(random.random())
#print(random.randint(1,6))

#Listat!!!!
Children = 3
Hometown = "Lahti"

TownsInFinland = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]
RandomInformation = ["Mira", 48, True, Children, Hometown]

print(TownsInFinland[0])
TownsInFinland.append("Rovaniemi")
print(TownsInFinland)

NumOfTowns = len(TownsInFinland) #vast: 6
print(TownsInFinland[NumOfTowns-1])

Municipalities = ["Asikkala", "Hollola", "Karvia", "Kempele"]
Towns = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]

MunicipalitiesAndTowns = [Municipalities, Towns]

print(MunicipalitiesAndTowns[1][-2])  #[1] Kertoo kumpi lista. Laskenta alkaa nollasta. [-2] kertoo mones nimi lopusta, tältä listalta. = Oulu

Towns.sort()
print(Towns) #Aakkosjärjestykseen sortattuna Towns-lista.

Teacher = {
    'name': 'Juha',  # Voi käyttää myös "näitä hipsuja"
    'age': 50,
    'city': 'Lahti'
}

print(Teacher["name"])

Teacher['email'] = 'juha.hyytiainen@lab.fi'

print(Teacher)

for key in Teacher:
    print(key, end=' ') #end=  tällä komennolla seuraava print tulee tämän printin perään. Väliin tulee välilyönti
    print(Teacher[key])

Student = [
   {'name': 'Mikko', 'age': 25, 'city': 'Tampere'},
   {'name': 'Maija', 'age': 30, 'city': 'Espoo'},
   {'name': 'Seppo', 'age': 35, 'city': 'Helsinki'},
]
print(Student[0])

Cities = {
   'Finland':['Tampere', 'Espoo', 'Helsinki'],
   'Sweden':['Stockholm', 'Malmö']
}
print(Cities['Finland'][0])



#  Towns = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]

for town in Towns:
    print(f"The town of {town}")
print(f"All the towns {Towns}")

for i in range(1,10):
    print(i)

for i in range(1,10,):
    print(i, end=' ')

for i in range(1,10, 3):
    print(i)

print("")
Total = 0
for i in range(1,101):   
   Total +=i
   print(Total)

print(Total)

for i in range(9):
    print()