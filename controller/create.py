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
            self.password_setting()
        else:
            print(f"password is None")
            self.password = ''
            self.password_setting()

    def password_setting(self):
        hostip = utils.get_host_ip()
        command = 'linstor encryption cp'

        log_cmd = f"{command}\\n{self.password}\\n{self.password}"

        try:
            child = pexpect.spawn(command)
            time.sleep(2)

            child.expect('Passphrase:')
            child.sendline(self.password)
            child.expect('Reenter passphrase:')
            child.sendline(self.password)

            child.expect(pexpect.EOF)

            log_data = f"{hostip} - {log_cmd} - {child.before.decode()}"
            utils.Log().logger.info(log_data)
        except Exception as e:
            print(f"error:{e}")
    def profile_setting(self):
        command = "cat /etc/linstor/linstor.toml"
        result = subprocess.run(command, shell=True, capture_output=True, text=True).stdout



if __name__ == "__main__":
    print("")