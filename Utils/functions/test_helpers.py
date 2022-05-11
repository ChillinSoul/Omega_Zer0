import helpers as helpers
import pytest


def test_inbound():
       
       assert bool(helpers.inbound(4,-2))==True
       pass
       assert bool(helpers.inbound(7,1))==False
       pass
       assert bool(helpers.inbound(7,-8))==False
       pass

def test_Legal():
       t = -8
       r = +1
       d = +8
       l = -1
       tl = t+l
       dl = d+l
       dr = d+r
       tr = t+r

       directions = [t,r,d,l,tl,dl,dr,tr]    
       
       b=list(range(0, 64))
       op='w' 
       player='b'
       i=2
       move=36   
       assert bool(helpers.Legal(b,move,player,op))==False
       for dir in directions:
              if b[36+dir*(i)] == player and i>1:
                     assert bool(helpers.Legal(b,36,player,op))==True



     
