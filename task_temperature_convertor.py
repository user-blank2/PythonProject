class TemperatureConverter:
    def __init__(self,celsius,fahrenheit):
            self.celsius=celsius
            self.fahrenheit=fahrenheit

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return  (celsius * 9//5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return  (fahrenheit - 32) * 5//9


temp =TemperatureConverter(32,102)

print(TemperatureConverter.celsius_to_fahrenheit(temp.celsius))
print(TemperatureConverter.fahrenheit_to_celsius(temp.fahrenheit))