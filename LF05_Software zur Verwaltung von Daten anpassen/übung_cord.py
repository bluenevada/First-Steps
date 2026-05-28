# Zwei Zahlen genau vergleichen

# Schreibe ein Programm, das testet und ausgibt,
# welche von zwei Zahlen größer ist oder ob beide Zahlen gleich groß sind.
# Die beiden Zahlen sollen zufällige erzeugt werden.

# import random
# random.seed()

# a = random.randint(1,10)
# b = random.randint(1,10)

# if a > b:
#     print("a ist größer als b")
# elif b > a:
#     print("b ist größer als a")
# elif a == b:
#     print("a ist gleich b")
# else:
#     print("Es ist etwas schief gelaufen.")

# Zahlenreihen

# Schaue, welche der 12 Aufgaben du schon lösen kannst.
# Je mehr, desto besser, aber es müssen nicht alle sein.


# 1. Schreibe eine Schleife, die Folgendes ausgibt:
# 1 2 3 4 5
print("\n\n Aufgabe 1:\n")

for i in range(1,6):
    print(i, end = " ")

# 2. Schreibe eine Schleife, die Folgendes ausgibt:
# 100 90 80 70 60 50 40 30 20 10
print("\n\n Aufgabe 2:\n")

for i in range(100,0,-10):
    print(i, end = " ")

# 3. Schreibe eine Schleife, die Folgendes ausgibt:
# 2000 3000 4000 5000 6000
print("\n\n Aufgabe 3:\n")

for i in range(2000,6001,1000):
    print(i, end = " ")

# 4. Schreibe eine Schleife, die Folgendes ausgibt:
# 13 17 21 25 29
print("\n\n Aufgabe 4:\n")

for i in range(13,30,4):
    print(i, end = " ")

# 5. Schreibe eine Schleife, die Folgendes ausgibt:
# 2.0 1.5 1.0 0.5 0.0 -0.5 -1.0
print("\n\n Aufgabe 5:\n")

counter = 2.0

while counter >= -1.0:
    print(counter, end = " ")
    counter -= 0.5

# 6. Schreibe eine Schleife, die Folgendes ausgibt:
# 1.0 2.2 3.4 4.6 5.8 7.0 8.2 9.4
print("\n\n Aufgabe 6:\n")

number = 1.0

while number <= 9.4:
    print(round(number, 1), end = " ")
    number += 1.2

# 7. Schreibe eine Schleife, die Folgendes ausgibt:
# Beachte: die 7 fehlt!
# 1 2 3 4 5 6 8 9 10
print("\n\n Aufgabe 7:\n")

number = 1

while number <= 10:
    if number != 7:
        print(number, end = " ")
    number += 1

# 8. Schreibe eine Schleife, die Folgendes ausgibt:
# Beachte: die 25 und die 41 fehlen!
# 13 17 21 29 33 37 45
print("\n\n Aufgabe 8:\n")

number = 13

while number <= 45:
    if number != 25 and number != 41:
        print(number, end = " ")
    number += 4

# 9. Schreibe eine Schleife, die Folgendes ausgibt:
# Z5 Z7 Z9 Z11 Z13
print("\n\n Aufgabe 9:\n")

num = 5

while num <= 13:
    print("Z"+ str(num), end = " ")
    num += 2

# 10. Schreibe eine Schleife, die Folgendes ausgibt:
# a2b3 a12b13 a22b23
print("\n\n Aufgabe 10:\n")

num_1 = 2
num_2 = 3

while num_1 <= 22 and num_2 <= 23:
    print("a"+ str(num_1) + "b" + str(num_2), end = " ")
    num_1 += 10
    num_2 += 10

# 11. Schreibe eine Schleife,
# die alle Zahlen von 1 bis 20 addiert
# und danach das Endergebnis ausgibt.
print("\n\n Aufgabe 11:\n")

ergebniss = 0

for i in range(1,21):
    ergebniss += i
print(ergebniss, end = " ")

# 12. Schreibe EINE Schleife, die Folgendes ausgibt:
# 1 2 3 4 5 4 3 2 1
print("\n\n Aufgabe 12:\n")

for i in range(1, 10):
    if i <= 5:
        print(i, end=" ")
    else:
        print(10 - i, end=" ")