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

while elapsed_time < 60:
    if msvcrt.kbhit():
        key = msvcrt.getch().decode('utf-8')
        if key == "z":
            z_count += 1
        elif key == "x":
            x_count += 1
    elapsed_time = time.time() - start_time

print("z was pressed", z_count, "times")
print("x was pressed", x_count, "times")

bpmCalc(z_count, x_count)