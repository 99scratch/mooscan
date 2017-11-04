import argparse
import pytest
from lib.core.CliArgHandler import CliArgHandler


valid_test_site = 'http://www.testsite.com'


def test_cliarg_default_values():

    # Arrange
    argv = []

    # Act
    parser = CliArgHandler()
    arguments = parser.parse(argv)

    expected_args = {
            'allscans': True,
            'htaccess': False,
            'update': False,
            'url': None,
            'verbose': None,
            'version': False
    }

    # Assert
    assert vars(arguments) == expected_args


def test_cliarg_host_value():

    # Arrange
    argv = ['--url', valid_test_site]

    # Act
    parser = CliArgHandler()
    arguments = parser.parse(argv)

    expected_args = {
        'allscans': True,
        'htaccess': False,
        'update': False,
        'url': valid_test_site,
        'verbose': None,
        'version': False
    }

    # Assert
    assert vars(arguments) == expected_args


def test_invalid_url_format():
    
    # Arrange
    argv = ['--url', 'invalidurl']

    # Act
    parser = CliArgHandler()

    # Assert
    with pytest.raises(SystemExit):
        parser.parse(argv)
