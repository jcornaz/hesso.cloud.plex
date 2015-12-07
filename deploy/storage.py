from libcloud.storage.types import Provider, ContainerDoesNotExistError
from libcloud.storage.providers import get_driver

class Storage(object):
    def __init__(self, bucketname, access_key, secret_key):
        self._bucketname = bucketname
        self._driver = get_driver(Provider.S3)(access_key, secret_key)
        self._container = None

    def deploy(self):
        print("deploy storage...")

        if self._container is None:
            try:
                self._container = self._driver.get_container(self._bucketname)
            except ContainerDoesNotExistError:
                self._container = self._driver.create_container(self._bucketname)

        print("storage up")

    def destroy(self):
        if self._container is None:
            try:
                self._container = self._driver.get_container(self._bucketname)
            except ContainerDoesNotExistError:
                self._container = None

        if self._container is not None:
            self._driver.delete_container(self._container)
