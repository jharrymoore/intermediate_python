import argparse


def main(base, exponent, verbosity):
    if verbosity == 1:
        print("Calculating...")
    elif verbosity == 2:
        print(f"Calculating exponent {exponent} of base {base}")
    return base ** exponent


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--base', type=float, help='The First Number', default=5)
    parser.add_argument('-e', '--exponent', type=float, help='The Second Number', default=5)
    parser.add_argument('-v', '--verbosity', help='Set the execution verbosity', default=0, action='count')

    args = parser.parse_args()

    result = main(args.base, args.exponent, args.verbosity)
    print(result)
