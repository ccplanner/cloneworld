import sys

from action import Action
from level import Level
from game import Game
from textplay import textplay

CloneWorld = None

def load_level(path):
    CloneWorld = Game(path)

def move_chip(action = Action.Wait):
    return

#test function
def sandbox():
    CloneWorld = Game()
    CloneWorld.level = Level()
    pid = CloneWorld.level.setPlayer(5, 6, Action.South)
    mid = CloneWorld.level.addMonster("ball", 12, 7, Action.East)
    # NO RELATION TO THE BALL DEMO
    
    print CloneWorld.level.monsters[mid].brief()
    
    for i in range(0, 20):
        CloneWorld.update()
        print CloneWorld.level.monsters[mid].brief()
        
    print "\n", CloneWorld.level.monsters[mid]

#example usage: python main.py ../levelsets/classical.txt 2
def main(argv):
    if len(argv)<=0:
        sandbox()
    else:
        path=argv[0]
        lvlID=len(argv)>1 and int(argv[1]) or 1
        CloneWorld=Game(path)
        CloneWorld.setLevel(lvlID)
        textplay(CloneWorld.level)
        
	
    
if __name__ == "__main__":
    main(sys.argv[1:])
