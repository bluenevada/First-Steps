# # Kommentare

# # Das hier: # ist ein Single-Line Comment
# # Das hier: """ Kommentar """ ist ein Multiline Comment
# # Das hier: """ :param firstname: Variable für den Vorname """ ist ein Doc-String
# # Beispiel zu Doc-String: 
# # a = 40
# # b = 2

# # def addieren(a, b):
# #     """
# #     :param a: Zahl 1
# #     :param b: Ist die Zahl 2
# #     :return: gibt die Summe zweier Zahlen als Integer zurück
# #     """
    
# #     return a+b

# # Variablen

# # firstname = "GFN"

# # # Output einer Variable
# # print(firstname)

# # id() in print()
# # print(id(firstname))

# # # Diese Aktion referenziert nur auf die Speicheradresse und erstellt keine echte Kopie
# # company_name = firstname
# # print(company_name)
# # print(id(company_name))

# # # Output einer Variable mit einem String (Zeichenkettte)
# # print("--- Variable und Stringausgabe mit + ---")
# # print("Mit + Zeichen: Das ist mein Vorname" + firstname)

# # print("--- Variable und Stringausgabe mit , ---")
# # print("Mit , Zeichen: Das ist mein Vorname",firstname)

# # print("--- Variable und Stringausgabe mit F-String ---")
# # print(f"Mit F-String: Das ist mein Vorname {firstname}")

# # sep & end
# print("Das Wetter ist schön", "war es zumindest heute morgen", sep=" ")

# print("Hallo", end=" ")
# print("Welt")

# # Aufgabe:
# print("Wir","lernen", "gerade")
# print("Python")

# # Ziel: Wir***lernen***gerade...Python
# print("Wir","lernen", "gerade", sep="***")
# print(end="..." "Python")
# print("Hallo")

# # '''''''''''''''''''''

# # Input -  wir wollen eine Usereingabe
# # Speichert immer einen String
# # firstname_new = input("Gib bitte deinen Vornamen an: ")
# # Beispiel für eine Typumwandlung bei User-Input

# # age = input("Gib gib dein Alter an: ")
# # age_new = int(age)

# # # Kurzfassung: age = int(input("Gib gib dein Alter an: "))

# # # print(firstname_new)
# # print(age + 11)

# # Googlen: Es gibt eine Built-In Funktion, die es ermöglicht mit Zahlen in Strings zu rechnen

# # -------------------------------
# # Datentypen
# # str - String - Text  ("Das Wetter ist gut")
# # int - Integer - Ganzzahl (42)
# # float - Float - Zahlen mit Komma / Fließkommazahlen / Gleitkommazahlen (42.0)
# # bool - Boolean - Wahrheitswert (True & False)

# # Aufgabe: Den jeweiligen Datentyp ermitteln
# # Hier steht der nötige Basiscode für die Aufgabe
# # name = "Brutus"
# # street = "Zellenstrasse"
# # house_number = 25
# # height = 1.86
# # height_2 = .55
# # height_3 = 175.
# # is_married = True
# # married_date = "15.04.2009"
# # has_kids = False

# # print(type(name))
# # print(type(street))
# # print(type(house_number))
# # print(type(height))
# # print(type(height_2))
# # print(type(height_3))
# # print(type(is_married))
# # print(type(married_date))
# # print(type(has_kids))

# # Datentypen konvertieren

# # Funktion str() konvertiert den Variableninhalt in einen String. Funktioniert mit alle Inhalten

# # Beispiel str()
# # boolscher_wert = True
# # print(type(boolscher_wert))
# # bl_2 = str(boolscher_wert)
# # print(type(bl_2))

# # # Funktion int() konvertiert den Variableninhalt in einen Int. Funktioniert nur bei Zahlen

# # my_string = "42" # ohne die anführungszeichen wäre es kein str
# # print(int(my_string))

# # # Funktion float() konvertiert den Variableninhalt in einen Float. Funktioniert nur bei Zahlen
# # my_string_2 = 42
# # print(float(my_string_2))

# # Funktion bool() konvertiert den Variableninhalt in einen boolean. Funktioniert bei allen Inhalten
# # my_string_3 = "Wetter"
# # print(bool(my_string_3))

# # my_string_3 = ""
# # print("Nach überschreiben: ", bool(my_string_3))

# # Aufgabe 

# # Snake_Case_Schreibweise = variable_1
# # CamelCase = ersteVariable
# # Pascal Case = ErsteVariable

# # variable_1 = "25"
# # variable_2 = 10
# # variable_3 = "Ich bin eine Variable."

# # # print(variable1 + 5) # Die Ausgabe soll "30" sein
# # # print(variable2 + " ist eine Zahl.") # Die Ausgabe soll "10 ist eine Zahl." sein
# # # print(variable3 + 1) # Die Ausgabe soll "2" sein''

