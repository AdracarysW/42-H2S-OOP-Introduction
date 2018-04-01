#!/usr/bin/env python

# My program prints a certain string depending on the name of the person
# By awaraich


def greet():
    threat = input("Who goes there?\n?> ")
    return threat

def answer(word):
    if word == "DHTFHNUQARFMQMKGSPRLRSKBCMD":
        print ("Welcome, Daenerys.")

    elif word == "Dany":
        print ("Dany who?")

    elif word == "Jaqen H\'gar":
        print ("Move along, now.")

    else:
        print ("Who are you?")

def main():
    word = greet()
    answer(word)

main()
