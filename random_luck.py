#!/usr/bin/env python3
import random
from typing import Dict
from collections import defaultdict


def random_choice(options: Dict[str, int]) -> str:
    population = []
    weights = []
    for key, value in options.items():
        population.append(key)
        weights.append(value)

    return random.choices(population, weights=weights)[0]


def dist_debug(draw_count: int, options: Dict[str, int]):
    distribution = defaultdict(int)
    print(f"Drawing {draw_count}...")
    for i in range(draw_count):
        decision = random_choice(options)
        distribution[decision] += 1
        print(f"{decision}, ", end='')
    print()
    print("---------")
    from pprint import pprint
    pprint(dict(distribution))


fuzzy_ops = {
    "No": 28,
    "1": 2,
    "2": 2
}

challenge_ops = {
    "Nothing": 20,
    "Spacer": 7,
    "Dziennik": 7,
    "Art": 5,
}


if __name__ == "__main__":
    fuzzy = random_choice(fuzzy_ops)
    print(f"F: {fuzzy}")
    #dist_debug(31, fuzzy_ops)

    challenge = random_choice(challenge_ops)
    print(f"C: {challenge}")
    #dist_debug(31, challenge_ops)

