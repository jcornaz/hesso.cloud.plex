from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

CONTAINER_NAME = "plex_container"


class Storage(object):
    def __init__(self, username, password):
        self._driver = get_driver(Provider.S3)(username, password)

    def deploy(self):
        self._container = self._driver.get_container(CONTAINER_NAME)
        if not self._container:
            self._container = self._driver.create_container(CONTAINER_NAME)

    def destroy(self):
        if not self._container:
            self._container = self._driver.get_container()

        if self._container:
            self._driver.delete_container(self._container)
