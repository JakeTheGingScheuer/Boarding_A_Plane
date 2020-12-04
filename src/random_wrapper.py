import random


class RandomWrapper:
    @staticmethod
    def random_number(max_value):
        return random.randint(0, max_value-1)
