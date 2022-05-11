import pytest
import Node
import minmax
from Node import node

def test_MinMax():
    b=[[28,35,19,17,26,27,18,10,11,8,9],[36,0,2,1,4,3]]
    list_b=b[0]
    list_w=b[1]
    lst = [0 for _ in range(64)]
    for i in list_b:
        lst[i] = "b"
    for j in list_w:
        lst[j] = "w"
    bob = node(0,4,lst,"w")
    assert minmax.MinMax(bob)[1]==16
   
