import argparse


def count_passwords(input_range):
    lo, hi = input_range.split("-")
    lo, hi = int(lo), int(hi)
    count = 0
    for num in range(lo, hi+1):
        double_exists = False
        never_decreases = True
        prev = 10
        while num:
            num, digit = divmod(num, 10)
            if digit == prev:
                double_exists = True
            if digit > prev:
                never_decreases = False
            prev = digit
        if double_exists and never_decreases:
            count += 1
    return count


def count_strictly_double_passwords(input_range):
    lo, hi = list(map(int, input_range.split("-")))
    count = 0
    for num in range(lo, hi+1):
        double_exists = False
        never_decreases = True
        prev = 10
        num_repeats = 1
        while num:
            num, digit = divmod(num, 10)
            if digit == prev:
                num_repeats += 1
            elif num_repeats == 2:
                double_exists = True
                num_repeats = 1
            else:
                num_repeats = 1

            if digit > prev:
                never_decreases = False

            prev = digit

        # Check case where two leftmost digits are the double
        if num_repeats == 2:
            double_exists = True

        if double_exists and never_decreases:
            count += 1
    return count


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "input_range", help="Puzzle input range."
    )
    args = parser.parse_args()
    input_range = args.input_range

    num_passwords = count_passwords(input_range)
    print(f"Part 1: Num diff passwords in {input_range}: {num_passwords}.")

    num_passwords2 = count_strictly_double_passwords(input_range)
    print(f"Part 2: Num diff passwords in {input_range}: {num_passwords2}.")
