import cmd

class CmdHandler(cmd.Cmd, object):

    def __init__(self, requester):
        super(CmdHandler, self).__init__("tab", None, None)
        self._requester = requester

    def do_greet(self, line):
        print("hello " + line)

    def do_exit(self, line):
        return True