# 10. Implementar una función que convierte temperaturas de fahrenheit a celsius.

def fahrenheitCelsius(f):
    c = (f - 32) * 5 / 9
    return c

tempFahrenheit = 212
print(f"{tempFahrenheit} grados Fahrenheit son equivalentes a {fahrenheitCelsius(tempFahrenheit)} grados Celsius.")
