from utils import *

class Counter:
    def __init__(self, data):
        self.__countResult=0
        self.__data=data
        self.__parse()
    def __parse(self):
        self.__startCounting()
    def __startCounting(self):
        for g in groupeData(self.__data):
            self.__countYes(g)
    def __countYes(self,answersOfGroup):
        merged="".join(answersOfGroup)
        count = len("".join(set(merged)))
        self.__countResult+=count
    def getCountResult(self):
        return self.__countResult


f=open("input.txt","r")
data=f.readlines()
c=Counter(data)
print("Answer 1: {}".format(c.getCountResult()))