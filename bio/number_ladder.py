from time import time

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

all_nums_as_letters = [num_to_letters(str(n)) for n in range(1,1000)]

def can_be_transformed(num1: str, num2: str) -> bool:
        num1dic: dict[str, int] = {}
        for digit in num1:
                if digit not in num1dic:
                        num1dic[digit] = 1
                else:
                        num1dic[digit] += 1

        num2dic: dict[str, int] = {}
        for digit in num2:
                if digit not in num2dic:
                        num2dic[digit] = 1
                else:
                        num2dic[digit] += 1

        letters = set(num1).union(set(num2))
        differences = 0
        for letter in letters:
                if letter in num1dic and letter in num2dic:
                        differences += abs(num1dic[letter] - num2dic[letter])
                elif letter in num1dic:
                        differences += num1dic[letter]
                elif letter in num2dic:
                        differences += num2dic[letter]

        return differences <= 5

def get_direct_transformations(num: str) -> list[str]:
        return list(filter(lambda n: can_be_transformed(num, n), all_nums_as_letters))

def find_num_transformations(num1: str, num2: str, master_dic: dict[str, list[str]]) -> int:
        nums_to_check: set[str] = set()
        nums_to_check.add(num1)
        already_seen: set[str] = set()
        i = 0
        while True:
                new_nums_to_check: set[str] = set()
                for num in nums_to_check:
                        if num in already_seen:
                                continue
                        if num == num2:
                                return i

                        already_seen.add(num)
                        new_nums_to_check = new_nums_to_check.union(
                                filter(lambda x: x not in already_seen, master_dic[num])
                        )
                nums_to_check = new_nums_to_check
                i += 1

def main() -> None:
        inputs = [input("").split(" ") for _ in range(3)]

        begin = time()
        master_dic: dict[str, list[str]] = {}
        for num in all_nums_as_letters:
                master_dic[num] = get_direct_transformations(num)

        print(time() - begin)
        begin = time()

        for input_pair in inputs:
                num1 = num_to_letters(input_pair[0])
                num2 = num_to_letters(input_pair[1])
                print(find_num_transformations(num1, num2, master_dic))

if __name__ == "__main__":
        main()
