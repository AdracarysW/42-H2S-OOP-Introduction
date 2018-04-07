
from firstclass import First
import random

class Second(First):

    def __init__(self, name, hobby):
        super().__init__(name, self.number())
        self.hobby = hobby

    def number(self):
        print("Number method in SecondClass called")
        rand_num = random.randint(1, 6)
        return rand_num

    def getHobby(self):
        return self.hobby
