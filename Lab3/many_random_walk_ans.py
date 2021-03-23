import numpy as np


def random_walks(walks_count):
    walks = []
    number_of_steps = 1500
    for i in range(walks_count):
        draws = np.random.randint(0, 2, size=number_of_steps)
        steps = np.where(draws > 0, 1, -1)
        walk = steps.cumsum()
        walks.append(walk)
    return walks


def find_min_position_in_walks(walks):
    min_positions = []
    for walk in walks:
        min_positions.append(walk.min())
    return np.array(min_positions).min()


def find_max_position_in_walks(walks):
    max_positions = []
    for walk in walks:
        max_positions.append(walk.max())
    return np.array(max_positions).max()


def find_minimum_transition_time(walks, threshold):
    min_jump_over_threshold = []
    for walk in walks:
        jump = (np.abs(walk) >= threshold).argmax()
        min_jump_over_threshold.append(jump if jump > 0 else np.Inf)
    return np.array(min_jump_over_threshold).min()


def main():
    walks_count = 5000
    transition_value = 30
    walks = random_walks(walks_count)
    min_transition_time = find_minimum_transition_time(walks, transition_value)
    max_walk = find_max_position_in_walks(walks)
    min_walk = find_min_position_in_walks(walks)
    print("max walk = ", max_walk)
    print("min walk = ", min_walk)
    print("min transition time to get over than {0} = {1}".format(transition_value, min_transition_time))


main()
