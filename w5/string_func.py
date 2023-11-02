surname = "kurtak"

bigname = surname.upper()

print(bigname)

surname.title() # ilk harfi büyütür

new_name = surname[0].upper() + surname[1:-1] + surname[-1].upper()

print(new_name)

number = "66"


if number.isdigit():
    print(int(number))
else:
    print("rakam disinda karakterler var")

# büyük küçük harf duyarlılığı var 'A' arasaydık false dönerdi.
if "a" in surname:
    print("a içerir")

if 'e' in surname:
    print("e içerir")
    
    
msg = "  c@nim$    "
print(msg)
msg = msg.replace("@", "a")
print(msg)
msg = msg.replace("$","")
print(msg)
msg = msg.strip() # lstrip, rstrip
print(msg)

name = "sena"
a = name*3
print(a)

##********!!!!

n = 5
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")
    
##********!!!!
n = 5 
for i in range(n):
    print("*"*(i+1))
    
# split join -> listeler dersinde anlatılacak