import sys
from storage import Storage
import yaml

if __name__ == '__main__':

    filename = 'credentials.yml'
    keypair = 'keypair.pem'

    if len(sys.argv) <= 1:
        print('You must specify a S3 bucket name')
    else:
        bucketname = sys.argv[1]
        if len(sys.argv) > 2:
            filename = sys.argv[1]
        else:
            filename = 'credentials.yml'

    with open(filename) as file:
        credentials = yaml.load(file)

    Storage(bucketname, credentials['id'], credentials['key']).deploy()
