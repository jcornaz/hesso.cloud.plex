import sys
import yaml
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from storage import Storage
from plexservers import PlexMediaServer, FileUploaderServer

if __name__ == '__main__':

    if len(sys.argv) > 1:
        config_filename = sys.argv[1]
    else:
        config_filename = 'config.yaml'

    with open(config_filename) as file:
        config = yaml.load(file)

    if config:
        driver = get_driver(Provider.EC2_EU_WEST)(config['access']['id'], config['access']['key'])

        Storage(config['bucket_name'], config['access']['id'], config['access']['key']).deploy()

        plex_server = PlexMediaServer(
            driver,
            't2.micro',
            config['access']['ssh_key'],
            config['elastic_ips']['plex'],
            config['bucket_name'],
            config['access']['id'],
            config['access']['key']
        )

        webserver = FileUploaderServer(
            driver,
            't2.micro',
            config['access']['ssh_key'],
            config['elastic_ips']['file_uploader']
        )

        plex_server.run(webserver)
        webserver.run(plex_server)
