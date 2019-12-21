import argparse


def run_diagnostic(input_file, input_val):
    if not input_file.endswith(".txt"):
        raise NameError(f"{input_file} is not a .txt file.")

    int_codes = None

    with open(input_file) as f:
        int_codes = [digit.strip() for line in f for digit in line.split(",")]

    if int_codes:
        i = 0
        while i < len(int_codes):
            opcode = int_codes[i]
            if int(opcode) == 99:
                break
            elif int(opcode) == 3:
                int_codes[int(int_codes[i+1])] = input_val
                i += 2
            elif int(opcode) == 4:
                output = int_codes[int(int_codes[i+1])]
                print(f"Output: {output}")
                i += 2
            else:
                if len(opcode) == 1:
                    addr1 = int(int_codes[i+1])
                    addr2 = int(int_codes[i+2])
                    addr3 = int(int_codes[i+3])
                    if int(opcode) == 1:
                        int_codes[addr3] = str(int(int_codes[addr1]) + int(int_codes[addr2]))
                    elif int(opcode) == 2:
                        int_codes[addr3] = str(int(int_codes[addr1]) * int(int_codes[addr2]))
                    i += 4
                else:
                    while len(opcode) < 5:
                        # Pad zeros
                        opcode = "0" + opcode
                    op = int(opcode[3:])
                    mode1 = int(opcode[2])
                    mode2 = int(opcode[1])
                    mode3 = int(opcode[0])
                    addr1 = i+1 if mode1 else int(int_codes[i+1])
                    addr2 = i+2 if mode2 else int(int_codes[i+2])
                    addr3 = i+3 if mode3 else int(int_codes[i+3])
                    if op == 1:
                        int_codes[addr3] = str(int(int_codes[addr1]) + int(int_codes[addr2]))
                    elif op == 2:
                        int_codes[addr3] = str(int(int_codes[addr1]) * int(int_codes[addr2]))
                    i += 4
    else:
        raise NameError(f"File {input_file} could not be read.")


def run_diagnostic2(input_file, input_val):
    if not input_file.endswith(".txt"):
        raise NameError(f"{input_file} is not a .txt file.")

    int_codes = None

    with open(input_file) as f:
        int_codes = [digit.strip() for line in f for digit in line.split(",")]

    if int_codes:
        i = 0
        while i < len(int_codes):
            opcode = int_codes[i]
            if int(opcode) == 99:
                break
            elif int(opcode) == 3:
                int_codes[int(int_codes[i+1])] = input_val
                i += 2
            elif int(opcode) == 4:
                output = int_codes[int(int_codes[i+1])]
                print(f"Output: {output}")
                i += 2
            else:
                if len(opcode) == 1:
                    op = int(opcode)
                    if op in [1, 2, 7, 8]:
                        addr1 = int(int_codes[i+1])
                        addr2 = int(int_codes[i+2])
                        addr3 = int(int_codes[i+3])
                        if op == 1:
                            int_codes[addr3] = str(int(int_codes[addr1]) + int(int_codes[addr2]))
                        elif op == 2:
                            int_codes[addr3] = str(int(int_codes[addr1]) * int(int_codes[addr2]))
                        elif op == 7:
                            int_codes[addr3] = str(1) \
                                if int(int_codes[addr1]) < int(int_codes[addr2]) else str(0)
                        elif op == 8:
                            int_codes[addr3] = str(1) \
                                if int(int_codes[addr1]) == int(int_codes[addr2]) else str(0)
                        i += 4
                    elif op in [5, 6]:
                        addr1 = int(int_codes[i+1])
                        addr2 = int(int_codes[i+2])
                        if op == 5:
                            if int_codes[addr1] != "0":
                                i = int(int_codes[addr2])
                            else:
                                i += 3
                        elif op == 6:
                            if int_codes[addr1] == "0":
                                i = int(int_codes[addr2])
                            else:
                                i += 3
                else:
                    if int(opcode[-2:]) in [1, 2, 7, 8]:
                        while len(opcode) < 5:
                            # Pad zeros
                            opcode = "0" + opcode
                        op = int(opcode[3:])
                        mode1 = int(opcode[2])
                        mode2 = int(opcode[1])
                        mode3 = int(opcode[0])
                        addr1 = i+1 if mode1 else int(int_codes[i+1])
                        addr2 = i+2 if mode2 else int(int_codes[i+2])
                        addr3 = i+3 if mode3 else int(int_codes[i+3])
                        if op == 1:
                            int_codes[addr3] = str(int(int_codes[addr1]) + int(int_codes[addr2]))
                        elif op == 2:
                            int_codes[addr3] = str(int(int_codes[addr1]) * int(int_codes[addr2]))
                        elif op == 7:
                            int_codes[addr3] = str(1) \
                                if int(int_codes[addr1]) < int(int_codes[addr2]) else str(0)
                        elif op == 8:
                            int_codes[addr3] = str(1) \
                                if int(int_codes[addr1]) == int(int_codes[addr2]) else str(0)
                        i += 4
                    elif int(opcode[-2:]) in [5, 6]:
                        while len(opcode) < 4:
                            # Pad zeros
                            opcode = "0" + opcode
                        op = int(opcode[2:])
                        mode1 = int(opcode[1])
                        mode2 = int(opcode[0])
                        addr1 = i+1 if mode1 else int(int_codes[i+1])
                        addr2 = i+2 if mode2 else int(int_codes[i+2])
                        if op == 5:
                            if int_codes[addr1] != "0":
                                i = int(int_codes[addr2])
                            else:
                                i += 3
                        elif op == 6:
                            if int_codes[addr1] == "0":
                                i = int(int_codes[addr2])
                            else:
                                i += 3
    else:
        raise NameError(f"File {input_file} could not be read.")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_file", help="Input file for opcodes."
    )

    args = parser.parse_args()
    input_file = args.input_file
    input_val1 = 1
    print("-------------------- Part One --------------------")
    run_diagnostic(input_file, input_val1)
    print("Diagnostic code is last line of above output.\n")

    input_val2 = 5
    print("-------------------- Part Two --------------------")
    run_diagnostic2(input_file, input_val2)
    print("Diagnostic code is last line of above output.")
