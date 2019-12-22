import argparse


def max_thruster_signals(input_file="input.txt"):
    if not input_file.endswith(".txt"):
        raise NameError(f"{input_file} is not a .txt file.")

    max_signal = 0

    intcodes = None

    with open(input_file) as f:
        intcodes = [code.strip() for line in f for code in line.split(",")]

    if intcodes:
        # TODO:
        pass

    else:
        raise NameError(f"File {input_file} could not be read.")

    return max_signal


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Input file for opcode.")

    args = parser.parse_args()
    input_file = args.input_file

    print(max_thruster_signals(input_file))
