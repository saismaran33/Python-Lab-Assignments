# List of Students enrolled in Python class
l1 = ['abc', 'def', 'jkl', 'xyz', 'orm']
# List of students enrolled in Web Development class
l2 = ['bcd', 'abc', 'orm', 'Sam', 'Ben', 'jenny', 'jkl']

print("Students enrolled in both Python and Web Developement classes are:")
for i in l1:
    if i in l2:
        print(i,"\n")


print("Students enrolled in either of web development or python are: \n")

# Checking the names that are present in List 1 but not in List 2
for j in l1:
    if j not in l2:
        print(j,"\n")

# Checking the names that are present in List 2 but not in List 1
for k in l2:
    if k not in l1:
        print(k,"\n")
