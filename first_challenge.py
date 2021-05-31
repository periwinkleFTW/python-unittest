"""
Coding challenge #1
This counter function purpose is tho count how many english letters does your contain.py
After writing your tests, develop the counter function as needed to pass all your tests.
"""


def counter(name):

    if name is None:
        raise Exception('You cannot input None values')

    name = name.replace(' ', '')
    if len(name) == 0:
        raise Exception('Please input your name')

    if name.isalpha():
        return len(name)
    else:
        raise Exception('The string must contain only letters')
