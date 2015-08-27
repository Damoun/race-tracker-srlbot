"""
Provide main entry function to run the bot.
"""
import settings
from .bot import SRLBot


def main():
    """
    Create and run the bot.
    """
    bot = SRLBot(
        server=settings.IRC_SETTINGS['server'],
        port=settings.IRC_SETTINGS['port'],
        channel=settings.IRC_SETTINGS['channel'],
        nickname=settings.IRC_SETTINGS['nickname'],
    )
    bot.start()

if __name__ == "__main__":
    main()
