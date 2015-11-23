import getpass
from storage import Storage


def get_credentials(userprompt='username', passprompt='password'):
    user = input(userprompt + " [%s]: " % getpass.getuser())

    if not user:
        user = getpass.getuser()

    password = getpass.getpass(passprompt + ": ")

    return user, password


if __name__ == '__main__':
    username, password = get_credentials()
    Storage(username, password).deploy()
