# This script accepts some arguments passed from the command line
import numpy as np
import argparse

def main(num1, num2):
    return num1 + num2

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-num1', type=float)
    parser.add_argument('-num2', type=float)

    args = parser.parse_args()

    result = main(args.num1, args.num2)
    print(result)
