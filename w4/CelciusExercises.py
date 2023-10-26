'''

Celcius Fahrenheit Converter

'''

''' C to F '''
celcius = float(input("Enter a C which i will return to F:"))
fahrenheit = (9/5)*celcius + 32
print(celcius, "celcius is", fahrenheit, "fahrenheit")
print("fahrenheit is:", fahrenheit)


''' F to C '''
fahrenheit = float(input("Enter a F which i will return to C:"))
celcius = (5/9)*(fahrenheit-32)
print(celcius, "celcius is", fahrenheit, "fahrenheit")

