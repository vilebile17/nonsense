import time, random


def main():
    num_rounds = 5

    print("======== Welcome! ========")
    print(
        f"In this game you will be required to square {num_rounds} numbers between 13 and 99"
    )
    print(
        "We will record your times for each problem (in seconds) and then return all of the results to you."
    )
    print("Let's see how well you do!\n")

    # We have two lists, one for every single result and one for just the times of the correct answers
    score_list = []
    time_list = []

    for i in range(1, num_rounds + 1):
        num = random.randint(13, 99)
        input("Press enter when ready... ")
        start = time.time()

        # This part ensures that the user input is indeed a number
        while True:
            try:
                user_answer = int(input(f"{i}) {num}^2 = "))
                break
            except Exception as _:
                print("That doesn't appear to be an integer bro...")

        end = time.time()
        total_time = end - start

        # Dealing with whether or not the user is correct
        if user_answer == num**2:
            score_list.append(round(total_time, 2))
            time_list.append(round(total_time, 2))
            print("Nice answer!\n")
        else:
            score_list.append("DNF")
            print(f"Uh oh, the answer is actually {num**2}\n")

    print(f"Nice work bozo, your results were {score_list}")
    if len(time_list) != 0:
        print(
            f"Meaning that your mean time was {round(sum(time_list) / len(time_list), 2)} seconds"
        )
    else:
        print("Oof, you didn't get any right. Better luck next time!")


main()
