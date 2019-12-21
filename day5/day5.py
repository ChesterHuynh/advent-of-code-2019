import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_file", help="Input file for module masses."
    )

    args = parser.parse_args()
    input_file = args.input_file
    print(input_file)
