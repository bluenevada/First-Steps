# Kommentare

# Das hier: # ist ein Single-Line Comment
# Das hier: """ Kommentar """ ist ein Multiline Comment
# Das hier: """ :param firstname: Variable für den Vorname """ ist ein Doc-String
# Beispiel zu Doc-String: 
# a = 40
# b = 2

# def addieren(a, b):
#     """
#     :param a: Zahl 1
#     :param b: Ist die Zahl 2
#     :return: gibt die Summe zweier Zahlen als Integer zurück
#     """
    
#     return a+b

# Variablen

# firstname = "GFN"

# # Output einer Variable
# print(firstname)

# id() in print()
# print(id(firstname))

# # Diese Aktion referenziert nur auf die Speicheradresse und erstellt keine echte Kopie
# company_name = firstname
# print(company_name)
# print(id(company_name))

# # Output einer Variable mit einem String (Zeichenkettte)
# print("--- Variable und Stringausgabe mit + ---")
# print("Mit + Zeichen: Das ist mein Vorname" + firstname)

# print("--- Variable und Stringausgabe mit , ---")
# print("Mit , Zeichen: Das ist mein Vorname",firstname)

# print("--- Variable und Stringausgabe mit F-String ---")
# print(f"Mit F-String: Das ist mein Vorname {firstname}")

# sep & end
print("Das Wetter ist schön", "war es zumindest heute morgen", sep=" ")

print("Hallo", end=" ")
print("Welt")

# Aufgabe:
print("Wir","lernen", "gerade")
print("Python")

# Ziel: Wir***lernen***gerade...Python
print("Wir","lernen", "gerade", sep="***")
print(end="..." "Python")
print("Hallo")

# '''''''''''''''''''''

# Input -  wir wollen eine Usereingabe
# Speichert immer einen String
# firstname_new = input("Gib bitte deinen Vornamen an: ")
# Beispiel für eine Typumwandlung bei User-Input

# age = input("Gib gib dein Alter an: ")
# age_new = int(age)

# # Kurzfassung: age = int(input("Gib gib dein Alter an: "))

# # print(firstname_new)
# print(age + 11)

# Googlen: Es gibt eine Built-In Funktion, die es ermöglicht mit Zahlen in Strings zu rechnen

# -------------------------------
# Datentypen
# str - String - Text  ("Das Wetter ist gut")
# int - Integer - Ganzzahl (42)
# float - Float - Zahlen mit Komma / Fließkommazahlen / Gleitkommazahlen (42.0)
# bool - Boolean - Wahrheitswert (True & False)

# Aufgabe: Den jeweiligen Datentyp ermitteln
# Hier steht der nötige Basiscode für die Aufgabe
# name = "Brutus"
# street = "Zellenstrasse"
# house_number = 25
# height = 1.86
# height_2 = .55
# height_3 = 175.
# is_married = True
# married_date = "15.04.2009"
# has_kids = False

# print(type(name))
# print(type(street))
# print(type(house_number))
# print(type(height))
# print(type(height_2))
# print(type(height_3))
# print(type(is_married))
# print(type(married_date))
# print(type(has_kids))

# Datentypen konvertieren

# Funktion str() konvertiert den Variableninhalt in einen String. Funktioniert mit alle Inhalten

# Beispiel str()
# boolscher_wert = True
# print(type(boolscher_wert))
# bl_2 = str(boolscher_wert)
# print(type(bl_2))

# # Funktion int() konvertiert den Variableninhalt in einen Int. Funktioniert nur bei Zahlen

# my_string = "42" # ohne die anführungszeichen wäre es kein str
# print(int(my_string))

# # Funktion float() konvertiert den Variableninhalt in einen Float. Funktioniert nur bei Zahlen
# my_string_2 = 42
# print(float(my_string_2))

# Funktion bool() konvertiert den Variableninhalt in einen boolean. Funktioniert bei allen Inhalten
# my_string_3 = "Wetter"
# print(bool(my_string_3))

# my_string_3 = ""
# print("Nach überschreiben: ", bool(my_string_3))

# Aufgabe 

# Snake_Case_Schreibweise = variable_1
# CamelCase = ersteVariable
# Pascal Case = ErsteVariable

# variable_1 = "25"
# variable_2 = 10
# variable_3 = "Ich bin eine Variable."

# # print(variable1 + 5) # Die Ausgabe soll "30" sein
# # print(variable2 + " ist eine Zahl.") # Die Ausgabe soll "10 ist eine Zahl." sein
# # print(variable3 + 1) # Die Ausgabe soll "2" sein''

# True = 1
# False = 0 

# print(int(variable_1) + 5) 
# print(str(variable_2) + " ist eine Zahl.") 
# print(bool(variable_3) + 1) 

#---------------------------------------------

