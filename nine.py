pifagor  = 10

for i in range(1, pifagor+1):
    print(" "," ", i, end=" ")
print("\n", " _"*20, end=" ")
for i in range(1, pifagor+1):
    print("\n",i, "|")
    for g in range(1, pifagor+1):
        print(" "*3,i*g, end=" ")