"""
Getting settings of the project by reading the settings.ini
"""
import os
from ConfigParser import ConfigParser


settings = ConfigParser()
settings.read(os.getenv('RACETRACKER_SETTINGS',
                        default='/etc/race-tracker/settings.ini'))
