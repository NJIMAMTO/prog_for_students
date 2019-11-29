##
##今いる場所から南へ10、西へ3ブロック分移動させる
##
from mcpi.minecraft import Minecraft #Minecraftクラスの呼び出し
from mcpi.block import * 

mc = Minecraft.create() #Minecraftとの接続を作成

pos = mc.player.getTilePos() #現在位置を取得
mc.setBlock(pos.x,pos.y+2,pos.z,WOOD) #指定した場所に原木を設置する