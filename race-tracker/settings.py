"""
Settings file for the race-tracker IRC bot.
"""
import os


IRC_SETTINGS = {
    'server': 'irc2.speedrunslive.com',
    'port': 6667,
    'nickname': 'rtbot',
    'channel': '#speedrunslive',
}

API_SETTINGS = {
    'url': 'http://localhost:8000',
    'host': 'localhost',
    'port': 8000
}

DEBUG = True
