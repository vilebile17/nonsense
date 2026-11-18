def main():
    n = int(input("n: "))
    # In these tuples, the first number is the column and the
    # second number is the row, as the question puts it
    alpha_coords: list[tuple[int, ...]] = []
    beta_coords: list[tuple[int, ...]] = []

    # Gets the inputs for the coordinates of Alpha and Beta spies
    # and puts them in two lists of tuple[int, int]
    for i in range(1, n + 1):
        alpha_input = input(f"alpha {i}: ").strip().split(" ")
        alpha_coords.append(tuple(int(val) for val in alpha_input))
    for i in range(1, n + 1):
        beta_input = input(f"beta {i}: ").strip().split(" ")
        beta_coords.append(tuple(int(val) for val in beta_input))

    # This is after the spies have left the grid, so the spy complexes
    # have switched
    alpha_coords_by_column = sorted(beta_coords, key=lambda x: x[0])
    beta_coords_by_column = sorted(alpha_coords, key=lambda x: x[0])
    alpha_coords_by_row = sorted(beta_coords, key=lambda x: x[1])
    beta_coords_by_row = sorted(alpha_coords, key=lambda x: x[1])

    resulting_row_labels = [-1 for _ in range(n)]
    resulting_column_labels = [-1 for _ in range(n)]

    last_visited_column = 0
    for _ in range(n):
        new_alpha = alpha_coords_by_column[last_visited_column]
        old_alpha = beta_coords_by_column[last_visited_column]
        resulting_row_labels[new_alpha[1]] = old_alpha[1]

        last_visited_row = new_alpha[1]

        new_beta = beta_coords_by_row[last_visited_row]
        old_beta = alpha_coords_by_row[last_visited_row]
        resulting_column_labels[new_beta[0]] = old_beta[0]

        last_visited_column = old_beta[0]

        print()
        print(resulting_column_labels)
        print(resulting_row_labels)


if __name__ == "__main__":
    main()
