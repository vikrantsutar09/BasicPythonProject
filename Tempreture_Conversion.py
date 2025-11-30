
unit = input("Is this tempreture in celsius or fahrenheit (C / F): ")
temp = float(input("Enter the tempreture: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The tempreture in fahrenheit is: {temp}F")
elif unit == "F":
    temp = round((temp -32) * 5 / 9,1)
    print(f"The tempreture in celcius is: {temp}C")
else:
    print(f"{unit} is an invalid unit o measurement")