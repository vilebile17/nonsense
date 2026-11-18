def get_direct_equivalents(num: str, d: int) -> list[str]:
    # takes a serial number and finds the numbers that are directly equivalent to it
    if d == 1:
        return []

    result = []

    # loops through every adjacent pair of digits
    for i in range(d - 1):
        digit1 = int(num[i])
        digit2 = int(num[i + 1])

        # Defining the digits to the left and right of our pair, if one doesn't exist on
        # one of the sides then the value at that side is set to -1 which happens to
        # work nicely with our checks coming up
        digit_to_left = -1
        digit_to_right = -1
        if i >= 1:
            digit_to_left = int(num[i - 1])
        if i + 2 < d:
            digit_to_right = int(num[i + 2])

        # If digit_to_left is between digit1 and digit2 OR if digit_to_right is between
        # digit1 and digit2
        if (digit1 < digit_to_left < digit2 or digit2 < digit_to_left < digit1) or (
            digit1 < digit_to_right < digit2 or digit2 < digit_to_right < digit1
        ):
            # Swap the digits around and leave the rest of the number unchanged
            result.append(num[:i] + num[i + 1] + num[i] + num[i + 2 :])

    return result


def main():
    d = int(input("d -> "))
    num = input("num -> ")

    # I think this method is called 'Breadth-First-Search'
    # We've got a list of numbers we'd like to test and we add to the list any
    # new numbers that we find, given that it's not in the already_found set.
    nums_to_check = [num]
    already_found = set(nums_to_check)
    iteration_count = 0
    while len(nums_to_check) > 0:
        newly_found_numbers = []

        for n in nums_to_check:
            equivalents = get_direct_equivalents(n, d)

            for eq in equivalents:
                if eq in already_found:
                    continue
                newly_found_numbers.append(eq)
                already_found.add(eq)

        iteration_count += 1
        nums_to_check = newly_found_numbers

    # We need to subtract one because we do a full loop without any changes
    # before the loop breaks
    print(iteration_count - 1)


if __name__ == "__main__":
    main()
