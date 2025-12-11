from time import sleep

def activatePause(duration):
    print(f"pausing for {duration} seconds")
    sleep(duration)
    print("Unpaused.")