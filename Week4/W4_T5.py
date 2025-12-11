print("Program starting.\n")

Feed = input("Insert starting point: ")
Alku = int(Feed)
Feed = input("Insert stopping point: ")
Loppu = int(Feed)
Feed = input("insert inspection point: ")
Tarkistus = int(Feed)

Run = True

if(Alku >= Loppu):
    print("\nStarting point value must be less than the stopping point value")
    Run = False
if((Alku > Tarkistus) or (Tarkistus > Loppu)):
    print("Inspection value must be within the range od start and stop.")
    Run = False

if(Run):
    print("First loop - Inspection with break:")
    for i in range(Alku, Loppu):
        if(i == Tarkistus):
            break
        else:
            print(i, end=' ')

    print("\nSecond loop - inspection with continue:")
    for i in range(Alku, Loppu):
        if(i == Tarkistus):
            continue
    else:
        if(i == (Loppu-1)):
            print(i)
        else:
            print(i, end=' ')

print("\nProgram ending.")