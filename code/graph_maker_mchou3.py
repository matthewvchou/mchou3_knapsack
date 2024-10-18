#!/usr/bin/env python3

'''

Matthew Chou - mchou3
October 18th, 2024
Theory of Computing Project 01

graph_maker_mchou3.py: creates graphs for results in csv files

'''

# Imports
import sys
import csv
import matplotlib.pyplot as plt
import numpy as np

def get_results(filename: str, num_cases: int):
    ''' 
    Function to read in input from CSV files line by line
    Format of CSV file line:
    'Testcase', 'Target', 'Coins', 'Solution', 'Execution Time (seconds)'

    Output: Yields {target value}, {coins list} for each line in the CSV
    '''
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        temp_list = []
        count_list = []
        count = 1
        for index, row in enumerate(reader):
            if index == 0:
                continue
            if count > num_cases:
                yield count_list, temp_list
                count = 1
                temp_list = []
                count_list = []
            temp_list.append(float(row[-1]))
            count_list.append(count)
            count += 1
        yield count_list, temp_list


# Main function to handle CSV creation
def main():
    # Check if a filename is passed as argument
    if len(sys.argv) < 2:
        print("Usage: python3 graph_maker_mchou3.py <input.csv> <output.csv>")
        sys.exit(1)

    # Read in CSV file and initialize TARGET and COINS for each line
    filename = sys.argv[1]
    
    # Initialize plot
    my_plot = plt.figure(figsize=(10,10))
    plt.title("Time vs. Number of Coins (Failures - Worst Case)")
    plt.xlabel("Number of Coins")
    plt.ylabel("Time (Seconds)")


    # Initializing variables for drawing
    color = ['green', 'yellow', 'red']
    names = ['Small Value Coins', 'Medium Value Coins', 'Large Value Coins']
    markers = ['o', 's', '^']
    i = 0

    # Drawing graph
    for counts, times in get_results(filename, 32): # NOTE: will have to change manually the number of test cases
        #mean = np.mean(times)
        #stddev = np.std(times)
        #plt.ylim(mean - 2 * stddev, mean + 2 * stddev)
        plt.plot(counts, times, label=names[i], color=color[i], marker=markers[i], linestyle='None')
        i += 1

    # Showing legend and grid
    plt.legend()
    plt.grid()

    # Save to file and close
    plt.savefig(sys.argv[2])
    plt.close()



if __name__ == "__main__":
    main()