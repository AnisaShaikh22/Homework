def divide_number_finder(min_value, max_value, divider_value):
    fully_divisable = []
    for n in range (min_value, max_value+1):
        if n%divider_value == 0:
            fully_divisable.append(n)
    return fully_divisable

print(divide_number_finder(1,22,4))
