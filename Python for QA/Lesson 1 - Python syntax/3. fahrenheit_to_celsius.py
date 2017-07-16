# Write a program that converts Fahrenheit temperature to Celsius

# declare a variable and store temperature in Fahrenheit: 120
# convert the temperature from Fahrenheit to Celsius and print out: 48.888888888888886
# note 1: google to find the conversion formula from Fahrenheit to Celsius
# note 2: you may check correctness of your program via an online converter: https://www.mathsisfun.com/temperature-conversion.html

# test your program with following test cases:

# case 1: when temperature in Fahrenheit = 32, temperature in Celsius = 0.0
# case 2: when temperature in Fahrenheit = 212, temperature in Celsius = 100.0

temperature_in_fahrenheit = 120
temperature_in_celsius = (temperature_in_fahrenheit - 32) * 5 / 9
print(temperature_in_celsius)
