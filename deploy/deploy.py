import csv
import sys
import subprocess
from storage import Storage


def read_csv(filename, delimiter):
    matrix = []

    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=delimiter)
        for row in reader:
            matrix.append(row)

    return matrix


def deploy_containers(access_key, secret_key):
    subprocess.call(['./ecs-cli', 'configure',
                     '--region', 'eu-west-1',
                     '--cluster', 'plex_cluster',
                     '--access-key', access_key,
                     '--secret-key', secret_key
                     ])
    subprocess.call(['./ecs-cli', 'compose', 'up'])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'credentials.csv'

    credentials = read_csv(filename, ',')

    access_key = credentials[1][1]
    secret_key = credentials[1][2]

    Storage(access_key, secret_key).deploy()
    deploy_containers(access_key, secret_key)
