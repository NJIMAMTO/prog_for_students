##
##今いる場所から南へ10、西へ3ブロック分移動させる
##
from mcpi.minecraft import Minecraft #Minecraftクラスの呼び出し
from mcpi.block import * 

mc = Minecraft.create() #Minecraftとの接続を作成

pos = mc.player.getTilePos() #現在位置を取得
mc.setBlocks(pos.x+1,pos.y,pos.z+1,pos.x+6,pos.y+3,pos.z+11,STONE) #指定した場所に石の塊を設置する