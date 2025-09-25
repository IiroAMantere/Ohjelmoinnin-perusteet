#Average and rounding
#Prompt the user to insert the minutes spent on each previous topic task. Calculate the sum and the average. Display those in the example program run format(Note! precision). Make sure to calculate the required average for two decimal digits and later integer as rounded integer (precision 0 + type conversion).

#Example program run:

#Program starting.
print("Program starting")
#Estimate how many minutes you spent on programming...
print("How many minutes you spent on programming...")
Task1 = int(input("A1_T1: "))
Task2 = int(input("A1_T2: "))
Task3 = int(input("A1_T3: "))
Task4 = int(input("A1_T4: "))
Task5 = int(input("A1_T5: "))
Task6 = int(input("A1_T6: "))
Task7 = int(input("A1_T7: "))
#A1_T1: 3
#A1_T2: 7
#A1_T3: 9
#A1_T4: 8
#A1_T5: 13
#A1_T6: 14
#A1_T7: 21
total = Task1+Task2+Task3+Task4+Task5+Task6+Task7
Average = float(total/7)
#In total you spent 75 minutes on programming.
print(f"\nIn total you spent {total} minutes on programming.")
#Average per task was 10.71 min and same rounded to the nearest integer 11 min.
print(f"\nAverage per task was {round(Average,2)} min and same roubded to nearest integer {round(Average)} min.")

#Program ending.
print("Program ending.")
