''' 
a = 5
b = 3
c = a + b

print(c)

# a + b = c mümkün değil
print(a,b)

a = 100
b = a + 3*(b+1)
print(a,b)
'''

# Değişkenlerin farklı tipleri olabilir week 2 konusu olacak

# Değişken oluşturma kuralları

# 1.Değişken sayı ile başlayamaz

a = 5 
a1 = 10
# 1a = 10 yanlış


# 2.Büyük harf kullanılabilir.

# 3.Türkçe karakter kullanılmaz

# 4. Sembol kullanılmaz. _ ve - hariç

 
'''current_year = 2023
birth_year = 1996
age = current_year - birth_year
print("You are", age, "years old.")
'''

# Kullanıcıdan almak istediğiniz bilgileri alabilirsiniz

current_year = 2023
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year
print("You are", age, "years old.")

# bu python gramer kurallarına aykırı! Stringle Integer ı işleme sokmaya çabalıyoruz.