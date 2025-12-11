#Kirjastojen käyttöä

# import turtle   #!Importaa koko kirjaston

#from turtle import Screen
#turtle_screen = Screen()   #!Importaa screen classin turtle kirjastosta

#from turtle import *   !Tätä ei kannata käyttää, koska jos Screen on importattu monesta paikkaa, tämä ei toimi.
#turtle_screen = Screen

# sipi = turtle.Turtle()  #Luo uusi olio eli Turtle instanssi
# sipi.shape("turtle") # Metodi
# sipi.color("green") # Metodi
# sipi.forward(100) # Metodi

# turtle_screen = turtle.Screen()  # Luo uusi ikkuna-olio, eli instanssi
# turtle_screen.exitonclick()  # Metodi

###########################


# class LABStudent:
# #Constructor method


#     name: str #atribute
#     age: int #atribute
#     major: str #atribute

#     def introduce(self): #Method
#         return f"Hi, I'm {self.name}, {self.age} years old, majoring in {self.major}."
#     def study(self): #Method
#         return f"{self.name} is studying {self.major}."

# John = LABStudent()
# John.name = "John"
# John.age = 32
# John.major = "Computer science"

# Jane = LABStudent()
# Jane.name = "Jane"
# Jane.age = 25
# Jane.major = "Physics"

# print(John.introduce())
# print(Jane.study())

from lab_student import LABStudent  #Tämä hakee toisesta tiedostosta "lab_student.py" tiedot, miten introduce ja study metodit toimivat. 

John = LABStudent("John", 32, "Computer Science")
Jane = LABStudent("Jane", 25, "Physics")

print(John.introduce()) #Tämä ja alempi toimii, koska näiden kahden komennon (introduce ja study) toiminta on määritelty lab_student.py-kansiossa. 
print(Jane.study())