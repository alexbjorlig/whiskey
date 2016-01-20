with open('Scotch data/' + 'Scotch (109x68)') as input_file:
    next(input_file)  # To skip the first line
    for whiskey in input_file:
        whiskey_cleaned = whiskey.replace(" ", "").strip()  # Remove spaces between characters, and '\n'
        whiskey_tuple_string = tuple(whiskey_cleaned)  # Convert the line to tuple string

        whiskey_tuple_integer = tuple([int(x) for x in whiskey_tuple_string])  # x is a single attribute either 1 or 0
