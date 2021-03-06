###########################################################
## This file is part of the BrainGenix Simulation System ##
###########################################################

import yaml

'''
Name: LoadConfig
Description: This function loads and parses the system config file which tells it where to look for plugins, etc.
Date-Created: 2020-12-18
Date-Modified: 2020-12-21
'''


def LoadConfig(ConfigFilePath):

    '''
    This function loads the config from a file path.
    It's designed to read a specific set of values from the path, so it doesn't just return a dictionary value.
    This loader is not designed to be used except as the initial config loader, as it only reads a few select parameters.
    *Please don't call this function unless you know what you're doing!*
    '''

    # First Read the contents of the file and parse it #
    with open(ConfigFilePath, 'r') as File:
        ConfigFileContents = File.read()

    ConfigFileDictionary = yaml.load(ConfigFileContents, Loader=yaml.FullLoader)

    
    # Extract the important values from the dictionary and return them to the main system #
    AddonsPath = str(ConfigFileDictionary.get('AddonsPath'))
    LogPath = str(ConfigFileDictionary.get('LogPath'))
    PrintLogText = bool(ConfigFileDictionary.get('PrintLogText'))
    LogBufferLength = int(ConfigFileDictionary.get('LogBufferLength'))
    LogFileLinesBeforeSplit = int(ConfigFileDictionary.get('LogFileLinesBeforeSplit'))
    EnableGzip = bool(ConfigFileDictionary.get('gzipLogs'))
    ZKHost = str(ConfigFileDictionary.get('ZKHost'))

    DBUname = str(ConfigFileDictionary.get('DatabaseUsername'))
    DBPasswd = str(ConfigFileDictionary.get('DatabasePassword'))
    DBHost = str(ConfigFileDictionary.get('DatabaseHost'))
    DBName = str(ConfigFileDictionary.get('DatabaseName'))

    # Return the values #
    return AddonsPath, LogPath, LogBufferLength, PrintLogText, LogFileLinesBeforeSplit, EnableGzip, ZKHost, DBUname, DBPasswd, DBHost, DBName