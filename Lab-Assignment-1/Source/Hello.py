p=input("Enter your password: ")
n=len(p)
a=0
if n>6:
    if n<16:
        a=1
    else:
        print("length should be 6-16 characters")
else:
    print("Length should 6-16 characters")
q=0
for c in p:
    if c.isdigit():
        q=1
        break
if q==0:
    print("Should have atleast one number")
b=0
while b==0:
    if '$' in p:
        b=1
        break
    elif '@' in p:
        b=1
        break
    elif '!' in p:
        b=1
        break
    elif '*' in p:
        b=1
        break
    else:
        print("Should have atleast one special character")
        break
r=0
for c in p:
    if c.islower():
        r=1
        break
if r==0:
    print("Should have atleast one lowercase")
s=0
for c in p:
    if c.isupper():
        s=1
        break
if s==0:
    print("Should have atleast  one uppercase")

if s==1 and r==1 and a==1 and b==1 and q==1:
    print("\n Your Password satisfies all the conditions")
else:
    print("\n Try other password please")