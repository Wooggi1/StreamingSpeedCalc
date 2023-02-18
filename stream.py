import time
import sys
import msvcrt

def bpmCalc(zCount, xCount):
    clicks = zCount + xCount
    bpm = clicks/4
    print(f"Your streaming speed is {bpm}bpm")

start_time = time.time()
elapsed_time = 0
z_count = 0
x_count = 0

zKey = input("insert first keybind of preference\n")
xKey = input("insert second keybind of preference\n")
clickLimit = int(input("insert the amount of clicks\n"))

while elapsed_time < 60:
    if msvcrt.kbhit():
        key = msvcrt.getch().decode('utf-8')
        if key == zKey:
            z_count += 1
        elif key == xKey:
            x_count += 1

        clicks = z_count + x_count
        if clicks == clickLimit:
            break
        
    elapsed_time = time.time() - start_time

print("z was pressed", z_count, "times")
print("x was pressed", x_count, "times")


#bpmCalc(z_count, x_count)
