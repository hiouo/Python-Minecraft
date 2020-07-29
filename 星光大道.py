# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:41:00 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()
for i in range(20) :
    mc.setBlock(x+i,y-1,z+i,46)
    mc.setBlock(x+i,y-1,z+i+1,46)
    mc.setBlock(x+i,y-1,z+i+2,46)
    mc.setBlock(x+i,y-1,z+i+3,46)
    mc.setBlock(x+i,y-1,z+i+4,46)
    mc.setBlock(x+i,y-1,z+i+5,46)
    mc.setBlock(x+i,y-1,z+i+6,46)
    mc.setBlock(x+i,y-1,z+i+7,46)
    mc.setBlock(x+i,y-1,z+i+8,46)
    mc.setBlock(x+i,y-1,z+i+9,46)
    mc.setBlock(x+i,y-1,z+i+10,46)
    mc.setBlock(x+i,y-1,z+i+11,46)