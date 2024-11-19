import random


def recalculatetotal(one_count, two_count, five_count, ten_count, twenty_count, fifty_count, hundred_count):
    ones_total = one_count * 1
    two_total = two_count * 2
    five_total = five_count * 5
    ten_total = ten_count * 10
    twenty_total = twenty_count * 20
    fifty_total = fifty_count * 50
    hundred_total = hundred_count * 100
    grand_total = ones_total + two_total + five_total + ten_total + twenty_total + fifty_total + hundred_total
    return grand_total


def totalcalc(count, multiplier):
    total = count * multiplier
    return total


def generate_unique_id(length):
    unique_id = ""
    for i in range(length):
        random_number = random.randint(0, 35)
        character = chr(random_number + 48)
        if random_number < 10:
            character = chr(random_number + 65)
        unique_id += character
    return unique_id
