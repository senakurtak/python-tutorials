# Dosya işlemleri
# dosya izinleri; yazma, okuma, açabilme vs. işletim sistemi kullanıcının açma yetisi var mı yok mu kontrol eder

#  student.txt core işletim sistemi için özel bir anlam ifade etmiyor, bize sunduğu ara yüzde anlam ifade ediyor. "".py olan dosyayı ... ile aç" kuralını uygulayabilir
# herhangi bir mod belirlemeden aç dersen okuma modunu açmaya çalışacak.

import os

fp = open("w10/student.txt") # fp üzerinden dosyaya erişebileceğim

#number = fp.read(9) # imleç 9 karakteri okuyacak (boşluk dahil)
#print(number)
#fp.read(1)
#name = fp.read(4)
#print(number, name)
# hangi boyutta okuma yapacağımızı kararlaştırıyoruz


'''
for i in range(4):
    line = fp.readline()[:-1]
    strs = line.split(" ")
    if len(strs)<=1: # error handler
        break
    number = strs[0]
    name = strs[1]
    grade = strs[2]
    print(number, name)

'''

'''
fp = open("w10/student.txt")
data = fp.readlines() # her satırı tek tek okuyarak listenin içine koyar
print(data)
for d in data:
    if d[-1]=='\n' :
        d = d[:-1]
    number, name, grade = d.split(" ") 
    print(name, number, grade)
fp.close()# açtığın dosyayı kapatman beklenir.
    '''
    
def averageFile(filePath):
    with open(filePath) as fp:
        data = fp.readlines() # her satırı tek tek okuyarak listenin içine koyar
        print(data)
        total = 0
        count = 0
        for d in data:
            if d[-1]=='\n' :
                d = d[:-1]
          #  number, name, grade = d.split(" ")  # üçünü tek yere atamaması için yazdık
            _, _, grade = d.split(" ")
            total += int(grade)
            count +=1
        return total/count

avg = averageFile("w10/student.txt")
print(avg)
