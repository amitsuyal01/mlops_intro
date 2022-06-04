# creating a function to add two numbers
import argparse


def my_add(x, y):
    return x + y


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Simple function to add two numbers")
    parser.add_argument("first", type=int, help="First number")
    parser.add_argument("second", type=int, help="Second number")

    args = parser.parse_args()

    # print (my_add(3,4))
    adding = my_add(args.first, args.second)
    print(f"the sum of {args.first} and {args.second} is {adding}")
