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

# list_1 = [["hi", "two"], "yes", "house", [["home", "go"], "leave"]]
# list_2 = ["thanks", "help", ["for", ["the", "great",], "good"], "am", "I"]
# list_1.append("here")

# print(list_1[0][0], list_2[-1], list_2[-2], list_1[-1])
# print(list_2[0], list_2[2][0], list_2[2][1][0], list_2[1])
# print(list_1[1], list_1[3][0][1], list_1[3][0][0])

# Aufgabe 2
one = False
b = True
hello = not(one) #True
test = not(b) #False
 
print(not one and test) #False
print(hello and test or one and b) #False
print(hello is one) #False
print(test is b or hello and b) #True
print(not b is hello or one) #False
print(hello or test or b) #True