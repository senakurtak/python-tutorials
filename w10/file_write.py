'''
r: read
w: write (dosyayı her zaman sıfırdan oluşturur)
a: append (olan dosyaya ekler)
b: byte (resim gibi dosyalar için byte modunda) # byte like moduna çeviriyoruz.
t: text (text modunda)
'''

''''
fp = open("results", "a") # çalışma dizinimize (python-tutorials içine) oluşturdu
fp.write("Sena")
fp.write("Şeyma")
fp.write("Denizcan")
fp.close()
'''

data = ["cihan", "merve", "manat"] 

fp = open("results.txt", "w")
fp.writelines(data) # satırı dosyaya yazmamıza olanak sağlar
fp.close()