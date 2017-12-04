import dslink

import cmdhandler


class DSACLI(dslink.DSLink):
    def on_connected(self):
        cmdhandler.CmdHandler(self.requester).cmdloop()
        # TODO: How to trigger the DSLink to stop?


if __name__ == "__main__":
    DSACLI(dslink.Configuration(name="cli", requester=True))
