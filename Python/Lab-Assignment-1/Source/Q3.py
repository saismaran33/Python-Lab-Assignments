# func is a function to print the triplets
def func(a, n):
    # found is just a random variable
    found =False
    for i in range(0, n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):
                # checking if the sum is 0 or not
                if (a[i] + a[j] + a[k] == 0):
                    print( a[i], a[j], a[k])
                    found = True

    if (found == False):
        print(" No Triplets are found in the given list")

# Taking input from the user
a = [int(x) for x in input().split()]
print(a)
# Finding the length of list
n = len(a)
# Function call with list "a" and length of the list "n" as the arguments
func(a, n)