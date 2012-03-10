from level import Level
from state2str import *
from action import Action

#play the a clone world level using text input and output
def textplay(level):
    while 1:
        print state2str(level)
        print 'Enter move ^<>v ""=exit, anything else=wait'
        action=raw_input()
        if len(action)<1: return;
        elif action[0]=='^': direction=Action.North;
        elif action[0]=='<': direction=Action.West;
        elif action[0]=='>': direction=Action.East;
        elif action[0]=='v': direction=Action.South;
        else: direction=Action.Wait;
        level.move(direction)
