a = ["aa", "bb", "cc", "dd"]
print("{} is {} years old.".format("cihan", 30))
my_str = "".join(a)
print(my_str)
my_str = "*".join(a) # "" ile verilen arada yapıştırıcı görevi görür. Bu stringi ekleyerek birleştir
print(my_str)
data = "30,10,13,53,57,21"
data_list = data.split(",") # ne ile ayıracağını ver (",")/(",-")
print(data_list)

for i in range(len(data_list)): # pointer ile adreslenen yapılar için kolay, immutable değil
    data_list[i] = int(data_list[i])
print(data_list)
'''
# immutable ise 
a = []
for value in range(data_list):
    a.append(int(value))
    
data_list = a

ya da 
- list comphrension -> [int(v) for v in array]
'''

data_list = [int(v) for v in data_list] # int(v)-> ne append ettiğini gösterir
print(data_list)

my_list = [i+1 for i in range(10) if i<5]  
print(my_list)