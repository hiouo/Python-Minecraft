from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat("I'm watching you.")

while True:
    x,y,z = mc.player.getTilePos()
    mc.postToChat("You are located on X:"+str(x)+", Y:"+str(y)+", Z:"+str(z))
    