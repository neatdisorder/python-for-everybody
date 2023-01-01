# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

# (0 °C × 9/5) + 32 = 32 °F

celsius = input("Enter temperature in Celsius: ")
fahrenheit = (float(celsius) * 9/5) + 32
print("Temperature is " + str(fahrenheit) + " °F")