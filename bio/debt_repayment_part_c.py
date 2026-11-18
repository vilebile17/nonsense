from math import ceil


def round_up(num: float) -> float:
    # takes a number and rounds it up to two decimal places
    return ceil(num * 100) / 100


def main() -> None:
    # takes the inputs and stores them as a decimal rather than a percentage

    results = {}
    for interest in range(101):
        for repayment in range(101):
            print(f"{interest},{repayment}")
            balance = 100
            total_money = 0
            iterations = 0

            while balance > 0 and iterations < 10000:
                # add interest
                try:
                    interest_to_add = round_up(interest * balance)
                except:
                    break
                balance += interest_to_add

                # repay interest
                try:
                    amount_repaid = max(50, round_up(repayment * balance))
                except:
                    break
                balance -= amount_repaid
                total_money += (
                    amount_repaid if balance >= 0 else amount_repaid + balance
                )

                iterations += 1

            if balance <= 0:
                results[(interest, repayment)] = total_money

    print(results)


if __name__ == "__main__":
    main()
