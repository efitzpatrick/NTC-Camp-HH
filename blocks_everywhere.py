#Everyone type
from mcpi.minecraft import Minecraft
import random

mc = Minecraft.create()
pos = mc.player.getTilePos()

#While Loops Type
def randomBlockLocations(blockType, repeats):
    counter = 0
    while counter <= repeats:
        counter = counter + 1
        x_dif = random.randint(-10, 10)
        z_dif = random.randint(-10, 10)

        x = pos.x + x_dif
        z = pos.z + z_dif
        y = mc.getHeight(x, z)
        mc.setBlock(x, y, z, blockType)
        mc.postToChat("done")

#For Loops type
def randomBlockLocations_for(blockType, repeats):
    for counter in range(repeats):
        x_dif = random.randint(-10, 10)
        z_dif = random.randint(-10, 10)

        x = pos.x + x_dif
        z = pos.z + z_dif
        y = mc.getHeight(x, z)
        mc.setBlock(x, y, z, blockType)

randomBlockLocations(92, 10)


#89
