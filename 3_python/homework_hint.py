import sys #コマンドライン引数を使うために必要なモジュール
from mcpi.minecraft import Minecraft #Minecraftクラスの呼び出し

args = sys.argv #コマンドラインに入力された引数を受け取る

arg1 = args[0]
arg2 = args[1]
mc = Minecraft.create() #Minecraftとの接続を作成
mc.postToChat(args1) #コマンドライン引数をチャットに表示
mc.postToChat(args2) #コマンドライン引数をチャットに表示