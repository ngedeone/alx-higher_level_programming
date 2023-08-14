#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Pad the tuples with zeros if they have less than 2 elements
    padded_tuple_a = tuple_a + (0, 0)[:2 - len(tuple_a)]
    padded_tuple_b = tuple_b + (0, 0)[:2 - len(tuple_b)]

    # Add corresponding elements and create a new tuple
    result = (
        padded_tuple_a[0] + padded_tuple_b[0],
        padded_tuple_a[1] + padded_tuple_b[1]
    )
    return result
