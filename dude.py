from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
t = 0
while t<20:
    mc.setBlocks(x+30,y,z,x-30,y-20,z,52)
    z=z+5
    t=t+1
    