import csv
import sys
import docker_management as dm
from storage import Storage


def read_csv(filename, delimiter):
    matrix = []

    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=delimiter)
        for row in reader:
            matrix.append(row)

    return matrix


if __name__ == '__main__':

    filename = 'credentials.csv'
    keypair = 'keypair.pem'

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if len(sys.argv) > 2:
            keypair = sys.argv[2]

    credentials = read_csv(filename, ',')

    access_key = credentials[1][1]
    secret_key = credentials[1][2]

    Storage(access_key, secret_key).deploy()
    dm.deploy(keypair, access_key, secret_key)
