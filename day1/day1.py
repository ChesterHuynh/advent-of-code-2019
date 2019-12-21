import argparse


def compute_fuel_req(input_file):
    if not input_file.endswith(".txt"):
        raise NameError(f"{input_file} is not a .txt file.")

    fuel_req = 0
    with open(input_file) as f:
        for l in f:
            mass = int(l.strip())
            fuel_req += (mass // 3) - 2
    return fuel_req


def compute_fuel_req2(input_file):
    if not input_file.endswith(".txt"):
        raise NameError(f"{input_file} is not a .txt file.")

    total = 0
    with open(input_file) as f:
        for l in f:
            mass = int(l.strip())
            added_fuel = (mass // 3) - 2
            while added_fuel > 0:
                total += added_fuel
                added_fuel = (added_fuel // 3) - 2
    return total


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_file", help="Input file for module masses."
    )
    args = parser.parse_args()
    input_file = args.input_file

    fuel_req = compute_fuel_req(input_file)
    print(f"Part 1: fuel requirement is {fuel_req}.")

    fuel_req2 = compute_fuel_req2(input_file)
    print(f"Part 2: fuel requirement is {fuel_req2}.")
