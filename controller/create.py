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
        self.hostip = utils.get_host_ip()

    def main(self):
        if self.password is not None:
            print(f"密码配置为: {self.password}")
        else:
            print(f"密码配置为空")
            self.password = ''

        self.password_setting()
        self.profile_setting()


    def password_setting(self):
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

            log_data = f"{self.hostip} - {log_cmd} - {child.before.decode()}"
            utils.Log().logger.info(log_data)
            print(f"linstor集群密码配置完成")
        except Exception as e:
            print(f"linstor集群密码配置错误: {e}")

    def profile_setting(self):
        try:
            if self.password == '':
                command = "echo '[encrypt]\\npassphrase=\"\"' >> /etc/linstor/linstor.toml"
                utils.exec_cmd(command)
            else:
                command = f"echo '[encrypt]\\npassphrase=\"{self.password}\"' >> /etc/linstor/linstor.toml"
                utils.exec_cmd(command)
            print(f"linstor.toml文件配置完成")
        except Exception as e:
            print(f"linstor.toml文件配置错误: {e}")



if __name__ == "__main__":
    pass