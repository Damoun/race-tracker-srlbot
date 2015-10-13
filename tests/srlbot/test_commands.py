"""
This file contain unit test for the srlbot/commands.py file.
"""
from unittest import TestCase
from mock import Mock, MagicMock, patch
import requests
import responses

from srlbot.commands import HTTPSRLCommands


class TestHTTPSRLCommandsDoStartraceMethod(TestCase):
    """
    This class test the SRLCommands.do_startrace method.
    """

    @responses.activate
    def test_except_connection_error(self):
        """
        Test on requests throwing an exception ConnectionError.
        """
        commands = HTTPSRLCommands(
            Mock(), ['test'], {'startrace': 'http://localhost'}
        )
        responses.add(responses.GET, 'http://localhost',
                      body=requests.exceptions.ConnectionError())
        commands.do_startrace('test', ['.startrace', 'sms'])
        responses.reset()

    def test_without_abbrev(self):
        """
        Test without the abbrev argument.
        """
        commands = HTTPSRLCommands(
            Mock(), ['test'], {'startrace': 'http://localhost'}
        )
        with patch('requests.post') as mock_requests:
            commands.do_startrace('test', ['.startrace'])
            mock_requests.assert_not_called()


class TestHTTPSSRLCommandsDoQuitMethod(TestCase):
    """
    This class test the SRLCommands.do_quit method.
    """

    def test_without_message(self):
        """
        Test without a quit message.
        """
        bot = Mock()
        bot.die = MagicMock()
        commands = HTTPSRLCommands(
            bot, ['test'], {'startrace': 'http://localhost'}
        )
        commands.do_quit('test', ['!quit'])
        bot.die.assert_called_with('')

    def test_bad_admin(self):
        """
        Test without an admin.
        """
        bot = Mock()
        bot.die = MagicMock()
        commands = HTTPSRLCommands(
            bot, ['test'], {'startrace': 'http://localhost'}
        )
        commands.do_quit('test-nonadmin', ['!quit'])
        bot.die.assert_not_called()

    def test_with_message(self):
        """
        Test with a message.
        """
        bot = Mock()
        bot.die = MagicMock()
        commands = HTTPSRLCommands(
            bot, ['test'], {'startrace': 'http://localhost'}
        )
        commands.do_quit('test', ['!quit', 'bye'])
        bot.die.assert_called_with('bye')
