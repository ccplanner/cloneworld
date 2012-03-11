from level import *
from player import Player

#TODO these are unhandled
#Wall=None
Water=Unimplemented
Ice=Unimplemented
Fire=Unimplemented
Bomb=Unimplemented
ComputerChip=Unimplemented
Socket=Unimplemented
#Exit=None
Block=Unimplemented
HintButton=Unimplemented

Data={
    ' ' : Empty,
    '@' : MyPlayer, #Chip himself
    '#' : Wall,
    ',' : Water,
    '=' : Ice,
    '&' : Fire,
    '6' : Bomb,
    '$' : ComputerChip,
    'H' : Socket,
    'E' : Exit,
#    '[]' : Block,
    '?' : HintButton
}

ReverseData=dict((v,k) for k, v in Data.iteritems())