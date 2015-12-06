from cloudserver import Server
import time


class PlexMediaServer(Server):
    def __init__(self, driver, net, size, image_id, key_pair, webserver, bucket_name):
        super(PlexMediaServer, self).__init__(driver, net, size, image_id, key_pair)
        self._bucketname = bucket_name
        self._webserver = webserver
        self.is_ready = False

    @property
    def name(self):
        return 'PLEXMediaServer'

    def run(self):

        # Mount S3 storage
        self.execute('ubuntu', "sudo mount.s3ql --max-cache-entries 2 s3://" + self._bucketname + " /mnt/s3 --cachesize 204800 --allow-other")

        # Share the S3 storage
        self.execute('ubuntu', "echo '/mnt/s3 " + self._webserver.private_ip + "(rw,async)' >> /etc/exports")
        self.execute('ubuntu', "sudo service nfs-kernel-server restart")

        # PLEX media server is ready
        self.is_ready = True


class FileUploader(Server):
    def __init__(self, driver, net, size, image_id, key_pair, plex_server):
        super(FileUploader, self).__init__(driver, net, size, image_id, key_pair)
        self._plex_server = plex_server

    @property
    def name(self):
        return 'FileUploader'

    def run(self):
        while not self._plex_server.is_ready():
            time.sleep(1000)

        # Mount S3 storage
        self.execute('ubuntu', "sudo mount " + self._plex_server.private_ip + ":/mnt/s3 /mnt/s3");

        # Start web server
        self.execute('ubuntu', "python /home/ubuntu/hesso.cloud.plex/webserver/index.py");
