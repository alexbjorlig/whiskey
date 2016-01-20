import numpy


def calculate_euclidean_distance(a, b):
    """
    The purpose of this definition is to calculate the euclidean distance from two points.
    Please refer to Provost and Fawcett 146
    :param a:
    :param b:
    :return:
    """
    a_2 = numpy.array(a)
    b_2 = numpy.array(b)
    return numpy.linalg.norm(a_2-b_2)

random_whiskey = (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0)

with open('Scotch data/' + 'Scotch (109x68)') as input_file:
    next(input_file)  # To skip the first line
    for whiskey in input_file:
        whiskey_cleaned = whiskey.replace(" ", "").strip()  # Remove spaces between characters, and '\n'
        whiskey_tuple_string = tuple(whiskey_cleaned)  # Convert the line to tuple string

        whiskey_tuple_integer = tuple([int(x) for x in whiskey_tuple_string])  # x is a single attribute either 1 or 0
        print(calculate_euclidean_distance(random_whiskey, whiskey_tuple_integer))
