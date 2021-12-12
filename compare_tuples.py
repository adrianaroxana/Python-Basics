def compare_tuples(tuple1, tuple2):
    return sorted(tuple1) == sorted(tuple2)


print(compare_tuples((1, 2, 3), (3, 1, 2)))
print(compare_tuples((5, 8, 7), (10, 2, 3)))

