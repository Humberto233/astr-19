import numpy as np
import sys

# define the function to add the exponent
def f(x):
    return x**3 + 8

# creating the main function now
def main():
    print(f(9)) #calling the function

    # checking if the result is larger than 27
    if f(9) >= 27: 
        print("Yay!")
    
    else: 
        return

if __name__=="__main__":
    main()