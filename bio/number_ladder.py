digits_to_letters: dict[str, str] = {
        "0": "ZERO",
        "1": "ONE",
        "2": "TWO",
        "3": "THREE",
        "4": "FOUR",
        "5": "FIVE",
        "6": "SIX",
        "7": "SEVEN",
        "8": "EIGHT",
        "9": "NINE"
}

def num_to_letters(num: str) -> str:
        return "".join([digits_to_letters[digit] for digit in num])

def can_be_transformed(num1: str, num2: str) -> bool:
        matches = 0
        og_num2_len = len(num2)

        # This loop goes through every char in num1 and matches it to the same char
        # in num2 (if it exists) to create a kind of venn-diagram; the matches variable
        # stores the number of letters in num1 which have a corresponding char in num2
        for char1 in num1:
                i = 0
                while i < len(num2):
                        if char1 == num2[i]:
                                matches += 1
                                num2 = num2[:i] + num2[i + 1:]
                                break
                        else:
                                i += 1

        # This finds the number of un-matched letters by taking the combined total
        # number of letters and subtracting double the amount of matches (since
        # there are two instances of that letter, one in each number)
        return (len(num1) + og_num2_len) - 2 * matches <= 5

def get_direct_transformations(num: str) -> list[str]:
        possible_nums = [num_to_letters(str(n)) for n in range(1,1000)]
        return list(filter(lambda n: can_be_transformed(num, n), possible_nums))

def main() -> None:
        inp1 = input("").split(" ")

        num1let = num_to_letters(inp1[0])
        num2let = num_to_letters(inp1[1])

        nums_to_check = get_direct_transformations(num1let)
        already_seen = set()
        i = 1
        while True:
                new_nums_to_check = []
                for num in nums_to_check:
                        if num in already_seen:
                                continue
                        if num == num2let:
                                print(i)
                                return

                        already_seen.add(num)
                        new_nums_to_check.extend(
                                filter(lambda x: x not in already_seen, get_direct_transformations(num))
                        )
                nums_to_check = new_nums_to_check
                i += 1

if __name__ == "__main__":
        main()
