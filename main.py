import argparse
from controller import create


# ----以下是一级命令行----
# python3 main.py
# python3 main.py create(c)
# # 创建密码



class argparse_operator:
    def __init__(self):
        self.parser = argparse.ArgumentParser(prog='argparse')
        self.setup_parse()

    def setup_parse(self):
        sub_parser = self.parser.add_subparsers()

        self.parser.add_argument('-v',
                                 '--version',
                                 dest='version',
                                 help='Show current version',
                                 action='store_true')

        parser_create = sub_parser.add_parser("create",aliases=['c'],help='create passphrase')

        parser_create.add_argument('-p', dest='password', help='Specify the password', required=False)

        self.parser.set_defaults(func=self.main_usage)
        parser_create.set_defaults(func=self.create_operation)


    def perform_all_tests(self,args):
        print("this is 'python3 main.py'")

    def main_usage(self,args):
        if args.version:
            print(f'Version: ？')
        else:
            self.perform_all_tests(args)

    def create_operation(self,args):
        # 根据是否提供了 -p 参数来决定执行哪个函数
        if args.password is not None:
            m = create.Create(args.password)
            m.main()

        else:
            m = create.Create()
            m.main()

    def parser_init(self):
        args = self.parser.parse_args()
        args.func(args)


if __name__ == "__main__":
    cmd = argparse_operator()
    cmd.parser_init()