# # True = 1
# # False = 0 

# # print(int(variable_1) + 5) 
# # print(str(variable_2) + " ist eine Zahl.") 
# # print(bool(variable_3) + 1) 

#---------------------------------------------
# TAG 2
#---------------------------------------------

# # Listen
# print("-------------------------")
# # Eine Variable trägt immer nur einen Inhalt
# firstname = "Davy"

# # Eine Liste trägt viele Inhalte
# # Wir können Datentypen vermischen
# firstnames = ["Davy", True, "Florian", 42, "Max", 44.5, "Yves", [1,2,3]]

# print(firstnames)
# print(firstnames[0]) # 0-indexiert
# print(firstnames[-1]) # Rückwärts geht auch - gibt das letzte Element der Liste aus

# # Eintrag durch Angabe der Index-Position überschreiben
# firstnames[0] = 'Jones'
# # Neue, leere Liste erzeugen + append() + extend()
# new_list = []
# new_list = list() # selten gesehen 
# print(f"Inhalt der neuen Liste: {new_list}")

# # append() fügt einen Inhalt hinzu
# new_list.append("Neuer Eintrag")
# print(f"Inhalt der geänderten Liste: {new_list}")
# new_list.append("Zweiter Eintrag")
# print(f"Inhalt der geänderten Liste: {new_list}")
# # extend() fügt mehrere Inhalte  hinzu
# new_list.extend([5,6,7])
# print(f"Inhalt der mit extend geänderten Liste: {new_list}")
# # insert() fügt den Inhalt mit der Indexposition an die gewünschte Stelle hinzu
# new_list.insert(5, 'GFN')
# print(f"Inhalt der mit insert geänderten Liste: {new_list}")
# # remove() löscht einen Inhalt. allerdings nur den ersten davon. Gibt es die 42 mehrmals, wird nur die erste in der Liste gelöscht
# new_list.append("Neuer Eintrag")
# new_list.remove('Neuer Eintrag')
# print(f"Inhalt der mit remove geänderten Liste: {new_list}")
# # clear() leert die gesamte Liste
# new_list.clear()
# print(f"Inhalt der mit clear geänderten Liste: {new_list}")

# # List Slicing

# my_list = [1,3,4,5,7,9,42]

# print(my_list[0]) # Ausgabe: 1
# print(my_list[0:3]) # Ausgabe: 1,3,4 Tipp: einfach von der letzten Zahl (bei zwei Zahlen) die erste Zahl abziehen um zu errechnen wie viele Elemente ich bekommen sollte

# # Mit Schrittweite
# print(my_list[0:7:2]) # Start - Stop - Step

# # Test - funktioniert
# print("mit len(): ", my_list[0:len(my_list):2])

# print("---------------------")
# my_list_2 = my_list
# print("my_list_2: ", my_list_2)

# print(id(my_list))
# print(id(my_list_2))

# my_list.append("Smartphone")
# print(my_list_2)

# my_list_2[0] = 'GFN'
# print("--- Neue ausgabe nach Veränderung ---")
# print(my_list)
# print(my_list_2)
# print(id(my_list))
# print(id(my_list_2))
# print("--- Mit Full Slicing ---")
# my_list_3 = my_list[:] # Full Slicing um eine echte Kopie, die unabhängig von der bisherigen Liste ist, zu erstellen
# print(id(my_list))
# print(id(my_list_3))
# my_list.append('Python ist cool')
# print(my_list)
# print(my_list_3)

# Übung:

# my_list_uebung = ["d", "l", "r", "o", "w", " ", "i", "h", "s", "t"]

# # So soll der Output aussehen:
# # Aufgabe 1: hi world
# # * ist in diesem Fall der "Unpacking Operator"
# print(*my_list_uebung[-3::-1], sep = "")

# # Aufgabe 2: wild
# print(my_list_uebung[4] + my_list_uebung[6] + my_list_uebung[1] + my_list_uebung[0])

# # Aufgabe 3: list
# print(my_list_uebung[1] + my_list_uebung[-4] + my_list_uebung[-2] + my_list_uebung[-1])

# ------------------------
# Listen in listen
# print("--------------------------------")
# meine_liste = [1,2,3,4,5,[1,2,3,[True, "Hugo"]]]

# print(meine_liste[2]) # bei ausgabe der drei in der ersten Liste
# print(meine_liste[5][1]) # ausgabe der 2 in der zweiten Liste
# print(meine_liste[5][3][1]) # ausgabe von Hugo in der dritten Liste

# # ---------------------------------

# arr=[[1,2],[3,4],[5,6]]

