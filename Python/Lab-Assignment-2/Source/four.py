
import numpy as np # importing numpy library and referring it as np
x = np.random.randint(0, 20, 15) # This is a built-in function which generates random 15 integers from 1-20 numbers
print("Given List:")
print(x)
print("Most frequent value in the List:")
print(np.bincount(x).argmax()) #Using a built-in function