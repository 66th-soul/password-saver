import random
title=open("title.txt")
pas=open("passwords.txt","a")
t=title.read()
print(t)

tab="______________________________________________________"

l=input("Login or site:  ")

answr=int(input("Auto-generate pass (1) / Write pass by hands (2):  "))
if answr==1:
    x = int(input("Pcs of symbols:  "))
elif answr==2:
    hand_passw=input("Enter pass:  ")
    x = 10
else:
    exit("Error. Invalid Value.")
    

if x < 0:
    z=8
elif x > 20:
    z=20
else:
    z=x

if answr==1:
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    passlen = z
    p =  "".join(random.sample(s,passlen ))
    pas.write("\n")
    pas.write(str(l))
    pas.write("\n")
    pas.write(str(p))
    pas.write("\n")
    pas.write(str(tab))
    pas.write("\n")
    
elif answr==2:
    pas.write("\n")
    pas.write(str(l))
    pas.write("\n")
    pas.write(str(hand_passw))
    pas.write("\n")
    pas.write(str(tab))
    pas.write("\n")

if answr==1:
    print("Your pass:",p)
    print("Writed succesfully")
else:
    print("Writed succesfully")

pas.close()
