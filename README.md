# MooScan
A scanning tool for Moodle LMS

[![Build Status](https://travis-ci.org/vortexau/mooscan.svg?branch=master)](https://travis-ci.org/vortexau/mooscan) [![Python 3.4|3.5|3.6](https://img.shields.io/badge/python-3.4|3.5|3.6-brightgreen.svg)](https://www.python.org/) [![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/) [![Twitter](https://img.shields.io/badge/twitter-@vortexau_-blue.svg)](https://twitter.com/vortexau)


## Key Benefits
* Allows administrators to determine exactly what is visible externally in their Moodle installation. 
* A tool for penetration testers to find potential vulnerabilities in a Moodle installation by enumerating installed plugins, themes and libraries.

## Docker Commands
* Build container
    * `docker-compose --build up`
* Run unit-tests
    * `docker-compose run --entrypoint pytest mooscan`

## Road Map
To be defined once the basic (MVP!) tool is released, functional and reliable.

## Special Thanks
* Codingo; for the gentle nudges to get this tool to a point where it may be useful for the community.
* SecTalks for the continual support and encouragement.
