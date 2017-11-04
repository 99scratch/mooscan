import argparse
import pytest
import responses
from pytest_mock import mocker
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


@responses.activate
def test_invalid_url_format():

    # Arrange
    argv = ['--url', 'invalidurl']

    # Act
    parser = CliArgHandler()

    # Assert
    with pytest.raises(SystemExit):
        parser.parse(argv)


@responses.activate
def test_url_not_moodle_validate():

    # Arrange
    httpurl = 'http://somesite.com'
    responses.add(responses.GET, httpurl + '/login/index.php', status=404)
    responses.add(responses.GET, httpurl + '/lib/db/install.xml', status=404)

    argv = ['--url', httpurl]

    # Act
    parser = CliArgHandler()

    # Assert
    with pytest.raises(SystemExit):
        parser.parse(argv)


@responses.activate
def test_url_is_moodle_validate():

    # Arrange
    httpurl = 'http://somesite.com'
    responses.add(responses.GET, httpurl + '/login/index.php', status=200)
    responses.add(responses.GET, httpurl + '/lib/db/install.xml', status=200)

    argv = ['--url', httpurl]

    expected_arguments = {
        'allscans': True,
        'htaccess': False,
        'update': False,
        'url': httpurl,
        'verbose': None,
        'version': False
    }

    # Act
    parser = CliArgHandler()
    arguments = parser.parse(argv)

    # Assert
    assert vars(arguments) == expected_arguments
