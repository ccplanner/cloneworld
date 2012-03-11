from level import *
from ascii import *

def state2str(level):
    #i apologize, this surely isn't idiomatic python
    out=''
    for row in level.top_layer:
        for square in row:
            out=out+ReverseData[square.__class__]
        out=out+"\n"
    return out