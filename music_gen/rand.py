from typing import Dict, Any
import random


def rand(possibility: Dict[Any, float], accuracy: float):
    rand_list = []
    for key, value in possibility.items():
        rand_list.extend([key] * int(value / accuracy))
    return random.choice(rand_list)


def choice(values):
    return random.choice(values)
