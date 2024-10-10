#!/usr/bin/env python3

import sys
import time

def make_jar():
    ''' 

    Function to read in input from CSV files 
    NOTE: We will assume that it is a valid input for the CSV files
    
    Format of CSV file:
    {Value Coin 0},...,{Value Coin N - 1},{Value Coin N},{Target Value}
    EXIT

    Output: {target value}, {coins list}

    '''
    content = sys.stdin.read() # Get contents of CSV
    raw = [int(x) for x in content.split(',')] # Make contents into int list for processing
    raw_target = len(raw) - 1 # Get position of target in list
    return raw[raw_target], raw[:raw_target] # Return {target value}, {coins list}

def solve(solution: list[int], total: int, remaining: int, index: int, target: int, coins: list[int]) -> list[int]:
    '''
    
    Solver that employs backtracking and DFS to find combinations that will equal to target

    Input:
        solution:       list[int] (comprised only of 0s and 1s - 0 means not included, 1 means included)
        total:          int
        remaining:      int
        index:          int
        target:         int
        coins           list[int] (comprised of all coins in jar)

    Output:
        list[int]:      This will be list of ints where the sum is equal to the target, or None if no combination is found

    '''
    if total == target: # Base Case: Total equals target value --> Combination has been found
        return solution
    if total > target or not remaining: # Base Case: total exceeds target value or no more numbers remaining
        return None
    

    remaining -= coins[index] # Subtract 

    # Recursive Call - Include next number in next iteration
    solution_include = solution[:] # Copy current iteration
    solution_include.append(coins[index]) # Append next number to create next iteration
    include = solve(solution_include, total + coins[index], remaining, index + 1, target, coins) # Recursive Call
    if include: # If recursive call finds solution, return the solution
        return include

    # Recursive Call - Don't include next number in next iteration
    exclude = solve(solution, total, remaining, index + 1, target, coins) # Recursive Call
    return exclude # Return regardless if there is one - if there isn't, then None will be returned


def main():
    # Read in CSV file and initialize TARGET and COINS
    target, coins = make_jar()
    # Initializing other variables
    print("Target: {}".format(target))
    print("Coins: {}".format(coins))
    
    # Get start time --> start of the knapsack solver
    start_time = time.time()
    # Call recursive function solve
    solution = solve([], 0, sum(coins), 0, target, coins) # Will output combination if valid, None if no combination valid
    if solution: # If solution is found, print combination
        print("Solution found: {}".format(', '.join([str(x) for x in solution])))
    else: # Else print "Solution not found."
        print("Solution not found.")
    
    # Print Execution Time --> knapsack solver stops
    print("--- Total Execution Time: {:.2f} seconds ---".format(time.time() - start_time))

if __name__ == '__main__':
    main()