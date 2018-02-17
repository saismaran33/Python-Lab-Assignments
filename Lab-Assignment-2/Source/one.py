# Disctionary
umkc = {
    "Python":50,
    "Web":30,
    "C":20,
    "Java":40
}

print("All the available books in the UMKC store are:")

for index in umkc.items():
   print(index)

a=int(input("Enter the minimum value of the range: "))
b=int(input("Enter the maximum value of the range: "))

x=dict((k, v) for k, v in umkc.items() if v >= a and v<=b) # (k,v) ordered pair indicates the key-value pair from the dictionary
# We are comparing the value in the dictionary with the given minimum and maximum values

for index,val in umkc.items():
   print("You can buy",index)
