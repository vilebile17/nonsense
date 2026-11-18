def parse_stacks(state: str) -> tuple[str, ...]:
    # I initially thought that it would be easier to work with the stacks
    # if we parsed them into lists/tuples and replaced any 0s with ''
    # That is what this function does
    # E.g. '12 0 3 4' -> ('12', '', '3', '4')
    return tuple(["" if s == "0" else s for s in state.split(" ")])


def get_possible_states(stacks: tuple[str, ...]) -> list[tuple[str, ...]]:
    # Takes a state of stacks and returns all of the possible states
    # that can be made after a single move
    results: list[tuple[str, ...]] = []
    for i in range(len(stacks)):
        if not stacks[i]:
            # i.e. if the peg is empty then move on to the next one
            continue

        # This is the ball that we are moving around
        current_ball = stacks[i][-1]

        for j in range(len(stacks)):
            if i == j:
                # we don't want to move the ball to the same stack that
                # we started on
                continue

            # Before moving the ball to another peg, we need to create
            # a copy of the stacks as a list so that we can modify it
            current_stacks = list(stacks)
            current_stacks[i] = current_stacks[i][:-1]
            current_stacks[j] += current_ball
            results.append(tuple(current_stacks))

    return results


def main():
    initial_state = input("initial state -> ")
    final_state = input("final_state -> ")
    initial_stacks = parse_stacks(initial_state)
    goal = parse_stacks(final_state)

    if len(initial_stacks) != 4 or len(goal) != 4:
        print("There must be four stacks; no more, no less")
        return

    # BFS time :)
    stacks_to_check = [initial_stacks]
    already_found = {initial_stacks}
    iteration_count = 0

    while goal not in already_found:
        newly_found_states = []
        for stack in stacks_to_check:
            # Gets all of the possible moves in a position and then filters it for
            # the ones that we haven't found yet
            new_states = get_possible_states(stack)
            unfound_states = filter(lambda x: x not in already_found, new_states)

            # Adds the unfound_states to the newly_found_states list and the already_found set
            newly_found_states.extend(unfound_states)
            for state in newly_found_states:
                already_found.add(state)

        iteration_count += 1
        stacks_to_check = newly_found_states

    print(iteration_count)


if __name__ == "__main__":
    main()
