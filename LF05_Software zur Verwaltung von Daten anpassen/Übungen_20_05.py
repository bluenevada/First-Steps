# my_list_uebung = ["d", "l", "r", "o", "w", " ", "i", "h", "s", "t"]
 
# # So soll der Output aussehen:

# # Aufgabe 1: hi world
# print(my_list_uebung[7],my_list_uebung[6],my_list_uebung[5],my_list_uebung[4],my_list_uebung[3],my_list_uebung[2],my_list_uebung[1],my_list_uebung[0])
# print(my_list_uebung[-3:-11:-1])

# # * ist in diesem Fall der unpacking operator
# print(*my_list_uebung[-3::-1], sep = "")

# # Aufgabe 2: wild
# print(my_list_uebung[4], my_list_uebung[6], my_list_uebung[1], my_list_uebung[0])

# # Aufgabe 3: list
# print(my_list_uebung[1], my_list_uebung[6], my_list_uebung[8], my_list_uebung[9])

# #Alternative:
# # So soll der Output aussehen:
# # Aufgabe 1: hi world
# print("".join(my_list_uebung[7::-1]))

# # Aufgabe 2: wild
# print("".join(my_list_uebung[i] for i in [4, 6, 1, 0]))

# # Aufgabe 3: list
# print("".join(my_list_uebung[i] for i in [1, 6, 8, 9]))

# #---------------------------------------------------------------------------

# #Bilde die folgenden Sätze, in dem du Daten aus den gegebenen Listen extrahierst:

# # 1. hi I am here
# # 2. thanks for the help
# # 3. yes go home

# # list_1 = [["hi", "two"], "yes", "house", [["home", "go"], "leave"]]
# # list_2 = ["thanks", "help", ["for", ["the", "great",], "good"], "am", "I"]
# # list_1.append("here")

# # print(list_1[0][0], list_2[-1], list_2[-2], list_1[-1])
# # print(list_2[0], list_2[2][0], list_2[2][1][0], list_2[1])
# # print(list_1[1], list_1[3][0][1], list_1[3][0][0])

# # # Aufgabe 2
# # one = False
# # b = True
# # hello = not(one) #True
# # test = not(b) #False

# # print(not one and test)             #False
# # print(hello and test or one and b)  #False
# # print(hello is one)                 #False
# # print(test is b or hello and b)     #True
# # print(not b is hello or one)        #False
# # print(hello or test or b)           #True

# # Eine Faustformel, um Hundejahre in Menschenjahre umzurechnen, ist das Alter des
# # Hundes mit 7 zu multiplizieren.
# # Je nach Hundegröße und Rasse sieht die Umrechnung jedoch etwas anders aus,
# # - Ein einjähriger Hund entspricht in etwa einem 14-jährigen Menschen.
# # - 2 Jahre eines Hundes entsprechen 22 Jahre eines Menschen.
# # - Ab dann entspricht ein Hundejahr jeweils 5 Menschenjahren.
 
# # TASK: Schreibe ein Programm, das das Alter eines Hundes entgegennimmt und das
# #       entsprechende Menschenalter ausgibt.

# print("I can calculate the age of your dog in human years")
# print("How old is your dog?")
# age_dog = float(input())

# if age_dog <= 0:
#     print("Your dog must be born")
# elif age_dog <= 1:
#     age_human = 14
# elif age_dog <= 2:
#     age_human = 22
# elif age_dog > 30:
#     print("Your dog should be dead by now")
# else:
#     age_human = age_dog * 5

# print("The age of the dog equals", age_human, "years in human age")
 
# # Übung 2:
# # Wir brauchen ein kleines Programm, was uns eine Begrüßung abhängig der
# # aktuellen Uhrzeit ausgibt.
 
# # 22:00 - 05:00: Gute Nacht!
# # 05:00 - 11:00: Guten Morgen!
# # 11:00 - 15:00: Mahlzeit!
# # 15:00 - 18:00: Guten Nachmittag!
# # 18:00 - 22:00: Guten Abend!
 
# # TASK: Schreibe ein Programm, was eine der Uhrzeit entsprechende Begrüßung ausgibt.
# #       Teste mit random und/oder input.

# # import datetime
# # print("Wie viel Uhr haben wir?")
# # jetzt = input()
# # jetzt = datetime.datetime.strptime(jetzt, "%H:%M").time()


# import datetime
# jetzt = datetime.datetime.now()
# print("Es ist", jetzt.hour, ":", jetzt.minute)

# if jetzt.hour >= 22 or jetzt.hour < 5:
#     print("Gute Nacht!")
# elif jetzt.hour >= 5 and jetzt.hour < 11:
#     print("Guten Morgen!")
# elif jetzt.hour >= 11 and jetzt.hour < 15:
#     print("Mahlzeit!")
# elif jetzt.hour >= 18 and jetzt.hour < 22:
#     print("Guten Abend!")

# Nutze alle drei Möglichkeiten, um ein Dictionary mit den folgenden Daten und passenden Keys zu erstellen:
 
# 1. Paper, 325, International Paper, 1350.75
# 2. Pencil, 55, Faber Castell, 321.62
# 3. Printer Ink, 30, Epson, 287.36

# 1. Paper, 325, International Paper, 1350.75
my_first_dict = {
    "product": "Paper"
    "amount": 325
    "company": "International Paper"
    "price": 1350.75
}

print(my_first_dict)
print(my_first_dict['product'])

# 2. Pencil, 55, Faber Castell, 321.62
list_log = ["product", "amount", "company", "price"]
list_pen = ["Pencil", 55, "Farber Castell", 321.62]

my_pen_dict = dict(zip(list_log, list_pen))
print(my_pen_dict)

# 3. Printer Ink, 30, Epson, 287.36

my_last_dict = dict(product = "Printer Ink", amount = 30, company = "Epson", price = 1350.75)