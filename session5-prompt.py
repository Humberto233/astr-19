import math
import numpy as np
from math import pi, sin

def sin_table(start, stop, entry):
    table = []
    value = (stop - start) / (entry - 1)

    for i in range(entry):
        x = start + i * value
        sinx = math.sin(x)
        table.append((x, sinx))
    
    return table

def print_sin_table(table):
    print(f"{'x':>10} {'sin(x)':>15}") 
    print("-" * 25)
    
    for x, value in table:
        print(f"{x:10.5f} {value:15.10f}")


def main():
    start = 0
    stop = 2*np.pi    
    entry = 1000

    filled_table = sin_table(start, stop, entry)
    
    print_sin_table(filled_table)

if __name__=="__main__":
    main()