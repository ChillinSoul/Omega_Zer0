import helpers as helpers
import pytest


def test_inbound():
       
       assert bool(helpers.inbound(4,-2))==True
       pass
       assert bool(helpers.inbound(7,1))==False
       pass
       assert bool(helpers.inbound(7,-8))==False
       pass

#def test_Legal():
       
      
       #b=[0:63]
      # op='w' 
      # player='b'
      
      # assert bool(helpers.Legal(b,36,player,op))==False

     
