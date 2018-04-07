
class First():

    def __init__(self, name, number):
        self.name = name
        self.Hello(number)

    def Hello(self, number):
        print("Method Hello in FirstClass is called")
        print("Hello {}, your number is {}".format(self.name, number))
