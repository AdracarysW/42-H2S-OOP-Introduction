#!/usr/bin/env python

# My program takes in a user input and welcomes them
# By awaraich


def greet():
    hello = input("Hello hacker, what is your name?\n>? ")
    return hello

def response(word):
    print("Welcome, " + word + ".")


def main():
    word = greet()
    response(word)

main()
