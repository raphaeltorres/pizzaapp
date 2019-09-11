import random
import string


R_GEN = random.SystemRandom()


def generate_pizza_id(name, timestamp):
    return '{name}-{hr}{min:02d}{sec:02d}{r}'.format(
        name=name.upper(),
        hr=string.ascii_uppercase[timestamp.hour],
        min=timestamp.minute,
        sec=timestamp.second,
        r=''.join(R_GEN.sample(string.ascii_uppercase, 3))
    )
