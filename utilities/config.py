import configparser

config=configparser.RawConfigParser()

config.read("D:\pytest\orange_hrm_copy\configuration\config.ini")


class Readconfig:

    @staticmethod
    def getuseremail():
        useremail=config.get("login data","username")
        return useremail


    @staticmethod
    def getpasword():
        userpasword=config.get("login data","password")
        return userpasword