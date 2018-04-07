
from firstclass import First
import random

class Second(First):

    def __init__(self, name):
        super().__init__(name, self.number())

    def number(self):
        print("Number method in SecondClass called")
        rand_num = random.randint(1, 6)
        return rand_num
