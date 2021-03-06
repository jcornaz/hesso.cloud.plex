from libcloud.compute.ssh import ParamikoSSHClient


class Server(object):
    def __init__(self, driver, size_id, key_pair, elastic_ip):
        sizes = [size for size in driver.list_sizes() if size.id == size_id]

        if not sizes:
            raise Exception("Unavailable size : '" + size_id + "'\navailable sizes : \n" +
                            "\n'".join([size.id for size in driver.list_sizes()]))
        else:
            self._size = sizes[0]

        images = [image for image in driver.list_images() if image.id == self.image_id]
        if not images:
            raise Exception(
                "Unavailable image : '" + self.image_id + "'\navailable images : \n'" +
                "\n".join([image.id for image in driver.list_images()]))
        else:
            self._image = images[0]

        self._driver = driver
        self._private_ip = None
        self._public_ips = []
        self._key_pair = key_pair

        print("gather arguments ...")

        print("instanciating " + self.name + "...")
        self._node = self.node = self._driver.create_node(
            name=self.name,
            size=self._size,
            image=self._image
        )

        self.attach_public_ip(elastic_ip)

    def attach_public_ip(self, ip):
        if not self._node:
            raise Exception("No instanciated node")

        print("attaching floating ip " + ip + " to " + self.name + "...")

        ips = [floating_ip.ip_address for floating_ip in self._driver.ex_list_floating_ips() if floating_ip.ip_address == ip]

        if not ips:
            raise Exception("the ip " + ip + " is not available")

        self._driver.ex_attach_floating_ip_to_node(self._node, ips[0])
        self._public_ips.append(ips[0])

    def detach_public_ips(self):
        if not self._node:
            raise Exception("No instanciated node")

        for ip in self._public_ips:
            print("detaching floating ip " + ip + " from " + self.name + "...")
            self._driver.ex_detach_floating_ip_from_node(self._node, ip)

        self._public_ips = []

    def execute(self, user, command):
        if not self._public_ips:
            raise Exception("No public ip attached")

        ip = self._driver.wait_until_running([self._node], ssh_interface='public_ips')[0][1][0]
        print("connecting to " + ip)
        ssh = ParamikoSSHClient(ip, 22, user, key_files=self._key_pair)
        if ssh.connect():
            full_command = "nohup " + command + " </dev/null >logfile.log 2>&1 &"
            print("execute \"" + full_command + "\" on " + ip + "...")
            ssh.run(full_command)
            ssh.close()
        else:
            raise Exception("Unable to connect to the remote via ssh")

    @property
    def image_id(self):
        raise Exception("The property image_id must be overrided")

    @property
    def private_ip(self):
        if not self._private_ip:
            print("wait on " + self.name + " to get a private ip ...")
            self._private_ip = self._driver.wait_until_running([self._node], ssh_interface='private_ips')[0][1][0]

        return self._private_ip

    @property
    def name(self):
        return self._imageid
