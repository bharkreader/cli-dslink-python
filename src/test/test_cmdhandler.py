import unittest

from dsacli import cmdhandler

class CmdHandlerTests(unittest.TestCase):
    def setUp(self):
        self.requester = "test_requester"
        self.test_cmdhandler = cmdhandler.CmdHandler(self.requester)

    def test_init(self):
        self.assertEqual(self.test_cmdhandler._requester, "test_requester")

    def test_greet(self):
        self.test_cmdhandler.do_greet("")
        # Nothing to test

    def test_do_exit(self):
        actual = self.test_cmdhandler.do_exit("")
        self.assertEqual(actual, True)