
print("You are Typing in test02.txt now :")
lines = 0
a = []
words = 0
while True:
    
    user = input()
    if user.strip().lower() == "done":
        break
    a.append(user)
    with open("test02.txt", "w") as f:
        for i in a :
            f.writelines(f"{i}\n")
    words += len(user.split())
    lines += 1
print (f"Lines : {lines}")
print(a)
with open("test02.txt", "r") as f:
    f_in = f.read()
print(f_in)
print(f"Words : {words}")
input()
