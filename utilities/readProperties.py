import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        return config.get("Common info", "baseURL")

    @staticmethod
    def getUserEmail():
        return config.get("Common info", "username")

    @staticmethod
    def getUserPassword():
        return config.get("Common info", "password")