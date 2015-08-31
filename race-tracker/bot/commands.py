"""
This file provide a class execute received commands.
"""
import json
import requests

from settings import settings


class SRLCommands(object):
    """
    Class to implement action on SpeedRunsLive RaceBot command.
    """
    def __init__(self, bot):
        self.url = settings.get('api', 'url')
        self.bot = bot
        self.admins = settings.get('irc', 'admins').split(',')

    def do_quit(self, author, words):
        """
        Disconnect the bot properly.
        """
        if any(author in admin for admin in self.admins):
            self.bot.die(len(words) == 2 and words[1] or "")

    def do_startrace(self, _, words):
        """
        Publish new starting race to a web-service.
        """
        print 'New starting race for game %s' % words[1]
        url = "%s/v1/race" % self.url
        payload = {'abbrev': words[1]}
        try:
            requests.post(url, data=json.dumps(payload))
        except requests.exceptions.ConnectionError:
            pass
