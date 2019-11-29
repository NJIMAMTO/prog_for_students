##
##今いる場所から南へ10、西へ3ブロック分移動させる
##
from mcpi.minecraft import Minecraft #Minecraftクラスの呼び出し

mc = Minecraft.create() #Minecraftとの接続を作成

pos = mc.player.getTilePos() #現在位置を取得
mc.player.setTilePos(pos.x-3,pos.y,pos.z-10) #指定した場所に移動させる