# function accepts temperature and wind speed, returns windchill factor
def calc_windChillF(t, s):
    return 35.74 + (0.6215 * t) - (35.75 * pow(s, .16)) + (.4275 * t * pow(s, .16))

# function accepts celsius, returns fahrenheit
def cels_to_fahr(celsius):
    return celsius * (9/5) + 32

# getting input from user
temperature = float(input("What is the temperature?: "))
t_system = input("Fahrenheit or Celsius (F/C): ").lower()

# in case user enters temperature in celsius degrees
if t_system == "c":
    temperature = cels_to_fahr(temperature)

# printing windchill factor for given temperature with speed range from 5 to 60 and step of 5
for wind in range(5,61,5):
    print(f"At temperature {temperature}°F, and wind speed {wind} mph, the windchill is: {calc_windChillF(temperature, wind):.2f}°F")
