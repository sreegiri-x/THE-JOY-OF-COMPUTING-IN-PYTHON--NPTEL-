# Solution: Celsius to Fahrenheit (Week 4, Programming Problem 3)

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

temp_c = float(input("Enter temperature in Celsius: "))
print(f"{temp_c}°C = {celsius_to_fahrenheit(temp_c)}°F")
