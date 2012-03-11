from player import Player
from monster import Monster
from trigger import Trigger
from action import Action
from debug import *
from utility import *

class Level:
    __LEVEL_SIZE=(32,32)
    __TICKS_PER_SECOND=10
    
    Win=1
    Lose=-1
    Playing=0
    
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.ticks = 0
        self.top_layer = []
        self.bottom_layer = []
        #self.triggers = []
        #self.monsters = []
        self.player = None
        self.x = None
        self.y = None
        
        xdim, ydim = Level.__LEVEL_SIZE
        for i in xrange(ydim):
            self.top_layer.append([])
            self.bottom_layer.append([])
            for j in xrange(xdim):
                self.top_layer[i].append(Empty(i, j))
                self.bottom_layer[i].append(Empty(i, j))
        
    def tick(self):
        for e in self.top_layer:
            if e!=None:
                e.update()
        self.ticks += 1
    
    def move(self, direction):
        if direction != Action.Wait:
            dx,dy=Action.nextStep(direction)
            nx,ny=self.x+dx,self.y+dy
            if nx<0 or nx>=Level.__LEVEL_SIZE[0] or ny<0 or ny>=Level.__LEVEL_SIZE[1]:
                error('chip tried to step out side of bounds')
                return
            
            if not self.top_layer[ny][nx].canChipStep():
                error('chip tried to step on something he cant')
                return
            
            status = self.top_layer[ny][nx].effect()
            
            self.top_layer[ny][nx] = self.top_layer[self.y][self.x]
            self.top_layer[self.y][self.x] = Empty(self.x, self.y)
            
            self.x=nx
            self.y=ny
            
            return status
        
    
    def __str__(self):
        s = "Level Information:\n"
        s += "Ticks: %i\n"%(self.ticks)
        
        if (len(self.description) > 0):
            s += "Description:\n%s\n"%(self.description)
        
        s += self.briefLocations()
        return s

class Empty:
    def __init__(self, x, y):
        return
    
    def update(self):
        return
    
    def effect(self):
        return Level.Playing
    
    def canChipStep(self):
        return True

class Unimplemented(Empty):
    1

class MyPlayer(Empty):
    1

class Wall(Empty):
    def canChipStep(self):
        return False

class Exit(Empty):
    def effect(self):
        return Level.Win

class Water(Empty):
    def effect(self):
        return Level.Lose


