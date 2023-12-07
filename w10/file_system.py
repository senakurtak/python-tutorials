# işletim sisteminde tüm dosyalar dizin adı verilen hiyerarşide saklanır. bu yapıda başlangıç noktası vardı-> kök
# linux -> Kök -> C:\ -> \ köktür. her işletim sisteminin belli dosyaları nasıl depoladığıyla alakalı yaklaşımları var.

# /Users/senakurtak/Repo/python-tutorials/w9/file_system.py -> absolute path // tam adres, her zaman çalışır
# senakurtak@Sena-MacBook-Air python-tutorials % -> relative path
import sys,os 
# system, operation system kütüphaneleri import edilir
# pythonda shell komutlarını karşılayan komutlar var
#for line in sys.path:
#    print(line) # pathteki her absolute pathi verir
    
#print(os.getcwd()) # bulunduğun directory pathini verir
# os.chdir("/Users/senakurtak/Repo/")
# print(os.getcwd())

# cwd -> current working directory

#os.makedirs("cak") # cak isimli bir klasör oluşturur

#print(os.path.abspath("file_system.py")) # file_system.py isimli file ın nerede olduğunu gösterir absolute path

#iteratif olarak olmadığı dosyanın yerini de bulmaz. burada böyle bir dosya olsa path i ne olurdu?

#print(os.path.abspath("file_system.py")) # file_system.py isimli file ın nerede olduğunu gösterir relative path

#print(os.path.abspath("cak//selam.txt"))
#print(os.path.relpath("cak//selam.txt"))


#print(os.path.dirname(pt))
#print(os.path.basename(pt))

#if not os.path.exists("week10\\cak\\selam.txt"):
#    print("not found")
#else:
#    print("found")
    
if not os.path.exists("week10\\cak\\selam.txt"):
    print( "Not found")
else:
    print("Found")

pt = "week10\ \cak\ Iselammy. txt"

if os.path.isfile(pt):
    print("It is a file")
elif os.path.isdir(pt):
    print("It is a directory")
    

'''
. curren directory
.. parent directory
'''

for tup in os.walk("."): # bulunduğum dizin demeye çalışıyorum
    print(tup)