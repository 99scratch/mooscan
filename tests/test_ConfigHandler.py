import os
from lib.core.ConfigHandler import ConfigHandler

def test_env_path():

    # Arrange
    os.environ['MOOSCAN_CONFIG_PATH'] = '/some/new/path'

    # Act
    handler = ConfigHandler()
    handler.LoadConfigPaths()

    # Assert
    assert handler.GetConfigFile() == '/some/new/path/mooscan.conf'
