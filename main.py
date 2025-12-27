#!/usr/bin/python3

def sum_until_target(target):
    number = 0
    sum = 0
    
    while sum < target:
        number += 1
        sum += number

    return sum

def sum_until_over(limit):
    number = 0
    sum = 0

    while sum <= limit:
        number += 1
        sum += number
    
    return sum

def add_evens_over(limit):
    number = 0
    sum = 0

    while sum <= limit:
        number += 2
        sum += number

    return sum

def count_additions(target):
    num = 0
    sum = 0
    addition_count = 0

    while sum < target:
        num += 1
        sum += num
        addition_count += 1

    return addition_count



test1 = sum_until_target(55)
test2 = sum_until_over(55)
test3 = add_evens_over(10)
test4 = count_additions(20)

print(test1, test2, test3, test4)
