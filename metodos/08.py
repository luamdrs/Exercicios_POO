class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius


    def para_fahrenheit(self):
        return (self.celsius * 9/5) + 32
    

    @classmethod
    def de_fahrenheit_para_celsius(cls, fahrenheit):
        return (fahrenheit - 32) * 5/9
    

temp1 = Temperatura(25)
print(f'25°C em Fahrenheit: {temp1.para_fahrenheit()}')

fahrenheit = 77
print(f'77°F em Celsius: {Temperatura.de_fahrenheit_para_celsius(fahrenheit)}')