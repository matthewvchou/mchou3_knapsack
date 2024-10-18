#!/usr/bin/env python3

'''

Matthew Chou - mchou3
October 18th, 2024
Theory of Computing Project 01

testcase_generator_mchou3.py: custom testcase generator for knapsack problem

'''

# Imports
import csv
import argparse
from random import randint
from random import sample

# Function to generate a random test case (modify as needed)
def generate_test_case(value: str, num_coins: int, correct: int):
    '''
    
    Function to create a test case for the knapsack solver
    NOTE: For general purposes, we will keep coin sizes from 1-100

    Input:
      size:         str (Denoting range of coin sizes)
      num_coins:    int (Denoting number of coins within the jar)
      correct:      bool (True = provide correct target | False = provide unobtainable target)

    Output:
      test_case:    list[int] (last int represents target, rest of list represents coins in jar)
    
    '''
    # Look to see value of coins
    if value == 'small': # Generating small test case
      start = 1
      end = 99
    elif value == 'medium': # Generating medium test case
      start = 100
      end = 999
    else: # Generating large test case
      start = 1000
      end = 10000
    
    # Generate list of coins - can have repeats in list
    coins = [randint(start, end + 1) for _ in range(num_coins)]
    
    if correct:
      # Solvable target - sum of random subset within coins
      coins.append(sum(sample(coins, randint(0, len(coins)))))
    else:
      # Unsolvable target - sum of all coins + 1
      coins.append(sum(coins) + 1)

    return coins

# Main function to handle CSV creation
def main():
    # Setting up argument parser
    parser = argparse.ArgumentParser(description="Generate a CSV file with random test cases.")
    parser.add_argument('-n', '--number', type=int, default=5, help="Number of test cases to generate for each size: small, medium, and large")
    parser.add_argument('-s', '--size', type=int, default=10, help="Maximum size of jar/knapsack - maximum number of coins within jar")
    parser.add_argument('-f', '--file', type=str, default='test.csv', help="Name of file to save to")
    parser.add_argument('-c', '--correct', type=int, default=1, help="If the test cases should have a solution or not | 1+ means correct, 0 means incorrect")

    # Parse arguments
    args = parser.parse_args()

    # Open the file and write the test cases as CSV
    with open(args.file, mode='w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Generate and write the specified number of test cases for each size
        for size in ['small', 'medium', 'large']: # From smaller to larger numbers
            for _ in range(args.number): # Number of test cases to generate for each size
              for i in range(1,args.size + 1): #  From 1 to args.size number of coins in each jar
                test_case = generate_test_case(size, i, args.correct) # Generate test case
                csvwriter.writerow(test_case) # Write to CSV file
    
    print(f"Generated {args.number} test cases for each size and saved to {args.file}")

if __name__ == "__main__":
    main()