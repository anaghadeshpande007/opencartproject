import configparser
import os.path

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini') #read ini file

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=(config.get('commonInfo','baseURL'))
        return url

    @staticmethod
    def getUseremail():
        username=((config.get('commonInfo','email')))
        return username

    @staticmethod
    def getPassword():
        password = ((config.get('commonInfo', 'password')))
        return password

