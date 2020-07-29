from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
x,y,z = mc.player.getPos()
def Tree(x,y,z):
    mc.setBlocks(x-1,y+4,z-1,x+1,y+6,z+1,57)
    mc.setBlocks(x,y,z,x,y+5,z,41)
Tree(x,y,z)