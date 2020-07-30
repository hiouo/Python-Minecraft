# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:00:18 2020

@author: appedu
"""
import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
for i in range(5000):
    r = random.randrange(1,7)
    if r==1:
        mc.setBlocks(x,y,z,x,y,z-4,46)
        z = z-4
    elif r==2:
        mc.setBlocks(x,y,z,x,y,z+4,46)
        z = z+4
    elif r==3:
        mc.setBlocks(x,y,z,x-4,y,z,46)
        x = x-4
    elif r==4:
        mc.setBlocks(x,y,z,x+4,y,z,46)
        x = x+4
    elif r==5:
        mc.setBlocks(x,y,z,x,y-4,z,46)
        y = y-4
    else :
        mc.setBlocks(x,y,z,x,y+4,z,46)
        y = y+4