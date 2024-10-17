#!/usr/bin/env python3



# Imports
import csv
import argparse
import random

# Function to generate a random test case (modify as needed)
def generate_test_case():
    # Generate list of random coins - for general purposes, we will keep 

    # Example: a test case with random integers
    return [random.randint(1, 100) for _ in range(5)]

# Main function to handle CSV creation
def main():
    # Setting up argument parser
    parser = argparse.ArgumentParser(description="Generate a CSV file with random test cases.")
    parser.add_argument('-s', '--size', type=int, default=5, help="Number of test cases to generate")
    parser.add_argument('-f', '--file', type=str, default='test.csv', help="Name of file to save to")

    # Parse arguments
    args = parser.parse_args()

    # Open the file and write the test cases as CSV
    with open(args.file, mode='w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Generate and write the specified number of test cases
        for _ in range(args.size):
            test_case = generate_test_case()
            csvwriter.writerow(test_case)
    
    print(f"Generated {args.size} test cases and saved to {args.file}")

if __name__ == "__main__":
    main()
