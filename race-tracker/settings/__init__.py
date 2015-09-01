"""
Getting settings of the project by reading the settings.ini
"""
import os
try:
    import configparser
except ImportError:
    import ConfigParser as configparser


settings = configparser.ConfigParser()
settings.read(os.getenv('RACETRACKER_SETTINGS',
                        default='/etc/race-tracker/settings.ini'))
