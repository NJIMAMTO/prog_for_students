##
##風車式ブランチマイニングを自動化するプログラム
##


from mcpi.minecraft import Minecraft #Minecraftクラスの呼び出し
from mcpi.block import * 

import time

class Windmill:
    def __init__(self):
        self.mc = Minecraft.create() #Minecraftとの接続を作成
        pos = self.mc.player.getTilePos() #自分のいる位置を取得]
        self.x = pos.x
        self.y = pos.y
        self.z = pos.z
        self.DD = self.Direction_Determination()
        self.DD2 = self.Direction_Determination2()
    
    
    def Direction_Determination(self):
        """
        (x,y,z)ベクトルで掘削する方向を指定する(一周目)
        """
        yield (1,0,0)
        yield(-1,0,0)
        yield(0,0,1)
        yield(0,0,-1)
        yield(-1,0,0)
        yield(1,0,0)
        yield(0,0,-1)
        yield(0,0,1)

    def Direction_Determination2(self):
        """
        (x,y,z)ベクトルで掘削する方向を指定する(2周目)
        """
        while True:
            yield (0,0,1)
            yield (1,0,0)
            yield (-1,0,0)
            yield (-1,0,0)
            yield (0,0,1)
            yield (0,0,-1)
            yield (0,0,-1)
            yield (-1,0,0)
            yield (1,0,0)
            yield (1,0,0)
            yield (0,0,-1)
            yield (0,0,1)
            yield (0,0,1)
            yield (1,0,0)
    
    def decision(self,x,y,z):
        """
        鉄・金・ダイアモンド・石炭
        ブロックがあれば掘削しないようにする
        """
        if (14 == self.mc.getBlock(x,y,z) or
            15 == self.mc.getBlock(x,y,z) or
            16 == self.mc.getBlock(x,y,z) or
            56 == self.mc.getBlock(x,y,z)):
            time.sleep(30)
            return False
        else:
            return True

    def mining(self):
        """
        指定された箇所を掘削する
        """
        if self.decision(self.x, self.y, self.z):
            self.mc.setBlock(self.x, self.y, self.z, 0)

        if self.decision(self.x, self.y + 1, self.z):
            self.mc.setBlock(self.x, self.y + 1, self.z, 0)


    def first_mining(self):
        """
        初期のＴ字部分の作成
        """
        for _ in range(4):
            self.x+=1
            self.mining()
 
        for _ in range(4):
            self.z+=1
            self.mining()
            
        self.z-=4
        self.mc.setBlock(self.x,self.y,self.z,50)

        for _ in range(4):
            self.z-=1
            self.mining()
        self.z+=8

    def second_mining(self):
        """
        一周目の風車を作る
        """
        for _ in range(4):
            x,y,z = next(self.DD)#進む方向を設定
            
            #======飛び出ている部分を作る======#
            for _ in range(4):
                self.x+=x
                self.y+=y
                self.z+=z
                
                self.mining()
                time.sleep(0.1)

            self.mc.setBlock(self.x,self.y,self.z,50)#目印になるトーチを設置
            #掘った分戻る
            self.x+=-4*x
            self.y+=y
            self.z+=-4*z

            #======メインの部分を作る======#
            x,y,z = next(self.DD)#進む方向を設定
            for _ in range(8):
                self.x+=x
                self.y+=y
                self.z+=z

                self.mining()

                time.sleep(0.1)

        #掘った分進む
        self.x+=4

    def L_shape_mining(self):
        """
        二周目以降のＬ字部分の掘削
        """
        self.mc.postToChat("test")
        while True:
            #0
            #L字部分
            x,y,z = next(self.DD2)#進む方向を設定

            for _ in range(4):
                self.x+=x
                self.y+=y
                self.z+=z
                
                self.mining()

                time.sleep(0.1)

            
            x,y,z = next(self.DD2)#進む方向を設定
            
            for j in range(4):
                self.x+=x
                self.y+=y
                self.z+=z
                
                if self.decision(self.x,self.y + 1,self.z):
                    self.mc.setBlock(self.x,self.y + 1,self.z,0)

                #トーチが有ればL字部分を作り続ける
                if (50 == self.mc.getBlock(self.x,self.y,self.z)) and (j==3):
                    self.L_shape_mining()

                #トーチが無ければwhileループを抜ける
                elif (50 != self.mc.getBlock(self.x,self.y,self.z)) and (j==3):
                    self.mc.setBlock(self.x,self.y,self.z,50)#目印になるトーチを設置
                    self.straight_mining()
                    return 0

                else:
                    if self.decision(self.x,self.y,self.z):
                        self.mc.setBlock(self.x,self.y,self.z,0)

                time.sleep(0.1)
            
    def straight_mining(self):
        """
        二周目以降の直線部分の掘削
        """
        x,y,z = next(self.DD2)#進む方向を設定
        while True:
            self.x+=x
            self.y+=y
            self.z+=z
            
            #トーチが有ればL字部分の制作に移る
            if (50 == self.mc.getBlock(self.x,self.y,self.z)):
                return 0

            self.mining()
            time.sleep(0.1)

#===========================#実行部分#===========================#

WM = Windmill()
#初期のＴ字部分の作成
WM.first_mining()
#1週目の風車を作成していく
WM.second_mining()
#循環して掘っていく(2週目以降)
for _ in range(3):
    for _ in range(4):
        WM.L_shape_mining()
            
        