import random

dec_num = random.randint(0,1000)

bin_num = bin(dec_num)
bin_num = bin_num.lower().lstrip("0b")

hex_num = hex(dec_num)
hex_num = hex_num.lower().lstrip("0x")

print("What do you want to learn?")
print("Type 1 for bin - hex")
print("Type 2 for hex - bin")
print("Type 3 for dez - bin")
print("Type 4 for bin - dez")
print("Type 5 for dez - hex")
print("Type 6 for hex - dez")

type = input()
type = int(type)

#bin-hex
if type == 1:
    print(bin_num)
    print("Enter the number in hex:")
    answer = input()

    while answer != hex_num:
        print("Wrong answer! Try again:")
        answer = input()

    print("Right answer!")

#hex-bin
elif type == 2:
    print(hex_num)
    print("Enter the number in bin:")
    answer = input()

    while answer != bin_num:
        print("Wrong answer! Try again:")
        answer = input()

    print("Right answer!")

#dez-bin
elif type == 3:
    print(dec_num)
    print("Enter the number in bin:")
    answer = input()

    while answer != bin_num:
        print("Wrong answer! Try again:")
        answer = input()

    print("Right answer!")

#bin-dez
elif type == 4:
    print(bin_num)
    print("Enter the number in dez:")
    answer = input()

    while answer != dec_num:
        print("Wrong answer! Try again:")
        answer = input()

    print("Right answer!")

#dez-hex
elif type == 5:
    print(dec_num)
    print("Enter the number in hex:")
    answer = input()

    while answer != hex_num:
        print("Wrong answer! Try again:")
        answer = input()

    print("Right answer!")

#hex-dez
elif type == 6:
    print(hex_num)
    print("Enter the number in dez:")
    answer = input()

    while answer != dec_num:
        print("Wrong answer! Try again:")
        answer = input()

    print("Right answer!")

else:
    print("Invalid function chosen!")