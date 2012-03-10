from level import *
from player import Player

#TODO these are unhandled
#Wall=None
Water=None
Ice=None
Fire=None
Bomb=None
ComputerChip=None
Socket=None
#Exit=None
Block=None
HintButton=None

Data={
    ' ' : None,
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
