def divide_number_finder(min_value, max_value, divider_value):
    fully_divisable = []
    for n in range (min_value, max_value+1):
        if n%divider_value == 0:
            fully_divisable.append(n)
    return fully_divisable

def main():
    running = True
    while(running) :
        min = input("Please input the minimum value: ")
        max = input("Please input the maximum value: ")
        divider = input("Please input the divider value: ")
        print(divide_number_finder(int(min), int(max), int(divider)))
        answer = input("press ENTER to quit: ")
        if answer == "":
            break

if __name__ == "__main__":
    main()

