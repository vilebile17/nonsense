# 2023 BIO round 1 q2
from typing import Self


class Pentominoe:
    # This defines a class for each pentominoe. It essentially holds the coords
    # of all of the points squares it contains and has some methods for manipulating
    # said coords
    def __init__(self, coords: list[tuple[int, int]]) -> None:
        self.coords = list(coords)

    def move(self, x: int, y: int) -> None:
        result: list[tuple[int, int]] = []
        for coord in self.coords:
            result.append((coord[0] + x, coord[1] + y))
        self.coords = result

    def get_distance(self, other: Self) -> float:
        # Cool cases for this method:
        # if the distance is 0 then the two shapes overlap;
        # if the distance is 1 then they are edge-to-edge.
        # I decided to add a weird case where the shapes are at an angle
        # to return distance = 1.5

        min_so_far = 99999
        for c1 in self.coords:
            for c2 in other.coords:
                distance = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
                if abs(c1[0] - c2[0]) == 1 and abs(c1[1] - c2[1]) == 1:
                    distance = 1.5
                min_so_far = min(min_so_far, distance)
        return min_so_far

    def add_coords(self, other: Self) -> list[tuple[int, int]]:
        # combines the coords of two pentominoes and returns it as a list
        return self.coords + other.coords

    def __str__(self) -> str:
        return " ".join([f"({c[0]}, {c[1]})" for c in self.coords])


def contains_negatives(coords: list[tuple[int, int]], index: int) -> bool:
    # if the list of coords contains a negative value; this is used towards
    # the end of the main function
    for coord in coords:
        if coord[index] < 0:
            return True
    return False


def mass_shift_coords(
    coords: list[tuple[int, int]], x: int, y: int
) -> list[tuple[int, int]]:
    # moves all of the coords by the vector (x,y); this is also used towards
    # the end of the main function
    return [(c[0] + x, c[1] + y) for c in coords]


# Just the hardcoded values from the question
shape_dic = {
    "F": [(1, 0), (2, 0), (0, 1), (1, 1), (1, 2)],
    "G": [(0, 0), (1, 0), (1, 1), (2, 1), (1, 2)],
    "I": [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
    "L": [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3)],
    "J": [(1, 0), (1, 1), (1, 2), (1, 3), (0, 3)],
    "N": [(1, 0), (1, 1), (0, 1), (0, 2), (0, 3)],
    "M": [(0, 0), (0, 1), (1, 1), (1, 2), (1, 3)],
    "P": [(0, 0), (0, 1), (1, 1), (1, 0), (0, 2)],
    "Q": [(0, 0), (0, 1), (1, 1), (1, 0), (1, 2)],
    "T": [(0, 0), (1, 0), (2, 0), (1, 1), (1, 2)],
    "U": [(0, 0), (0, 1), (1, 1), (2, 1), (2, 0)],
    "V": [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
    "W": [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)],
    "X": [(1, 0), (1, 1), (0, 1), (1, 2), (2, 1)],
    "Z": [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)],
    "S": [(0, 2), (1, 2), (1, 1), (1, 0), (2, 0)],
    "Y": [(0, 1), (1, 1), (1, 0), (1, 2), (2, 3)],
    "A": [(0, 0), (0, 1), (1, 1), (0, 2), (0, 3)],
}


def main():
    inp = input("-> ").upper()
    letter1 = inp[0]
    letter2 = inp[1]

    shape1 = Pentominoe(shape_dic[letter1])
    shape2 = Pentominoe(shape_dic[letter2])
    combinations = []

    # shape2 starts inside of shape1, so we move it down until they're no longer overlapping
    while shape1.get_distance(shape2) == 0:
        shape2.move(0, 1)
    combinations.append(shape1.add_coords(shape2))

    last_move = (0, 1)
    next_move = (999, 999)
    og_shape_2 = shape2.coords

    # This is where the main magic happens, we walk shape2 around shape1 and if it's edge-to-edge
    # with it, then we add that to combinations
    while True:
        vectors_to_distances: dict[tuple[int, int], float] = {}

        # Testing out each of the possible movements to see what they yield
        for vector in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            shape2.move(vector[0], vector[1])
            vectors_to_distances[vector] = shape1.get_distance(shape2)
            shape2.move(-vector[0], -vector[1])

        # remove the path that we came from before
        del vectors_to_distances[(-last_move[0], -last_move[1])]

        # pick the best option: we want a distance of 1 ideally as that would mean that we have
        # got direct edge contact
        min_so_far = 999
        shortest_vector = (-last_move[0], -last_move[1])
        for vector, distance in vectors_to_distances.items():
            if distance < min_so_far and distance != 0:
                shortest_vector = vector
                min_so_far = distance
        next_move = shortest_vector

        # move the coord and if shape1 and shape2 are edge-to-edge then add it to combinations
        shape2.move(next_move[0], next_move[1])
        if min_so_far == 1:
            combinations.append(shape1.add_coords(shape2))
        last_move = next_move

        # if we have gone in a full loop where shape2 is back where it started then we break out of
        # the loop
        if shape2.coords == og_shape_2:
            break

    # This is bit I will call 'normalisation' although that's probably not very accurate.
    # I'm moving all of the squares in each individual combination of shape1 and shape2 along
    # such that none of their coords contain a negative value.
    # This is so that combinations which result in the same shape have the exact same set of
    # coordinates.
    results = []
    for comb in combinations:
        current = comb
        while contains_negatives(current, 0):
            current = mass_shift_coords(current, 1, 0)
        while contains_negatives(current, 1):
            current = mass_shift_coords(current, 0, 1)
        results.append(current)

    # Finally, collate a list of all of the unique combinations and print out the length of the
    # list. And that, is the number of distinguishable shapes that can be made out of letter1 and letter2
    already_seen = []
    for coords in [set(r) for r in results]:
        if coords in already_seen:
            continue
        already_seen.append(coords)
    print(len(already_seen))


if __name__ == "__main__":
    main()
