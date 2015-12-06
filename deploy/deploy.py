import sys
import yaml
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from storage import Storage
from plexservers import PlexMediaServer, FileUploaderServer

if __name__ == '__main__':

    filename = 'credentials.yml'
    keypair = 'keypair.pem'

    if len(sys.argv) <= 1:
        print('You must specify a S3 bucket name')
    else:
        bucketname = sys.argv[1]
        if len(sys.argv) > 2:
            filename = sys.argv[2]
            if len(sys.argv) > 3:
                keypair = sys.argv[3]

    with open(filename) as file:
        credentials = yaml.load(file)

    driver = get_driver(Provider.EC2_EU_WEST)(credentials['id'], credentials['key'])

    Storage(bucketname, credentials['id'], credentials['key']).deploy()
    plex_server = PlexMediaServer(driver, 'c2.micro', keypair, bucketname)
    webserver = FileUploaderServer(driver, 'c2.micro', keypair)

    plex_server.run(webserver)
    webserver.run(plex_server)
