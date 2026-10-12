#22  12.10.  Program hýbe kuličkou a potom vypíše tabulku.
import time
import math

pocet = 10
print("Kulicka jede")

for i in range(pocet):
    time.sleep(0.1)
    print(i*" " + "O")

for i in range(pocet):
    time.sleep(0.1)
    print((pocet-i)*" " + "O")

print("Tabulka")
for i in range(1, pocet + 1):
    print(i, i*i , math.sqrt(i))
