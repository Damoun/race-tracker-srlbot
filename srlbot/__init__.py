"""
Provide main entry function to run the bot.
"""
import logging
import argparse

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


def main():
    """
    Create and run the bot.
    """
    options = handle_argument()
    bot = SRLBot(channel="#race-tracker")
    command = HTTPSRLCommands(
        bot, ['dam0un'], {'startrace': 'http://localhost'}
    )
    bot.start()

if __name__ == "__main__":
    main()
