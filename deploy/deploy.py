import sys
import docker_management as dm
from storage import Storage
import yaml

if __name__ == '__main__':

    filename = 'credentials.yml'
    keypair = 'keypair.pem'

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if len(sys.argv) > 2:
            keypair = sys.argv[2]

    with open(filename) as file:
        credentials = yaml.load(file)

    Storage(credentials['id'], credentials['key']).deploy()
    dm.deploy(keypair, credentials['id'], credentials['key'])
