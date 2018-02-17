list = [{"name":'abc', "number":123, "email":"abc123@mail.umkc.edu"},
        {"name":"def", "number":345, "email":"def345@mail.umkc.edu"},
        {"name":"xyz","number":678,"email":"xyz678@mail.umkc.edu"}]

name = input("Enter name to get contact: ")
for i in list:
    if name in i.values():
        print(i)

num = int(input("Enter number to get contact: "))

for j in list:
# If condition for checking whether the entered number is in dictinary or not
    if num in j.values():
        print(j)

nme = input("Enter name to get contact and edit number: ")

for k in list:
# If the entered name in dictionary
    if nme in k.values():
        print(k)
        newnum = int(input("Enter number to edit: "))
        k["number"] = newnum
        print(k)