# MooScan
A scanning tool for Moodle LMS, after v1.7.0

[![Build Status](https://travis-ci.org/vortexau/mooscan.svg?branch=master)](https://travis-ci.org/vortexau/mooscan) [![Python 3.4|3.5|3.6](https://img.shields.io/badge/python-3.4|3.5|3.6-brightgreen.svg)](https://www.python.org/) [![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/) [![Twitter](https://img.shields.io/badge/twitter-@vortexau_-blue.svg)](https://twitter.com/vortexau)

## How does it work?
MooScan downloads a copy of the public Moodle GIT repository and pulls in files of interest which can be used to determine the installed Moodle version, determine if local public changes have been made, and allows brute-force scanning of an install to determine any and all installed plugins (and their versions, too!)

Moodle itself includes a lot of content inside its web root that can be very revealing. Information such as composer.json, package.json, npm-shrinkwrap.json which all include version numbers used to build libraries; install.xml files used to setup databases which include version numbers, and in some older versions, .html files which include PHP - these files are pulled in by Moodle, and, in some cases, may have been modified by admins to include their *production* values (auth/ldap/config.html I'm looking at *you*!). As a Moodle admin, it would be nice to know this. As a pentester, it would be doubly-nice to know this!

## Why?
In a previous life, I was a developer in a small team maintaining a large Moodle install (35k users) and while _we_ were careful with our install, I realised that others may not be so careful..

No specific tool existed then, so in the spirit of [PoC||GTFO](https://www.alchemistowl.org/pocorgtfo/), I decided to [build my own fucking birdfeeder](https://www.alchemistowl.org/pocorgtfo/pocorgtfo02.pdf).

## Key Benefits
* Allows administrators to determine exactly what is visible externally in their Moodle installation. 
* A tool for penetration testers to find potential vulnerabilities in a Moodle installation by enumerating installed plugins, themes and libraries.

## Docker Commands
* Build container
    * `docker-compose --build up`
* Run PEP8 tests
    * `docker-compose run --entrypoint "pep8 -v *.py lib/"  mooscan`
* Run unit-tests
    * `docker-compose run --entrypoint pytest mooscan`

## Road Map
To be defined once the basic (MVP!) tool is released, functional and reliable.

## Special Thanks
* Codingo; for the gentle nudges to get this tool to a point where it may be useful for the community.
* SecTalks for the continual support and encouragement.
