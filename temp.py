# Step 1 - Convert Temperature from Celsius to Fahrenheit
# Create a program file named temp.py.
# Construct a python statement to convert 25 degrees Celsius to Fahrenheit
# the formula
# Output the Celsius and Fahrenheit values with an appropriate print statement
# Commit your changes
# Step 2 - Function to Convert Temperature from Celsius to Fahrenheit
# Edit temp.py to create a function called celsius_to_fahrenheit that takes one parameter, celsius
# the function celsius_to_fahrenheit should return the temperature in Fahrenheit.
# Write a function call to convert 25 degrees Celsius to Fahrenheit and print the result.
# Commit your changes
# Step 3 - Function to Convert Temperature from Fahrenheit to Celsius
# Edit temp.py to add an appropriate function that converts Fahrenheit to Celsius
# Write a function call to convert 82 degrees Fahrenheit to Celsius and print the result.
# Commit your changes



""" progarm to convert Celsius to Fahrenhiet """


def celsius_to_fahrenhiet():
    """Convert given value to fahrenhiet"""
    fah = celsius * 9/5 +32
    return fah 



#progarm to convert Celsius to Fahrenhiet 
celsius = 25
fah = celsius_to_fahrenhiet(celsius)
print(f"{celsius} degress is {fah} Fahrenheit")