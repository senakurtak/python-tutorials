''''
def name(inputs):
#func body
return output
'''

def info():
    print("Bu bir eğitim örneğidir.")
    print("Use it with your own risk")
    
def greet(name="İsimsiz"):
    if name == "Sena":
        name = "Patron"
    print("Merhaba", name, "hoşgeldiniz!")
    
def minimum(o1, o2):
    if o1<o2:
        return o1
    else:
        return o2

info()

a = 46
b = 32

c = minimum(a,b)
d = minimum(o2= 292, o1=291)
info()
greet("Sena")
greet("Emin")
greet()

pass