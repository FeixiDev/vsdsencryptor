import time

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
        command = ['linstor', 'encryption', 'ep']
        password = ''

        log_cmd = f"command\npassowrd"

        try:
            # 使用Popen执行命令
            process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       text=True)
            time.sleep(2)

            # 向命令行输入密码，\n代表回车
            # process.communicate(input=f'{password}\n{password}\n')
            stdout, stderr = process.communicate(input=f'{password}\n')

            # 等待命令执行完成
            process.wait()

            # 检查命令执行的退出状态
            if process.returncode == 0:
                log_data = f"{hostip} - {log_cmd} - {stdout}"
                print("------Command executed successfully------")
            else:
                log_data = f"{hostip} - {log_cmd} - {stderr}"
                print("------Error executing command------")
            utils.Log().logger.info(log_data)

        except Exception as e:
            print(f"error:{e}")



if __name__ == "__main__":
    print("")