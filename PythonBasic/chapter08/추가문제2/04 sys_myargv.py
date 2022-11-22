import sys

def number_print(number_list):
    total = 0
    for number in number_list:
        total += int(number)
    print(total)

number_list = sys.argv[1:]


number_print(number_list)