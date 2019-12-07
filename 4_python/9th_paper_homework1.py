##
##サンプルプログラムloop4.pyをwhilw文で書き直したプログラム
##
from mcpi.minecraft import Minecraft #Minecraftクラスの呼び出し
from mcpi.block import * 
from time import sleep

mc = Minecraft.create() #Minecraftとの接続を作成

pos = mc.player.getTilePos() #自分のいる位置を取得
#そこを基準にして階段を作成
i = 0
while i < 5:
    mc.setBlocks(pos.x+i,pos.y+i,pos.z,pos.x+4,pos.y+i,pos.z+4,STONE)
    sleep(2) #生成過程をわかりやすくするために一時停止
    i +=1


