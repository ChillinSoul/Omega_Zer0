import helpers as helpers
import pytest


def test_inbound():
       
       assert bool(helpers.inbound(4,-2))==True
       pass
       assert bool(helpers.inbound(7,1))==True
       pass
       assert bool(helpers.inbound(7,-8))==False
       pass

def test_Legal():
       b=[4,5]
       op='37' 
       i=1
       if i>1:
              assert bool(helpers.Legal(b,36,'player',op))==True

     
