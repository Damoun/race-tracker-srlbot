"""
Setup file for srlbot.
"""
from setuptools import setup


setup(
    name='srlbot',
    version='0.0.1',
    author='Damien Plenard',
    author_email='damien@plenard.me',
    url='https://github.com/race-tracker/srlbot',
    license='MIT',
    packages=['srlbot'],
    test_suite='tests',
    description=(
        'An IRC bot used to monitor race from SpeedRunsLive.'
    ),
    install_requires=['irc', 'requests'],
    extras_require={
        'test': ['coverage', 'mock', 'responses', 'codecov'],
    },
    entry_points={
        'console_scripts': [
            'srlbot = srlbot:main',
        ]
    }
)
