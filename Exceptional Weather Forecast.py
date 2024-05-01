#Task 1:


def get_temperature():
    while True:
        temperature_str = input("Enter the temperature in Fahrenheit: ")
        try:
            temperature = float(temperature_str)
            return temperature
        except ValueError:
            print("Error: Enter a valid numerical temperature.")

temperature = get_temperature()
print("Temperature entered:", temperature)




#Task 2:


def fahrenheit_to_celsius(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius
    except Exception as e:
        print("An error occurred during temperature conversion:", e)

temperature = 75  
celsius_temperature = fahrenheit_to_celsius(temperature)
if celsius_temperature is not None:
    print("Celsius temperature:", celsius_temperature)




#Task 3:


def fahrenheit_to_celsius(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * 5 / 9
    except Exception as e:
        print("An error occurred during temperature conversion:", e)
    else:
        print("The temperature in Celsius is {:.2f}°C.".format(celsius))
    finally:
        print("Thank you for using the weather forecast application!")

temperature = 75
fahrenheit_to_celsius(temperature)
