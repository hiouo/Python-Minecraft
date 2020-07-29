from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()
for i in range(100):
    mc.setBlocks(x-i,y-i,z-i,x+i,y-i,z+i,46)