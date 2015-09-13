"""
Provide main entry function to run the bot.
"""
import logging

from settings import settings
from .srlbot import SRLBot


def main():
    """
    Create and run the bot.
    """
    bot = SRLBot(
        server=settings.get('irc', 'server'),
        port=settings.getint('irc', 'port'),
        channel=settings.get('irc', 'channel'),
        nickname=settings.get('irc', 'nickname'),
    )
    bot.start()

if __name__ == "__main__":
    main()
