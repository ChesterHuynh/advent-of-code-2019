import argparse


def computeManhattanDistance(pt1):
    x1, y1 = pt1
    return abs(x1) + abs(y1)


def extract_endpoints(path):
    x, y = 0, 0
    posns = []
    posns.append((x, y))
    for step in path:
        direction = step[0]
        distance = int(step[1:])
        if direction == "L":
            x -= distance
        elif direction == "R":
            x += distance
        elif direction == "D":
            y -= distance
        elif direction == "U":
            y += distance
        posns.append((x, y))
    return posns


def closest_intersection(input_file):
    if not input_file.endswith(".txt"):
        raise NameError(f"{input_file} is not a .txt file.")

    wire_paths = None

    with open(input_file) as f:
        wire_paths = [path.strip().split(",") for path in f.readlines()]

    if not wire_paths:
        raise NameError(f"File could not be read.")

    path1 = wire_paths[0]
    path2 = wire_paths[1]
    posns1 = extract_endpoints(path1)
    posns2 = extract_endpoints(path2)
    intxns = []

    # Compute intersections with each combination of pairs of points for each
    # of the two paths.
    # Used: https://www.wikiwand.com/en/Line%E2%80%93line_intersection
    for i in range(len(posns1)-1):

        (x1, y1), (x2, y2) = posns1[i], posns1[i+1]

        for j in range(len(posns2)-1):

            (x3, y3), (x4, y4) = posns2[j], posns2[j+1]
            denom = (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))

            if denom:
                intxn_x = ((x1*y2 - y1*x2) * (x3-x4) - (x1 - x2) * (x3*y4 - y3*x4)) / denom
                intxn_y = ((x1*y2 - y1*x2) * (y3-y4) - (y1 - y2) * (x3*y4 - y3*x4)) / denom
                if (
                    (
                        not (intxn_x == intxn_y == 0)
                    )
                    and
                    (
                        (
                            y1 == y2
                            and x1 != x2
                            and y3 != y4
                            and x3 == x4
                            and intxn_x > min([x1, x2])
                            and intxn_x < max([x1, x2])
                            and intxn_y > min([y3, y4])
                            and intxn_y < max([y3, y4])
                        )
                        or
                        (
                            y1 != y2
                            and x1 == x2
                            and y3 == y4
                            and x3 != x4
                            and intxn_x > min([x3, x4])
                            and intxn_x < max([x3, x4])
                            and intxn_y > min([y1, y2])
                            and intxn_y < max([y1, y2])
                        )
                    )
                ):
                    intxns.append((intxn_x, intxn_y))

    return int(min(list(map(computeManhattanDistance, intxns))))


def fewest_steps_intersection(input_file):
    if not input_file.endswith(".txt"):
        raise NameError(f"{input_file} is not a .txt file.")

    wire_paths = None

    with open(input_file) as f:
        wire_paths = [path.strip().split(",") for path in f.readlines()]

    if not wire_paths:
        raise NameError(f"File could not be read.")

    path1 = wire_paths[0]
    path2 = wire_paths[1]
    posns1 = extract_endpoints(path1)
    posns2 = extract_endpoints(path2)
    intxns = []

    # Compute intersections with each combination of pairs of points for each
    # of the two paths.
    # Used: https://www.wikiwand.com/en/Line%E2%80%93line_intersection
    numsteps1 = 0
    for i in range(len(posns1)-1):
        (x1, y1), (x2, y2) = posns1[i], posns1[i+1]
        numsteps2 = 0

        for j in range(len(posns2)-1):
            (x3, y3), (x4, y4) = posns2[j], posns2[j+1]

            denom = (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))
            if denom:
                intxn_x = ((x1*y2 - y1*x2) * (x3-x4) - (x1 - x2) * (x3*y4 - y3*x4)) / denom
                intxn_y = ((x1*y2 - y1*x2) * (y3-y4) - (y1 - y2) * (x3*y4 - y3*x4)) / denom
                if (
                    (
                        not (intxn_x == intxn_y == 0)
                    )
                    and
                    (
                        (
                            y1 == y2
                            and x1 != x2
                            and y3 != y4
                            and x3 == x4
                            and intxn_x > min([x1, x2])
                            and intxn_x < max([x1, x2])
                            and intxn_y > min([y3, y4])
                            and intxn_y < max([y3, y4])
                        )
                        or
                        (
                            y1 != y2
                            and x1 == x2
                            and y3 == y4
                            and x3 != x4
                            and intxn_x > min([x3, x4])
                            and intxn_x < max([x3, x4])
                            and intxn_y > min([y1, y2])
                            and intxn_y < max([y1, y2])
                        )
                    )
                ):
                    total_steps = numsteps1 \
                                    + abs(intxn_x - x1) \
                                    + abs(intxn_x - x3) \
                                    + numsteps2 \
                                    + abs(intxn_y - y1) \
                                    + abs(intxn_y - y3)
                    intxns.append((total_steps, (intxn_x, intxn_y)))
            numsteps2 += max([abs(x4-x3), abs(y4-y3)])
        numsteps1 += max([abs(x2-x1), abs(y2-y1)])

    intxns.sort(key=lambda x: x[0])
    return int(intxns[0][0])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "input_file", help="Input file for module masses."
    )
    args = parser.parse_args()
    input_file = args.input_file

    min_dist = closest_intersection(input_file)
    print(f"Part 1: Min Manhattance distance: {min_dist}.")

    fewest_steps = fewest_steps_intersection(input_file)
    print(f"Part 2: Fewest combined steps: {fewest_steps}.")
