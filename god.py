# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 13:51:06 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    x,y,z = mc.player.getTilePos()
    a=mc.getBlock(x,y+1,z)
    if a==8 or a==9:
        mc.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,19)