"""
with open("test01.txt", "w") as f:
    f.write(input("Write something in the txt file :\n"))

with open("test01.txt", "r") as f:
    f_in = f.read() 
    print(f_in)
"""


print("you are typing in 'test01.txt' file :")
while True :
    user = input()
    if user.strip().lower() == "done":
       break
    with open("test01.txt","a") as f:
        f.writelines(f"{user}\n")
print("boy")

"""
print("You are typing in 'test01.txt' file :")
while True:
    user = input()
    if user.replace("\r", "").strip().lower() == "done":
        break
    with open("test01.txt", "a") as f:
        f.writelines(f"{user}\n")
print("boy")
"""