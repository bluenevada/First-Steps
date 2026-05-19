def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer greater than 0."
    elif n < 1 :
        return "Argument must be an integer greater than 0."
    else:
        num_list = []
    for i in range(1, n+1):
        num_list.append(i)
        result = ' '.join(str(num) for num in num_list)
    return result

number_pattern(4)
number_pattern(12)