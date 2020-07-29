from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
x,y,z = mc.player.getPos()
def Tree(x,y,z):
    mc.setBlocks(x-1,y+4,z-1,x+1,y+6,z+1,46)
    mc.setBlocks(x,y,z,x,y+5,z,46)
for i in range(20):
    for j in range(10):
        for k in range(10):
            Tree(x+i*5,y+i*j,z+i*k)