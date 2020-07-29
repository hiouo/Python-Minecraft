# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:31:44 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()
while True:
    hits = mc.events.pollProjectileHits()
    if len(hits)>0:
        hit = hits[0]
        x,y,z = hit.pos.x,hit.pos.y,hit.pos.z
        mc.createExplosion(x,y,z,500)