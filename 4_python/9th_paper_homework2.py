##
##逆さまのピラミッドをつくるプログラム
##
from mcpi.minecraft import Minecraft #Minecraftクラスの呼び出し
from mcpi.block import * 

mc = Minecraft.create() #Minecraftとの接続を作成

pos = mc.player.getTilePos() #自分のいる位置を取得
#そこを基準にしてピラミッドを作成
height = 51 #ピラミッドの高さ
length = height*2-1 #一番上のブロックの数(正方形の一辺の長さ)
#上からピラミッドを作っていく
for i in range(height):
    mc.setBlocks(pos.x+i,pos.y+(height-i),pos.z+i,pos.x+(length-i+1),pos.y+(height-i),pos.z+(length-i+1),STONE)



