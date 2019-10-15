def split_array(inputArray):
    total = sum(inputArray)

    if total % 2 != 0: return False

    number_iterator = iter(sorted(inputArray, reverse=True))
    value = total / 2
    while value > 0:
        number = next(number_iterator)
        value = value - ( number if value - number >= 0 else 0 )
    return value == 0;