# print(arr[0][1])
# print(arr[1][1])
# print(arr[2][1])
# print("----------------------")

# # Mehrdimensionale Arrays über append erzeugen
# # erwartete Ausgabe: arr=[[1,2,[3,4]],[3,4],[5,6]]
# arr[0].append(arr[1])
# print(arr)

# # Aufgabe:
# # nested lists - listen in listen

# list_1 = [["hi", "two"], "yes", "house",[["home", "go"], "leave"]]
# list_2 = ["thanks", "help", ["for", ["the", "great"], "good"], "am", "I"]

# # Ausgabe per print() : hi I am home
# print(list_1[0][0] , list_2[4] , list_2[3] , list_1[3][0][0] )

# # Ausgabe per print() : thanks for the help
# print(list_2[0] , list_2[2][0],  list_2[2][1][0] , list_2[1] )

# # Ausgabe per print() : yes go home
# print(list_1[1], list_1[3][0][1], list_1[3][0][0])

# # Funktioniert nur eingeschränkt bzw. mit dem Unpacking operator sogar sauber:
# # Ich würde die Variante nicht empfehlen
# print("mit slicing: ", list_1[1], list_1[3][0][1], *list_1[3][0][:1])

# list1 = [
#     ["hi", "two"], "yes", "house",
#         [
#             ["home", "go"], "leave"]
#                 ]

# list2 = ["thanks", "help", 
#           ["for", 
#               ["the", "great"], "good"], 
#           "am", "I"]

# # -----------------------------
# Vergleichsoperatoren + Logische Operatoren

# Größer als  a > b
# Größer gleich a >= b

# Kleiner als a < b
# Kleiner gleich a <= b

# equals
# a == b
# a === b in Python gibt es das nicht. Aber in PHP beispielsweise ist das der Typstarke Vergleich

# not equals
# a != b


# a = [1] 
# print(type(a))
# b = (1) # tuple
# print(type(b))

# if a == b:
#     print("Ja, sind gleich")
# elif a != b:
#     print("Ja, sind unterschiedlich")
# else:
#     print("Nein, sind nicht gleich")

# a = 42
# b = 2

# print(a < b)
# ---------------
# Aufgabe: 
# 1. "Test" == "test" = False
# 2. "und" > "&" = True
# 3. "-2" < "2" = True
# 4. "(Text)" > "{Text}" = False 

# --------------------------------------------------
# Logische Operatoren
# Beispiel der Prüfung inklusive if-elif-else 

# a_2 = " " # True
# b_2 = None # False
# print(type(a_2)) # String
# print(type(b_2)) # NoneType

# if a_2 and b_2:
#     print("Ja, sind True")
# elif a_2 != b_2:
#     print("Ja, sind unterschiedlich")
# else:
#     print("Sonstiges")
    
# # Short Circuit - Kurzschluss
# if a_2 or b_2:
#     print("Ja, erster ist True oder beide sind True")
# elif a_2 != b_2:
#     print("Ja, sind unterschiedlich")
# else:
#     print("Sonstiges")
# print("------------------------")

# # Aufgabe 1
# print(1 < 2 and 2 < 3) # True
# print(1 > 2 or 2 < 3) # True
# print(not True) # False
# print(not 1 < 2 and 2 < 3) # False
# # "in" Operator in Python/CPython prüfen
# print("e" in "hello") # True
# print("a" in "hello") # False

# # Aufgabe 2

# one = False
# b = True
# hello = not(one) # True
# test = not(b) # False

# print(not one and test) # Ergebnis: False
# print(hello and test or one and b) # False
# print(hello is one) # False
# print(test is b or hello and b) # True
# print(not b is hello or one) # False
# print(hello or test or b) # True

# if - elif - else
# Siehe Datei übung_true_false.py


# --------------------------------------
# Tag 3
# --------------------------------------

# Sets - ähnlich wie listen, aber sie sind unsortiert, nicht-indexiert und erlauben keine Dopplungen

# list_42 = ["Davy", 1, 1, "Jones", "Davy", 2, 2, 42, 42]

# # Set
# my_first_set = {"Davy", "Davy", "Jones"}
# print(my_first_set)

# # löschen mit remove()
# my_first_set.remove("Davy")
# print(my_first_set)

# # Einfügen geht mit add()
# my_first_set.add("GNF")
# print(my_first_set)

# # Listen um doppelte Einträge bereinigen. Nennt sich auch ein pythonisches Idiom
# print(list(set(list_42)))

# # Aufgaben nach for-Loop gezeigt

# #
# # Tuple - auch das gleiche wie Liste, können jedoch nicht verändert werden. 0-indexiert

# my_first_tuple = (1,2,3,4,5)

# print(my_first_tuple[1])

