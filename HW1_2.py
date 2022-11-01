def number_allocation(num):
    if num>=100 or num<=9:
        raise ValueError("The number should have two digits")
    return num

def number_pronounciation(num):
    number = number_allocation(num)
    data = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
        6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
        11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
        15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
        19 : 'nineteen', 20 : 'twenty',
        30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
        70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }

    if (number < 20):
        return str(number) + "--> "+data[number]

    if (20<= number < 100):
        if number % 10 == 0:
            return str(number) + "--> "+data[number]
        else:
            return str(number) + "--> "+data[number // 10 * 10] + ' ' + data[number % 10]

## Test
## Uncomment each line to do the test

print(number_pronounciation(25))
print(number_pronounciation(87))
print(number_pronounciation(109)) #ValueError
print(number_pronounciation(7)) #ValueError
