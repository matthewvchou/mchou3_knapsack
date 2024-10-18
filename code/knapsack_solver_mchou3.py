#!/usr/bin/env python3

'''

Matthew Chou - mchou3
October 18th, 2024
Theory of Computing Project 01

knapsack_solver_mchou3.py: Solver for knapsack problem

'''

# Imports
import sys
import time
import csv

def make_jar(filename):
    ''' 
    Function to read in input from CSV files line by line
    Format of CSV file line:
    {Value Coin 0},...,{Value Coin N - 1},{Target Value}

    Output: Yields {target value}, {coins list} for each line in the CSV
    '''
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            # Convert the row from strings to integers
            raw = list(map(int, row))
            
            # The target is the last element, coins are the rest
            target = raw[-1]
            coins = raw[:-1]
            
            # Return the target value and the list of coins
            yield target, coins


def solve(solution: list[int], total: int, index: int, target: int, coins: list[int]) -> list[int]:
    '''
    
    Solver that employs backtracking and DFS to find combinations that will equal to target

    Input:
        solution:       list[int] (comprised only of 0s and 1s - 0 means not included, 1 means included)
        total:          int
        index:          int
        target:         int
        coins           list[int] (comprised of all coins in jar)

    Output:
        list[int]:      This will be list of ints where the sum is equal to the target, or None if no combination is found

    '''
    if total == target: # Base Case: Total equals target value --> Combination has been found
        return solution
    if total > target or index >= len(coins): # Base Case: total exceeds target value or no more numbers remaining
        return []

    # Recursive Call - Include next number in next iteration
    solution_include = solution[:] # Copy current iteration
    solution_include.append(coins[index]) # Append next number to create next iteration
    include = solve(solution_include, total + coins[index], index + 1, target, coins) # Recursive Call
    if include: # If recursive call finds solution, return the solution
        return include

    # Recursive Call - Don't include next number in next iteration
    exclude = solve(solution, total, index + 1, target, coins) # Recursive Call
    return exclude # Return regardless if there is one - if there isn't, then None will be returned


def main():
    # Check if a filenames are passed as argument
    if len(sys.argv) < 3:
        print("Usage: python3 knapsack_solver_mchou3.py <input.csv> <output.csv>")
        sys.exit(1)

    # Read in CSV file and initialize TARGET and COINS for each line
    filename = sys.argv[1]

    # Open the output CSV file for writing
    with open(sys.argv[2], mode='w', newline='') as output_file:
        writer = csv.writer(output_file)
        
        # Write the header for the output CSV
        writer.writerow(['Testcase', 'Target', 'Coins', 'Solution', 'Execution Time (seconds)'])

        count = 1
        for target, coins in make_jar(filename):
            # Get start time --> start of the knapsack solver
            start_time = time.time()
            
            # Call recursive function solve
            # solve(solution: list, total: int, index: int, target: int, coins: list[int]) -> list[int]:
            solution = solve([], 0, 0, target, coins) # Will output combination if valid, None if no combination valid
            
            # Calculate execution time
            exec_time = time.time() - start_time
            
            # Write the results for this testcase
            if solution:
                writer.writerow([target, coins, solution, "{:f}".format(exec_time)])
            else:
                writer.writerow([target, coins, solution, "{:f}".format(exec_time)])
            
            print("Run {:f} Done -- Execution Time: {:.9f}".format(count, exec_time))
            count += 1


if __name__ == '__main__':
    main()