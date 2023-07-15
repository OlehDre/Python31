
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, next):  #Додавання
        return self.value + next.value

    def __sub__(self, next):  #Різниця
        return self.value - next.value

    def __mul__(self, next):  #Множення
        return self.value * next.value

    def __truediv__(self, next):  #Ділення
        return self.value / next.value

    def __floordiv__(self, next):
        return self.value // next.value

    def __pos__(self):
        self.value = self.value + 1
        return self.value


    def __mod__(self, next):
        return self.value % next.value

num1 = Number(5)
num2 = Number(34)


print(num2 % num1)