# Befehle, Built-Ins sind fast gleich zur Liste, aber können nicht verändert werden
# Geht nicht. Fehler: 'tuple' has no attribute 'append' 
# my_first_tuple.append(6)
# print(my_first_tuple[-1])
#

#
# Dicts
#
# Dictionaries besteht aus Schlüssel:Werte Paaren

# my_first_dict = {
#     "Name": "Sarah", 
#     "Age": 42, 
#     "Job":"Chef", 
#     "Standort": "München", # Git sagt, an dieser Stelle wurde was geändert, da bei Erweiterung hier noch ein Komma hinzugefügt werden muss
#     "Abteilung": "Vertrieb"
#     } # GIT - VCS (Version Control System) - GitHub 

# print(my_first_dict)
# print(my_first_dict['Name'])

# list_98 = ["Name", "Age", "Job"]
# list_99 = ["Fritz", "42", "Musiker"]

# zip()
# Challenge: wie kann ich die zip-Function aus Python manuell nachbauen. Gib mir lediglich tipps und einen Pseudocode als Startpunkt
# my_new_dict = dict(zip(list_98, list_99))
# print(my_new_dict)

#
# Aufgabe zu dict
# 
# Nutze alle drei Möglichkeiten, um ein Dictionary mit den folgenden Daten und passenden Keys (zum selber ausdenken) zu erstellen:

# 1. Paper, 325, International Paper, 1350.75
# 2. Pencil, 55, Faber Castell, 321.62
# 3. Printer Ink, 30, Epson, 287.36

# Lösung
# 1. Paper, 325, International Paper, 1350.75
# my_dict_11 = {
#     "Item": "Paper", 
#     "Amount": 325, 
#     "Supplier":"International Paper", 
#     "Price": "1350.75", 
#     }

# # 2. Pencil, 55, Faber Castell, 321.62
# my_dict_22 = dict(item = "Pencil", amount = 55, supplier = "Faber Castell", price = 1350.75)

# # 3. Printer Ink, 30, Epson, 287.36
# my_list_11 = ['item', 'amount', 'supplier', 'price']
# my_list_22 = ['Printer Ink', 30, 'Epson', 287.36]

# my_dict_33 = dict(zip(my_list_11, my_list_22))

# Testcode - nur die geschweiften Klammern, triggern nicht direkt zip bzw. geben nur die Objectreference zurück.
# # my_dict_33 = {
# #     zip(my_list_11, my_list_22)
# #     }

# print(my_dict_11, my_dict_22, my_dict_33)

#
# Befehle zu Dictionaries:
#

# len()
# print(len(my_dict))

# # get()
# print(my_dict.get("Name"))

# # in True
# print("Age" in my_dict)
# # in False
# print("Height" in my_dict)

# # update()
# my_dict.update({"Height": 176})
# print(my_dict)

# # del
# del my_dict["Occupation"]
# print(my_dict)

# # pop()
# print(my_dict.pop("Age"))
# print(my_dict)

# # clear()
# my_dict.clear()
# print(my_dict)

#
# Aufgabe 2 zu dict´s: 
# 

my_dict = {"Key1": False, "Key2": "Yes", "Key3": 1.5, "Key4": [1, 2, 3], "Key5": {"Name": "Peter"}}

# Manipuliere das gegebene Dictionary um die folgenden Outputs zu bekommen:
# Nutze dafür ein paar der Befehle von oben 

# 1. True
# 2. 3
# 3. 5
# 4. Peter
# 5. False Yes
# 6. {}

#
# for Loops
# Mit for Loops durchlaufen wir Objekte wie z.B. Listen und führen dabei bestimmte Aktionen aus

my_string = "Let's go!"
my_list = [1, 2, 3, 5]
names = ['Max', 'Lisa', 'Josi', 'Hugo']
# das i steht meist für index und aber auch für item. 
# for i in my_string:
#     print(i, end="")

for i in my_list:
    print(i)
    
for name in names:
    print(name)

# Range Function
for number in range(1, 7): # Start, Stop, step
    n_1 = 0
    n_1 += number
    print(n_1)

# In eigenen Worten gefasst: 
# Wir durchlaufen Datenspeicher und geben die Elemente aus

# List Comprehension - erweiterte for Loop
# perfekt geeignet für kurze schreibweisen. siehe Dokument List_Comprehension.pdf

#
# While - Loop
# Mache etwas, solange die Bedingung erfüllt ist

# Aufgabe: 
# Die erreichte Zahl wird doppelt ausgegeben. Wie verhindern wir das?
counter = 10

while counter >= 1:
    if counter % 2 == 0:
        print(f"Das ist eine gerade Zahl: {counter}")
    print(counter) # Wie verhindern, dass die gerade Zahl auch hier ausgegeben wird?
    counter -= 1
    