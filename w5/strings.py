name = "Sena"
surname = 'Kurtak'
age = 27
history = '''
your history
'''
print("Bilgileriniz:", name, surname, type(name), type(surname), type(age), type(history))

print("Napoleon: 'Para Para Para' ")
print('Napoleon: "Para Para Para" ')

print("Sena: \"Para Para Para.\"")
# escape characters
# / forward slask
# \ backward slash

# def myFunc(a, b, min=True) -> min is optional
# \n -> alt satıra inmek için kullanılır

print(name, surname)

print(name, surname, sep="|") # aralara | ekler

print(name, end = "") # alt satırı yanına getirir.
print(surname)


print("zahide\nsena\nkurtak") #satırları ayırmaya yarar.
print("\tzahide\nsena\nkurtak") # \t->tab ekler 

print(r"\tzahide\nsena\nkurtak") # r-> raw stringe çevirir, özel karakterlerin hiçbiri bulunmaz.

name = "sena"
age = 27

info = "{} is {} years old".format(name, age)

print(info)
print("{0} is {1} years old".format(name, age))
print("{1} is {0} years old".format(age, name))

# + operattörü -> concatenation str+str

print(name+" is "+str(age)+" years old.")

result = ""
result = result + name
result = result + " is "
result += str(age)
result += "years old..."
print(result)