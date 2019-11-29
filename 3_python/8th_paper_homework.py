##
##マイクラのテキストに任意の2つの文章を表示させるプログラム
##
import sys #コマンドライン引数を使うために必要なモジュール
from mcpi.minecraft import Minecraft #Minecraftクラスの呼び出し

args = sys.argv #コマンドラインに入力された引数を受け取る

#argsをひとつずつに分割する
x = args[1]
y = args[2]
z = args[3]

mc = Minecraft.create() #Minecraftとの接続を作成

pos = mc.player.getTilePos() #現在位置を取得
mc.player.setTilePos(pos.x+int(x),pos.y+int(y),pos.z+int(z)) #指定した場所に移動させる
mc.setBlock(pos.x+int(x),pos.y+int(y)-1,pos.z+int(z),5) #真下に木材を設置