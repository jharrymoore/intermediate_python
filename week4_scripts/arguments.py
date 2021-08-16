#This script uses sys.argv to collect the arguments passed from the command line and work with them
import sys

def main():
    print(sys.argv)
    a = sys.argv[2]
    print(a)

    print(sys.argv[1] + sys.argv[2])

if __name__ == '__main__':
    main()