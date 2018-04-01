#!/usr/bin/env python

# My program prints a certain string depending on the name of the person
# By awaraich


def getWords():
    title = input("Please input a title: ")
    adjective = input("Please input an adjective: ")
    buisness = input("Please input a buisness: ")
    animal = input("Please input an animal: ")
    noise = input("Please input a noise: ")
    return [title, adjective, buisness, animal, noise]

def outPut(words):
    print ('')
    print (words[0])
    print (words[1], "Macdonald had a", words[2] + ", E-I-E-I-O")
    print ("and on that " + words[2] + " he had a " + words[3] + ", E-I-E-I-O")
    print ("with a " + words[4] + " " + words[4] + " here")
    print ("and a " + words[4] + " " + words[4] + " there,")
    print ("here a " + words[4] + ", there a " + words[4] + ",")
    print ("everywhere a " + words[4] + " " + words[4] + ",")
    print (words[1] + " Macdonald had a " + words[2] + ", E-I-E-I-O!")

def main():
    words = getWords()
    outPut(words)

main()
