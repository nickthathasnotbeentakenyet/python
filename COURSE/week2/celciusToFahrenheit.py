# heading
print("="*50)
print("="*13 + " Temperature Calculator " + "="*13)
print("="*50 + "\n")

# calculations and ouput
temperature_fahrenheit = float(input("What is the temperature in Fahrenheit?: "))
temperature_celcius = (temperature_fahrenheit - 32) * 5 / 9
print(f"The temperature in Celsius is {temperature_celcius:.1f} degrees.\n")