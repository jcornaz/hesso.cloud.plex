import subprocess


def configure(access_key, secret_key):
    print('configure ecs-cli...')
    subprocess.call(['./ecs-cli', 'configure',
                     '--region', 'eu-west-1',
                     '--cluster', 'plexcluster',
                     '--access-key', access_key,
                     '--secret-key', secret_key
                     ])


def create_cluster(keypair):
    print('create cluster...')
    subprocess.call(['./ecs-cli', 'up',
                     '--keypair', keypair,
                     '--capability-iam',
                     '--size', '2',
                     '--instance-type', 't2.micro'
                     ])


def deploy_containers():
    print('deploy containers...')
    subprocess.call(['./ecs-cli', 'compose', 'up'])


def deploy(keypair, access_key, secret_key):
    configure(access_key, secret_key)
    create_cluster(keypair)
    deploy_containers()
