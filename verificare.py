##Opțiunea 4: Convertor de temperatură
##Cere o temperatură în grade Celsius și o transformă în Fahrenheit.
##Formula: Fahrenheit = Celsius × 9 / 5 + 32

##---------------------------------------------------------------------##

celsius = float(input("Introdu temperatura în grade Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius}°C = {fahrenheit}°F")