print("What do you want to calculate?")
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
    bin_num = input("Enter a binary number:")
    bin_num = int(bin_num, 2)
    hex_num = hex(bin_num)
    hex_num = hex_num.lower().lstrip("0x")
    print(hex_num)

#hex-bin
elif type == 2:
    hex_num = input("Enter a hexadecimal number:")
    hex_num = int(hex_num, 16)
    bin_num = bin(hex_num)
    bin_num = bin_num.lower().lstrip("0b")
    print(bin_num)

#dec-bin
elif type == 3:
    dec_num = input("Enter a decimal number:")
    dec_num = int(dec_num)
    bin_num = bin(dec_num)
    bin_num = bin_num.lower().lstrip("0b")
    print(bin_num)
#bin-dec
elif type == 4:
    bin_num = input("Enter a binary number:")
    bin_num = int(bin_num, 2)
    dec_num = int(bin_num)
    print(dec_num)

#dec-hex
elif type == 5:
    dec_num = input("Enter a decimal number:")
    dec_num = int(dec_num)
    hex_num = hex(dec_num)
    hex_num = hex_num.lower().lstrip("0x")
    print(hex_num)

#hex-dec
elif type == 6:
    hex_num = input("Enter a hexadecimal number:")
    hex_num = int(hex_num, 16)
    dec_num = int(hex_num)
    print(dec_num)

else:
    print("Invalid input!")