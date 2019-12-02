import argparse


def analyze_int_code(input_file, val1=12, val2=2):
    if not input_file.endswith(".txt"):
        raise NameError(f"{input_file} is not a .txt file.")

    int_codes = None

    with open(input_file) as f:
        int_codes = [int(digit) for line in f for digit in line.split(",")]
        int_codes[1] = val1
        int_codes[2] = val2

    if int_codes:
        for i in range(0, len(int_codes), 4):
            if int_codes[i] == 1:
                int_codes[int_codes[i+3]] = int_codes[int_codes[i+1]] \
                                            + int_codes[int_codes[i+2]]
            elif int_codes[i] == 2:
                int_codes[int_codes[i+3]] = int_codes[int_codes[i+1]] \
                                            * int_codes[int_codes[i+2]]
            elif int_codes[i] == 99:
                break
            else:
                print(int_codes[i])
    else:
        raise NameError(f"File could not be read.")
    return int_codes[0]


def noun_verb_pair(input_file):
    for i in range(0, 100):
        for j in range(0, 100):
            if analyze_int_code(input_file, i, j) == 19690720:
                return i, j


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_file", help="Input file for module masses."
    )
    args = parser.parse_args()
    input_file = args.input_file

    result = analyze_int_code(input_file)
    print(f"Part 1: Result is {result}.")

    noun, verb = noun_verb_pair(input_file)
    print(f"Part 2: Result is noun = {noun}, verb = {verb}.")
    print(f"Part 2: 100 * noun + verb = {100 * noun + verb}.")
