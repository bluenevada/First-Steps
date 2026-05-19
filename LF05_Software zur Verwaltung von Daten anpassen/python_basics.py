#Kommentare

#Das hier: # ist ein Single-Line Comment
#Das hier: """ Kommentar """ ist ein Multiline Comment
#Das hier: """ :param firstname: Variable für den Vornamen """ ist ein Doc-String
#Beispiel zu Doc-String:
a = 40
b = 2

def addieren(a,b):
    """
    :param a: Zahl 1
    :param b: Ist die Zahl 2
    :return: gibt die Summe zweier Zahlen als Integer zurück
    """
    return a+b
print(addieren(a, b))

firstname = "GFN"

#Output einer Variablen
print(firstname)
print(id(firstname))

#Diese Aktion referenziert nur auf die Speicheradresse und erstellt keine echte Kopie
company_name = firstname
print(company_name)
print(id(company_name))
company_name = "Amadeus Fire AG"
print("--- nach Änderung ---")
print(company_name)
print(id(company_name))

#Output einer Variablen mit einem String (Zeichenkette)
print("--- Variable und Stringausgabe mit + ---")
print("Mit + Zeichen: Das ist mein Vorname " + firstname)
print("--- Variable und Stringausgabe mit , ---")
print("Mit , Zeichen: Das ist mein Vorname", firstname)
print("--- Variable und Stringausgabe mit F-String ---")
print(f"Mit + Zeichen: Das ist mein Vorname {firstname}")

#sep & end
print("Das Wetter ist schön", " war es zumindest heute Morgen", sep = "|||")

print("Hallo", end = " ")
print("Welt")

#Aufgabe:
print("Wir", "lernen", "gerade")
print("Python")

#Ziel: Wir***lernen***gerade...Python
print("Wir", "lernen", "gerade", sep = "***", end = "...")
print("Python")

#Input - wir wollen eine Usereingabe
#Speichert immer einen String
firstname_new = input("Gib bitte deinen Vornamen an: ")
age = int(input("Gib dein alter an: "))

print(firstname_new)
print(age + 11)

# ------------------------------
#Datentypen
#str - string - Text
#int - Integer - Ganzzahl (42)
#float - Float - Fließkommazahlen (42.0)
#bool - Boolean - Wahrheitswert (True/False)

# Aufgabe: Den jeweiligen Datentyp ermitteln
# Hier steht der nötige Basiscode für die Aufgabe
name = "Brutus" #str
street = "Zellenstrasse" #str
house_number = 25 #int
height = 1.86 #float
is_married = True #bool
married_date = "15.04.2009" #str
has_kids = False #bool

#Die Funktion type gibt den Datentyp an
print(type(name))
print(type(street))
print(type(house_number))
print(type(height))
print(type(is_married))
print(type(married_date))
print(type(has_kids))

#Mit dem Zusatz .__name__ wird <class''> nicht mitgeprinted
print(type(name).__name__)
print(type(street).__name__)
print(type(house_number).__name__)
print(type(height).__name__)
print(type(is_married).__name__)
print(type(married_date).__name__)
print(type(has_kids).__name__)

#Datentypen konvertieren
#Funktion str() konvertiert den Variableninhalt in einen String. Funktioniert mit allen Inhalten
boolscher_wert = True
print(type(boolscher_wert))
bl_2 = str(boolscher_wert)
print(type(bl_2))

#Funktion int() konvertiert den Variableninhalt in einen Int. Funktioniert nur bei Zahlen
my_string = "42" #ohne die "" wäre es kein String
print(int(my_string))

#Funktion float() konvertiert den Variableninhalt in einen Float. Funktioniert nur bei Zahlen.
my_string_2 = 42
print(float(my_string))

#Funktion bool() kovertiert den Variableninhalt in einen boolean. Funktioniert bei allen Inhalten.
my_string_3 = "Wetter"
print(bool(my_string_3))

my_string_3 = ""
print("Nach Überschreibung: ", bool(my_string_3))

#Aufgabe:

variable1 = "25"
variable2 = 10
variable3 = "Ich bin eine Variable."
 
print(int(variable1) + 5) # Die Ausgabe soll "30" sein
print(str(variable2) + " ist eine Zahl.") # Die Ausgabe soll "10 ist eine Zahl." sein
print(bool(variable3) + 1) # Die Ausgabe soll "2" sein

#Snake_Case_Schreibweise = variable_1
#Camel_Case_Schreibweise = ersteVariable
#Pascal_Case_Schreibweise = ErsteVariable