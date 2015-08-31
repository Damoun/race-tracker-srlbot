"""
This file contain unit test for the bot/commands.py file.
"""
from unittest import TestCase
from mock import Mock, MagicMock, patch
import requests
import responses

from bot.commands import SRLCommands


def settings_side_effect(*args, **kwargs):
    """
    Mocking settings.
    """
    if args[1] == 'url':
        return 'http://localhost'
    elif args[1] == 'admins':
        return 'test'


class TestSRLCommandsDoStartraceMethod(TestCase):
    """
    This class test the SRLCommands.do_startrace method.
    """

    @responses.activate
    def test_except_connection_error(self):
        """
        Test on requests throwing an exception ConnectionError.
        """
        with patch('settings.settings.get') as settings_get:
            settings_get.side_effect = settings_side_effect
            commands = SRLCommands(Mock())
            responses.add(responses.GET, 'http://localhost',
                          body=requests.exceptions.ConnectionError())
            commands.do_startrace('test', ['.startrace', 'sms'])
            responses.reset()


class TestSRLCommandsDoQuitMethod(TestCase):
    """
    This class test the SRLCommands.do_quit method.
    """

    def test_without_message(self):
        """
        Test without a quit message.
        """
        with patch('settings.settings.get') as settings_get:
            settings_get.side_effect = settings_side_effect
            bot = Mock()
            bot.die = MagicMock()
            commands = SRLCommands(bot)
            commands.do_quit('test', ['!quit'])
            bot.die.assert_called_with('')
