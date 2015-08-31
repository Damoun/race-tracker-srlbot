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
    def do_startrace(self, words):
        """
        Publish new starting race to a web-service.
        """
        print 'New starting race for game %s' % words[1]
        url = "%s/v1/race" % settings.get('api', 'url')
        payload = {'abbrev': words[1]}
        try:
            requests.post(url, data=json.dumps(payload))
        except requests.exceptions.ConnectionError:
            pass
