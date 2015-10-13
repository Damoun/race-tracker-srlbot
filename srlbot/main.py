"""
Provide main entry function to run the bot.
"""
import logging
import argparse
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

from .srlbot import SRLBot
from .commands import HTTPSRLCommands


def handle_argument():
    """
    Handle argument given by command line.
    """
    parser = argparse.ArgumentParser(
        description='Monitor & handle SRL command from an IRC channel.'
    )
    parser.add_argument('-c', '--config',  metavar='filename', type=str,
                        nargs=1, help='set configuration file.')
    return parser.parse_args()


def get_config(filename):
    config = configparser.SafeConfigParser({
        'server': 'irc.speedrunslive.com',
        'port': '6667',
        'channel': '#speedrunslive',
        'nickname': 'srlbot',
        'admins': '',
        'startrace': 'http://localhost',
    })
    config.read(filename)
    return config


def main():
    """
    Create and run the bot.
    """
    options = handle_argument()
    config = get_config(options.config)
    bot = SRLBot(
        server=config.get('irc', 'server'),
        port=config.getint('irc', 'port'),
        channel=config.get('irc', 'channel'),
        nickname=config.get('irc', 'nickname')
    )
    HTTPSRLCommands(bot, config.get('irc', 'admins').split(','),
                    {'startrace': config.get('url', 'startrace')})
    bot.start()
