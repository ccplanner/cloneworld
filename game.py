from level import *
from utility import *
from parse_levelset import parse_levelset
import copy

class Game:
    def __init__(self, path=""):
        self.reset()
        
        if (len(path) > 0):
            self.loadPackageData(path)
        
    def reset(self):
        self.resetPackageData()
        
    def resetPackageData(self):
        self.level = []
        self.level = None
        
    def loadPackageData(self, path):
        file = None
        
        try:
            file = open(path)
            self.levels = parse_levelset(file.read())
        except IOError as e:
            debug.error(e)
        finally:
            if (file != None):
                file.close()
	
    def setLevel(self, lvlID=1):
        self.level=copy.deepcopy(self.levels[lvlID-1])
