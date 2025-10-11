jadval = []

for i in range (1,11) :
    x= []
    for a in range(1,11):
        c = i * a
        x.append(f"{i}*{a} = {c}")
    jadval.append(x)
    

for jad in jadval :
    print(jad)