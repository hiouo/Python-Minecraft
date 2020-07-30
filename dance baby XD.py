# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 14:22:03 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
from random import randrange
for i in range(100):
    x,y,z = mc.player.getTilePos()
    x = x+i
    for j in range(100):
        color = randrange(0,16)
        z = z+1
        mc.setBlock(x,y,z,35,color)
