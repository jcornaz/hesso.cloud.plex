from libcloud.storage.types import Provider, ContainerDoesNotExistError
from libcloud.storage.providers import get_driver

CONTAINER_NAME = "plex_container"


class Storage(object):
    def __init__(self, access_key, secret_key):
        self._driver = get_driver(Provider.S3)(access_key, secret_key)
        self._container = None

    def deploy(self):
        if self._container is None:
            try:
                self._container = self._driver.get_container(CONTAINER_NAME)
            except ContainerDoesNotExistError:
                self._container = self._driver.create_container(CONTAINER_NAME)

        print("container deployed")

    def destroy(self):
        if self._container is None:
            try:
                self._container = self._driver.get_container(CONTAINER_NAME)
            except ContainerDoesNotExistError:
                self._container = None

        if self._container is not None:
            self._driver.delete_container(self._container)
