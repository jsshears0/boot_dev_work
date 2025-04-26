class Calculator:
    def __init__(self):
        self.__result = 0

    def add(self, a):
        self.a = a
        self.__result += self.a

    def subtract(self, a):
        self.a = a
        self.__result -= self.a

    def multiply(self, a):
        self.a = a
        self.__result *= self.a

    def divide(self, a):
        self.a = a
        if self.a == 0:
            raise ValueError("cannot divide by zero")
        else:
            self.__result /= self.a

    def modulo(self, a):
        self.a = a
        if self.a == 0:
            raise ValueError("cannot divide by zero")
        else:
            self.__result %= self.a

    def power(self, a):
        self.a = a
        self.__result **= self.a

    def square_root(self):
        self.__result **= .5

    def clear(self):
        self.__result = 0

    def get_result(self):
        return self.__result