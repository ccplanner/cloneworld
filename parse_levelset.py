from level import Level
from player import Player
from ascii import *
import re

#given ascii representation of levels return a list of level objects
#for now only returns first level (because havent implemented custom tiles end block parsing

#todo error checking, like make sure chip and an exit exists...
def parse_levelset(input):
    levels=[]
    for lvlstr in re.findall('%%%[^%]*', input):
        dungeon=re.split("\n", re.split("\nend", re.split("map\n", lvlstr)[1])[0])
        
        level=Level()
        for y in range(0, len(dungeon)):
            for x in range(0, (len(dungeon[y])+1)//2):
                c=dungeon[y][x*2]
                if c in Data:
                    tileclass=Data[c]
                    level.top_layer[y][x]=tileclass(x, y)
                    
                    if tileclass == MyPlayer:
                        level.x=x
                        level.y=y
                else:
                    Debug.notify('character %s not recognized'%c)
            
                
        
        levels.append(level)
        break #TODO for now only want the first level
    return levels