#indexing
surname = "kurtak"
print(surname[0]+surname[2]+surname[3]+surname[5])

# başka yazılım dillerine surname[2]= "h" yapamazsın çünkü python immutable

# slicing 
print(surname[1:4])

message = "longmessage"
print(message[:3]) #0 1 2
print(message[7:])
print(message)
print(message[-5:-2]) # negative indexing
print(message[::2])
print(message[3::3]) # index 3ten başla, 3 er atla

chess_row = "| |r| |N| | | | |"
