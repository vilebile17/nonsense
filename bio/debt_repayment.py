from math import ceil


def round_up(num: float) -> float:
    # takes a number and rounds it up to two decimal places
    return ceil(num * 100) / 100


def main() -> None:
    # takes the inputs and stores them as a decimal rather than a percentage
    interest = int(input()) / 100
    repayment = int(input()) / 100
    balance = 100
    total_money = 0

    while balance > 0:
        # add interest
        interest_to_add = round_up(interest * balance)
        balance += interest_to_add

        # repay interest
        amount_repaid = max(50, round_up(repayment * balance))
        balance -= amount_repaid
        total_money += amount_repaid if balance >= 0 else amount_repaid + balance

    print(round(total_money, 2))


if __name__ == "__main__":
    main()
