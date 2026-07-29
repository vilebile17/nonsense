def is_palindrome(n: int) -> bool:
    # I tried my best to make it as unreadable as possible
    return False not in list(map(lambda x: str(n)[x] == str(n)[len(str(n)) - x - 1],[i for i in range(len(str(n)) // 2)],))

def main():
    for test in [121, 120, 66, 1991, 1]:
        print(f"Is the number {test} a palindrome? The answer is: {is_palindrome(test)}!")

main()
