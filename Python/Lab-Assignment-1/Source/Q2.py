# Function to Reverse the words
def R_Word(s):
    # Spliting the given Sentence into list of words by using the space
    words = s.split(" ")
    # Reversing each word and creating a new list of words
    k = [word[::-1] for word in words]
    o = " ".join(k)
    return o

# Function to find the largest word
def L_word(s):
    p = s.split()
    p.sort(key=len, reverse=True)
    return p[0]

# Function to find the middle word
def M_Word(s):
    d =s.split(" ")
    print(d)
    if len(d) % 2 == 0:
        return d[int(len(d) / 2)], d[int(len(d) / 2 - 1)]
    else:
        return d[int(len(d) // 2)]

# Take input from the user
s = input("Enter a String: ")

# Function Calls
print("Reverse:",R_Word(s))
print("Largest Word:",L_word(s))
print("Middle Word:",M_Word(s))



