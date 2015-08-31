"""
This file contain unit test for the bot/commands.py file.
"""
from unittest import TestCase
from mock import Mock, MagicMock, patch

from bot import SRLBot


class TestSRLBotOnNicknameinuseMethod(TestCase):
    """
    This class test the SRLBot method on_nicknameinuse.
    """
    def test_normal(self):
        """
        Test a nomal call.
        """
        with patch('bot.commands.SRLCommands.__init__') as srlcommands:
            srlcommands.return_value = None
            bot = SRLBot()
            connection = Mock()
            connection.nick = MagicMock()
            connection.get_nickname = MagicMock(return_value='test')
            bot.on_nicknameinuse(connection, {})
            self.assertNotEqual('test_', connection.get_nickname())

class TestSRLBotOnWelcomeMethod(TestCase):
    """
    This class test the SRLBot method on_welcome.
    """
    def test_normal(self):
        """
        Test a nomal call.
        """
        with patch('bot.commands.SRLCommands.__init__') as srlcommands:
            srlcommands.return_value = None
            bot = SRLBot(channel='test')
            connection = Mock()
            connection.join = MagicMock()
            connection.server = 'localhost'
            connection.port = 4242
            bot.on_welcome(connection, {})
            connection.join.assert_called_with('test')
