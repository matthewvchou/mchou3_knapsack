#!/usr/bin/env python3

import sys
import time

def make_jar() -> dict:
    ''' 
    Function to read in input from CSV files 
    NOTE: We will assume that it is a valid input for the CSV files
    
    Format of CSV file:
    {Value Coin 0},...,{Value Coin N - 1},{Value Coin N},{Target Value}
    EXIT

    Output:
    dict{
        target: int
        coins: list[int]
        }
    
    '''
    content = sys.stdin.read() # Get contents of CSV
    raw = [int(x) for x in content.split(',')] # Make contents into int list for processing
    raw_target = len(raw) - 1 # Get position of target in list
    # Make "jar" --> Holds target value and all coins in jar
    jar = {
        'target':   raw[raw_target],
        'coins':    raw[:raw_target]
    }
    return jar # Return "jar"

def solve(jar: list[int], target: int, previous: set[list[int]]) -> bool:


def main():
    # Read in CSV file and make "jar"
    jar = make_jar()
    print(jar)
    
    # Get start time --> start of the knapsack solver
    start_time = time.time()
    # TODO: KNAPSACK SOLVER CODE GOES HERE
    # Print Execution Time --> knapsack solver stops
    print("--- Total Execution Time: {:.2f} seconds ---".format(time.time() - start_time))

if __name__ == '__main__':
    main()