import sys

sys.setrecursionlimit(1500)


def is_palindromic(num: int) -> bool:
    str_num = str(num)
    l = len(str_num)
    for i in range(l // 2):
        if str_num[i] != str_num[l - 1 - i]:
            return False
    return True


def get_biggest_palindrome(num: int) -> int:
    # returns the largest palindrome which can be subtracted from num
    # e.g. 539 -> 535
    # e.g. 835 -> 828
    str_num = str(num)
    middle_index = len(str_num) // 2

    # If the number is a palindrome then just return it
    if is_palindromic(num):
        return num

    # If the number is 1000... then return 999...
    # It's a bit disgusting but it works ig
    if str_num[0] == "1" and str_num[1:] == "".join(["0" for _ in str_num[1:]]):
        return int("".join("9" for _ in str_num[1:]))

    # If there are an odd number of digits
    if len(str_num) % 2 == 1:
        # If you can just flip the left side of the number
        # E.g. 15278 -> 15251
        if int(str_num[:middle_index]) <= int(str_num[middle_index + 1 :][::-1]):
            return int(
                str_num[:middle_index]
                + str_num[middle_index]
                + str_num[:middle_index][::-1]
            )

        # If we have to do some extra maths before we can flip it
        # E.g. 15231 -> 15199 -> 15151
        num -= int(str_num[middle_index + 1 :]) + 1
        str_num = str(num)
        return int(
            str_num[:middle_index]
            + str_num[middle_index]
            + str_num[:middle_index][::-1]
        )

    # Now we are left with if we have an even number of digits
    # Just like above, this part is if you can just flip the left side of the number
    if int(str_num[:middle_index] + str_num[:middle_index][::-1]) <= num:
        return int(str_num[:middle_index] + str_num[:middle_index][::-1])

    # If we have to do some extra maths before we can flip it
    num -= int(str_num[middle_index:]) + 1
    str_num = str(num)
    return int(str_num[:middle_index] + str_num[:middle_index][::-1])


def gather_solutions(
    true_num: int,
    current_num: int = -1,
    best_so_far: tuple[int, int, int] = (9999999, 9999999, 9999999),
) -> tuple[int, int, int]:
    # This is a _really_ unoptimised recursive function which essentially tests out all palindromic
    # numbers between true_num and 1 / 3 of true_num and sees what solutions exist for it
    # btw, I define a 'solution' as a group of three palindromic numbers that add to make true_num

    # If current_num is -1 then it was unset, I want to set it initially to true_num
    if current_num == -1:
        current_num = true_num
    # The base-case of the recursive algorithm
    if current_num <= 1 / 3 * true_num:
        pair = get_biggest_palindrome_pair(best_so_far[0] + best_so_far[1])
        return (best_so_far[2], pair[0], pair[1])

    # getting all of the solutions for our current number
    sol1 = get_biggest_palindrome(current_num)
    rem1 = true_num - sol1
    sol2 = get_biggest_palindrome(rem1)
    sol3 = rem1 - sol2

    # If our last solution, sol3, isn't palindromic then it isn't really a solution
    if not is_palindromic(sol3):
        return gather_solutions(true_num, sol1 - 1, best_so_far)

    solutions = (sol1, sol2, sol3)

    # Just to quote the question paper:
    # "If there are several possible palindromic sums you should output the one containing
    # the lowest palindromic number. If there are still several solutions remaining you
    # should select the one containing the highest palindromic number."
    if min(solutions) < min(best_so_far):
        return gather_solutions(true_num, sol1 - 1, solutions)
    if min(solutions) == min(best_so_far) and max(solutions) > max(best_so_far):
        return gather_solutions(true_num, sol1 - 1, solutions)
    return gather_solutions(true_num, sol1 - 1, best_so_far)


def get_biggest_palindrome_pair(num: int) -> tuple[int, int]:
    difference = 123
    current = num
    while True:
        result = get_biggest_palindrome(current)
        difference = num - result

        if is_palindromic(difference):
            return (difference, result)
        else:
            current = result - 1


def main() -> None:
    n = int(input())

    if is_palindromic(n):
        print(n)
        return

    solutions = gather_solutions(n)
    for s in solutions:
        if s != 0:
            print(s, end=" ")
    print()


if __name__ == "__main__":
    main()