# Listen
print("-------------------------")
# Eine Variable trägt einen Inhalt
firstname = "Davy"

# Eine Liste trägt viele Inhalte
# Wir können Datentypen vermischen
firstnames = ["Davy", True, "Florian", 42, "Max", 44.5, "Yves", [1,2,3]]

print(firstnames)
print(firstnames[0]) # 0-indexiert
print(firstnames[-1]) # Rückwärts geht auch - gibt das letzte Element der Liste aus

# Eintrag durch Angabe der Index-Position überschreiben
firstnames[0] = 'Jones'
# Neue, leere Liste erzeugen + append() + extend()
new_list = []
new_list = list() # selten gesehen 
print(f"Inhalt der neuen Liste: {new_list}")

# append() fügt einen Inhalt hinzu
new_list.append("Neuer Eintrag")
print(f"Inhalt der geänderten Liste: {new_list}")
new_list.append("Zweiter Eintrag")
print(f"Inhalt der geänderten Liste: {new_list}")
# extend() fügt mehrere Inhalte  hinzu
new_list.extend([5,6,7])
print(f"Inhalt der mit extend geänderten Liste: {new_list}")
# insert() fügt den Inhalt mit der Indexposition an die gewünschte Stelle hinzu
new_list.insert(5, 'GFN')
print(f"Inhalt der mit insert geänderten Liste: {new_list}")
# remove() löscht einen Inhalt. allerdings nur den ersten davon. Gibt es die 42 mehrmals, wird nur die erste in der Liste gelöscht
new_list.append("Neuer Eintrag")
new_list.remove('Neuer Eintrag')
print(f"Inhalt der mit remove geänderten Liste: {new_list}")
# clear() leert die gesamte Liste
new_list.clear()
print(f"Inhalt der mit clear geänderten Liste: {new_list}")

# List Slicing

my_list = [1,3,4,5,7,9,42]

print(my_list[0]) # Ausgabe: 1
print(my_list[0:3]) # Ausgabe: 1,3,4 Tipp: einfach von der letzten Zahl (bei zwei Zahlen) die erste Zahl abziehen um zu errechnen wie viele Elemente ich bekommen sollte

# Mit Schrittweite
print(my_list[0:7:2]) # Start - Stop - Step

# Test - funktioniert
print("mit len(): ", my_list[0:len(my_list):2])

print("---------------------")
my_list_2 = my_list
print("my_list_2: ", my_list_2)

print(id(my_list))
print(id(my_list_2))

my_list.append("Smartphone")
print(my_list_2)

my_list_2[0] = 'GFN'
print("--- Neue ausgabe nach Veränderung ---")
print(my_list)
print(my_list_2)
print(id(my_list))
print(id(my_list_2))
print("--- Mit Full Slicing ---")
my_list_3 = my_list[:] # Full Slicing um eine echte Kopie, die unabhängig von der bisherigen Liste ist, zu erstellen
print(id(my_list))
print(id(my_list_3))
my_list.append('Python ist cool')
print(my_list)
print(my_list_3)

Übung:

my_list_uebung = ["d", "l", "r", "o", "w", " ", "i", "h", "s", "t"]

# So soll der Output aussehen:
# Aufgabe 1: hi world
# * ist in diesem Fall der "Unpacking Operator"
print(*my_list_uebung[-3::-1], sep = "")

# Aufgabe 2: wild
print(my_list_uebung[4] + my_list_uebung[6] + my_list_uebung[1] + my_list_uebung[0])

# Aufgabe 3: list
print(my_list_uebung[1] + my_list_uebung[-4] + my_list_uebung[-2] + my_list_uebung[-1])

# ------------------------
# Listen in listen
print("--------------------------------")
meine_liste = [1,2,3,4,5,[1,2,3,[True, "Hugo"]]]

print(meine_liste[2]) # bei ausgabe der drei in der ersten Liste
print(meine_liste[5][1]) # ausgabe der 2 in der zweiten Liste
print(meine_liste[5][3][1]) # ausgabe von Hugo in der dritten Liste

# ---------------------------------

arr=[[1,2],[3,4],[5,6]]

print(arr[0][1])
print(arr[1][1])
print(arr[2][1])
print("----------------------")

# Mehrdimensionale Arrays über append erzeugen
# erwartete Ausgabe: arr=[[1,2,[3,4]],[3,4],[5,6]]
arr[0].append(arr[1])
print(arr)

# Aufgabe zu nested lists - listen in listen

list_1 = [["hi", "two"], "yes", "house",[["home", "go"], "leave"]]
list_2 = ["thanks", "help", ["for", ["the", "great"], "good"], "am", "I"]

# Ausgabe per print() : hi I am home
# Ausgabe per print() : thanks for the help
# Ausgabe per print() : yes go home
