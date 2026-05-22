# 1.	Welche Aussagen sind richtig?

# a)	Schleifen werden immer einmal durchlaufen.                                              n
# b)	Die fußgesteuerte Schleife beginnt in Python mit dem Schlüsselwort „repeat“.            y
# c)	Alle Elemente einer Liste müssen den gleichen Datentyp besitzen.                        n
# d)	Das erste Listenelement hat immer den Index 1.                                          n
# e)	Um Zufallszahlen in Python zu erzeugen, muss das Modul „random“ eingebunden werden.     n
# f)	Es gibt nur eine Methode, um Zufallszahlen zu erzeugen.                                 n

# 2.	Passen Sie das Beispielprogramm aus dem Schülerband Seite 558 so an, dass die eingegebenen Temperaturen aus der Liste mithilfe einer Schleife am Ende angezeigt werden.
# anzahl = 6
# i = 0
# summe = 0
# temperaturen = [] #Anlegen einer leeren Liste
# while i < anzahl:
#     print("Geben Sie die {0}. Temperatur in °C ein: ".format(i+1))
#     eingabe = float(input())
#     temperaturen.append(eingabe) #Element am Ende der Liste hinzufügen
#     summe = summe + temperaturen[i] #auf Listenelement zugreifen
#     i = i + 1
#     print(temperaturen)
# durchschnitt = summe / anzahl
# print("Durschnittstemperatur: ", round(durchschnitt, 2), "°C")

# 3.	Passen Sie das Beispielprogramm aus dem Schülerband Seite 558 so an, dass die Konsoleneingabe durch Zufallszahlen ersetzt wird und erhöhen Sie die Anzahl der Temperaturen, welche eingegeben werden können
# import random

# anzahl = 10
# i = 0
# summe = 0
# temperaturen = [] #Anlegen einer leeren Liste

# while i < anzahl:
#     print("Geben Sie die {0}. Temperatur in °C ein: ".format(i+1))
#     temperatur = random.randint(0, 41)
#     temperaturen.append(temperatur) #Element am Ende der Liste hinzufügen
#     summe = summe + temperaturen[i] #auf Listenelement zugreifen
#     i = i + 1
# for x in temperaturen:
#     print(x)

# durchschnitt = summe / anzahl
# print("Durschnittstemperatur: ", round(durchschnitt, 2), "°C")

# 4.	Schreiben Sie ein Programm, welches alle geraden Zahlen von 0 bis 20 ausgibt

# for a in range(20):
#     a += 1
#     if a % 2 == 0:
#         print(a)
    

# 5.	Geben Sie mithilfe von Schleifen folgende Figuren aus Sternen auf dem Bildschirm aus.
# Hinweis: Pro Schreibvorgang darf jeweils immer nur ein Stern ausgegeben werden.
 
# *******	7 Sterne
#  ***** 	5 Sterne
#   ***  	3 Sterne
#    *   	1 Stern

# liste = [7, 5, 3, 1]

# def stars(num_stars):

#     spaces = ((liste[0] - num_stars) // 2) + 1

#     for i in range(spaces):
#         print(" ", end = "")
#     for i in range(num_stars):
#         print("*", end = "")
#     for i in range(spaces):
#         print(" ", end = "")
#     print(f"{num_stars} Sterne")

# for i in liste:
#     stars(i)

# 6.	Schreiben Sie ein Programm, in das der Benutzer eine ganze Zahl eingibt und das im An-schluss die Fakultät dieser Zahl berechnet und ausgibt. Verwenden Sie keine Rekursion zur Lösung der Aufgabe. (Hinweis 0! = 1) 
# Beispiel: 5! = 5 * 4 * 3 * 2 * 1 = 120

num = int(input("Geben Sie eine ganze Zahl ein: "))
if num < 0:
    print("Die Fakultät ist nur für nicht-negative ganze Zahlen definiert.")
else:
    faku = 1
    for i in range(2, num + 1):
        faku *= i
    print(f"{num}! = {faku}")
