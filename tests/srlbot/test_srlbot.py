"""
This file contain unit test for the srlbot/srlbot.py file.
"""
from unittest import TestCase
from mock import Mock, MagicMock, patch

from srlbot import SRLBot


class TestSRLBotOnNicknameinuseMethod(TestCase):
    """
    This class test the SRLBot method on_nicknameinuse.
    """
    def test_normal(self):
        """
        Test a nomal call.
        """
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
        Test a normal call.
        """
        bot = SRLBot(channel='test')
        connection = Mock()
        connection.join = MagicMock()
        connection.server = 'localhost'
        connection.port = 4242
        bot.on_welcome(connection, {})
        connection.join.assert_called_with('test')


class TestSRLBotOnPrivmsgMethod(TestCase):
    """
    This class test the SRLBot method on_privmsg.
    """
    def test_quit_command(self):
        """
        Test a private message with quit command.
        """
        bot = SRLBot(channel='test')
        bot.commands = Mock()
        bot.commands.do_quit = MagicMock()
        event = Mock()
        event.arguments = ['!quit']
        event.source.nick = 'test'
        bot.on_privmsg({}, event)
        bot.commands.do_quit.assert_called_with(
            event.source.nick, event.arguments[0].split(" ", 1)
        )

    def test_unknown_command(self):
        """
        Test a private message with any command.
        """
        bot = SRLBot(channel='test')
        bot.commands = Mock()
        event = Mock()
        event.arguments = ['.startrace sms']
        event.source.nick = 'test'
        bot.on_privmsg({}, event)
        self.assertEqual([], bot.commands.method_calls)


class TestSRLBotOnPubmsgMethod(TestCase):
    """
    This class test the SRLBot method on_pubmsg.
    """
    def test_quit_command(self):
        """
        Test a public message with quit command.
        """
        bot = SRLBot(channel='test')
        bot.commands = Mock()
        bot.commands.do_quit = MagicMock()
        event = Mock()
        event.arguments = ['!quit']
        event.source.nick = 'test'
        bot.on_pubmsg({}, event)
        bot.commands.do_quit.assert_called_with(
            event.source.nick, event.arguments[0].split(" ", 1)
        )

    def test_startrace_command(self):
        """
        Test a public message with quit command.
        """
        bot = SRLBot(channel='test')
        bot.commands = Mock()
        bot.commands.do_startrace = MagicMock()
        event = Mock()
        event.arguments = ['.startrace sms']
        event.source.nick = 'test'
        bot.on_pubmsg({}, event)
        bot.commands.do_startrace.assert_called_with(
            event.source.nick, event.arguments[0].split(" ", 1)
        )

    def test_unknown_command(self):
        """
        Test a public message with any command.
        """
        bot = SRLBot(channel='test')
        bot.commands = Mock()
        event = Mock()
        event.arguments = ['test']
        event.source.nick = 'test'
        bot.on_pubmsg({}, event)
        self.assertEqual([], bot.commands.method_calls)
