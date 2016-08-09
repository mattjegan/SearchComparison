
from binarysearch import binary_search
from datetime import datetime
from random import choice, randint, random
from gallopingsearch import galloping_search

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_style("darkgrid")

def main():

    rows = []

    b_total = 0
    g_total = 0

    b_total_compars = 0
    g_total_compars = 0

    num_tests = 50
    num_items = 1000

    print("Test | Num_items | Binary Time |     | Galloping Time |     |")

    for test in range(0, num_tests):
        
        array = [randint(0, num_items) for item in range(0, num_items)]
        array.sort()
        
        # Best Case (Non-Trivial)
        #target = array[10]

        # Worst Case
        #target = array[-10]

        # Average Case
        target = choice(array)

        # Run the binary search
        b_start = datetime.now()
        b = binary_search(array, target)
        b_subtotal = (datetime.now() - b_start).microseconds
        b_total += b_subtotal
        b_compars = b[1]
        b_total_compars += b_compars

        # Run the galloping search
        g_start = datetime.now()
        g = galloping_search(array, target)
        g_subtotal = (datetime.now() - g_start).microseconds
        g_total += g_subtotal
        g_compars = g[1]
        g_total_compars += g_compars

        print("{:4} | {:9} | {:11} | {:3} | {:14} | {:3} |".format(test, num_items, b_subtotal, b_compars, g_subtotal, g_compars))

        rows.append([num_items, b_compars, 'Binary Search'])
        rows.append([num_items, g_compars, 'Galloping Search'])

        num_items += 1000

    print("Binary Search Average: {}".format(b_total // num_tests))
    print("Galloping Search Average: {}".format(g_total // num_tests))

    print("Binary Search Comparisons Average: {}".format(b_total_compars // num_tests))
    print("Galloping Search Comparisons Average: {}".format(g_total_compars // num_tests))

    df = pd.DataFrame(rows, columns=('N', 'C', 'Class'))
    g = sns.lmplot(x='N', y='C', ci=0, hue='Class', data=df, logx=True, size=5)
    g.savefig('out.png')
    

if __name__ == '__main__': main()