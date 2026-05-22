datenbank_name = "Davy"
datenbank_pw = "ganzgeheim"

username = input("Bitte gib deinen Usernamen ein: ")
password = input("Bitte gib dein Passwort ein: ")
age = int(input("Bitte gib dein Alter an: "))

# print(username == datenbank_name)
# print(password == datenbank_pw)
username_sanitized = username.strip() # Leerzeichen entfernen

correct_username = username_sanitized == datenbank_name # prüfung auf equality
print(correct_username )

correct_pw = password == datenbank_pw

if correct_username and correct_pw:
    print("Du bist erfolgreich eingeloggt") # Steigt der Interpreter aus dem Code
elif age >= 18: # Code Schwachstelle - Logischer Fehler
    print("Und du bist alt genug für die Inhalte")
else:
    print("Username oder Passwort ist falsch oder du bist zu jung")
    

