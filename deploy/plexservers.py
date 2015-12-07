from cloudserver import Server
import time


class PlexMediaServer(Server):
    def __init__(self, driver, size, key_pair, elastic_ip, bucket_name, access_id, access_key):
        super(PlexMediaServer, self).__init__(driver, size, key_pair, elastic_ip)
        self._bucketname = bucket_name
        self._access_id = access_id
        self._access_key = access_key
        self.is_ready = False

    @property
    def image_id(self):
        return 'ami-ad8524de'

    @property
    def name(self):
        return 'PLEXMediaServer'

    def run(self, webserver):
        # Mount S3 storage
        self.execute('ubuntu', "echo '[s3]\nstorage-url: s3://" + self._bucketname + "\nbackend-login: " + self._access_id + "\nbackend-password: " + self._access_key + "' > /home/ubuntu/.s3ql/authfile")
        self.execute('ubuntu', "sudo mount.s3ql --max-cache-entries 2 s3://" + self._bucketname + " /mnt/s3 --cachesize 204800 --allow-other --authfile /home/ubuntu/.s3ql/authfile")

        # Share the S3 storage
        self.execute('ubuntu', "echo '/mnt/s3 " + webserver.private_ip + "(rw,async)' >> /etc/exports")
        self.execute('ubuntu', "sudo service nfs-kernel-server restart")

        # PLEX media server is ready
        self.is_ready = True


class FileUploaderServer(Server):
    def __init__(self, driver, size, key_pair, elastic_ip):
        super(FileUploaderServer, self).__init__(driver, size, key_pair, elastic_ip)

    @property
    def name(self):
        return 'FileUploader'

    @property
    def image_id(self):
        return 'ami-ad8524de'

    def run(self, plex_server):
        while not plex_server.is_ready():
            time.sleep(1000)

        # Mount S3 storage
        self.execute('ubuntu', "sudo mount " + plex_server.private_ip + ":/mnt/s3 /mnt/s3");

        # Start web server
        self.execute('ubuntu', "python /home/ubuntu/hesso.cloud.plex/webserver/index.py");
