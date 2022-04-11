celsius = float(input('Enter the temperature to be converted to Fahrenheit: '))
fahrenheit = (celsius * 9/5)+32

print(f'{celsius} degrees Celsius converts to {fahrenheit:.1f} degrees Fahrenheit')

fahrenheit = float(input('Enter the temperature to be converted to Celsius: '))
celsius = ((fahrenheit-32)/(9/5))

print(f'{fahrenheit} degrees Fahrenheit converts to {celsius:.1f} degrees Celsius')
