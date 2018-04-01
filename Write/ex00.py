#!/usr/bin/env python

# My program performs three tasks in a row on a given phrase
# By: Amar Waraich


def greet():
    talk = input("Enter a phrase: ")
    return talk


def cap(s):
    ret = ""
    makeLower = False  # capitalize
    for char in s:
        if char.isalpha():
            if makeLower:
                ret += char.lower()
            else:
                ret += char.upper()
            if char != ' ':
                makeLower = not makeLower
        else:
            ret += char
    print (ret)
    return (ret)





def ast(s):

    ret = ""
    balance = 0
    for char in s:
        if char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
            ret += "*"
        elif char == "(":
            balance += 1
            ret += char
        elif char == ")":
            balance -= 1
            ret += char
        else:
            ret += char
    print(ret)
    if balance == 0:
        print("Balanced? True")
    else:
        print("Balanced? False")


def main():
    s = greet()
    s_cap = cap(s)
    ast(s_cap)


main()
