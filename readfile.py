def read_graph(filename):
    file = open(filename, "r")
    matrix = file.readlines()  # read in whole file as 1D list of strings
    for row in range(len(matrix)):
        # strip off trailing newline and break each row into a list, creating a 2D list
        matrix[row] = list(matrix[row].strip().split(" "))

        for col in range(len(matrix[row])):
            # convert each '0' into 0 and '1' into 1 so have numerical matrix instead of character one
                matrix[row][col] = int(matrix[row][col])
    return matrix[2:-1]


def read_number_of_node(filename):
    file = open(filename, "r")
    number = file.readlines()
    return number[0]

def read_node(filename):
    file = open(filename, "r")
    start = file.readlines()
    for row in range(len(start)):
        # strip off trailing newline and break each row into a list, creating a 2D list
        start[row] = list(start[row].strip().split(" "))

        for col in range(len(start[row])):
            # convert each '0' into 0 and '1' into 1 so have numerical start instead of character one
                start[row][col] = int(start[row][col])

    return start[1]