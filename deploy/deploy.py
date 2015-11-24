import csv
import sys
from storage import Storage


def read_csv(filename, delimiter):
    matrix = []

    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=delimiter)
        for row in reader:
            matrix.append(row)

    return matrix


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'credentials.csv'

    credentials = read_csv(filename, ',')

    Storage(credentials[1][1], credentials[1][2]).deploy()
