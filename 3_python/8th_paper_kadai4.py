##
##今いる場所から南へ10、西へ3ブロック分移動させる
##
from mcpi.minecraft import Minecraft #Minecraftクラスの呼び出し
from mcpi.block import * 

mc = Minecraft.create() #Minecraftとの接続を作成

pos = mc.player.getTilePos() #現在位置を取得
info = mc.getBlock(pos.x,pos.y-1,pos.z) #指定した場所のブロック情報を取得する
mc.postToChat(info)