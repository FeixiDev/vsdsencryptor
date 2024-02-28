import time
import pexpect
import utils.exec_command
from utils import utils
import subprocess

def main(password):
    pass

class Create:
    def __init__(self, password=None):
        self.password = password

    def main(self):
        if self.password is not None:
            print(f"password is {self.password}")
        else:
            print(f"password is None")
            self.default_password_setting()

    def default_password_setting(self):
        hostip = utils.get_host_ip()
        command = 'linstor encryption ep'
        password = ''

        log_cmd = f"{command}\n{password}"

        try:
            child = pexpect.spawn(command)
            time.sleep(2)

            child.expect('Passphrase:')
            child.sendline(password)

            child.expect(pexpect.EOF)

            log_data = f"{hostip} - {log_cmd} - {child.before.decode()}"
            utils.Log().logger.info(log_data)

        except Exception as e:
            print(f"error:{e}")



if __name__ == "__main__":
    print("")