jadval = []
print("Jadval zarb!")
user = int(input("from 0 to what ? "))
for i in range (1,user+1) :
    x= []
    for a in range(1,11):
        c = i * a
        x.append(f"{i}*{a} = {c}")
    jadval.append(x)
    

for jad in jadval :
    print(jad)