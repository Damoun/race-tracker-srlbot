"""
Provide main entry function to run the bot.
"""
import logging

from .srlbot import SRLBot
from .commands import HTTPSRLCommands


def main():
    """
    Create and run the bot.
    """
    bot = SRLBot(channel="#race-tracker")
    command = HTTPSRLCommands(
        bot, ['dam0un'], {'startrace': 'http://localhost'}
    )
    bot.start()

if __name__ == "__main__":
    main()
