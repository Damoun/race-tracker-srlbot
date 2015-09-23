"""
This file provide a class execute received commands.
"""
from __future__ import print_function
import json
import requests


class SRLCommands(object):
    """
    Class to implement action on SpeedRunsLive RaceBot command.
    """
    def __init__(self, bot, admins):
        self.bot = bot
        self.admins = admins
        bot.commands = self

    def do_quit(self, author, words):
        """
        Disconnect the bot properly.
        """
        if any(author in admin for admin in self.admins):
            self.bot.die(len(words) == 2 and words[1] or "")
            return True
        return False

    def do_startrace(self, _, words):
        """
        Handle a new starting race.
        """
        if len(words) < 2:
            return False
        print('New starting race for game %s' % words[1])
        return True


class HTTPSRLCommands(SRLCommands):
    """
    Command class to push command to an url.
    """
    def __init__(self, bot, admins, urls):
        super(HTTPSRLCommands, self).__init__(bot, admins)
        self.urls = urls

    def do_startrace(self, author, words):
        """
        Publish new starting race to a web-service.
        """
        if super(HTTPSRLCommands, self).do_startrace(author, words) == False:
            return False
        url = self.urls['startrace']
        payload = {'abbrev': words[1]}
        try:
            requests.post(url, data=json.dumps(payload))
        except requests.exceptions.ConnectionError:
            return False
        return True
