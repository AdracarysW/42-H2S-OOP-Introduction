
import random

class Second:

    def __init__(self):
        name = input("Enter your name: ")
        num = self.number()
        super().__init__(name, num)


    def number(self):
        print("Number method in SecondClass called")
        random_num = random.randint(1, 6)
