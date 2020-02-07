##
##逆さまのピラミッドをつくるプログラム
##
from mcpi.minecraft import Minecraft #Minecraftクラスの呼び出し
from mcpi.block import * 

import time



def decision(mc,x,y,z):
    if (14 == mc.getBlock(x,y,z) or
        15 == mc.getBlock(x,y,z) or
        16 == mc.getBlock(x,y,z) or
        56 == mc.getBlock(x,y,z)):
        return False
    else:
        return True

def mining(mc,x,y,z):
    if decision(mc,x,y,z):
        mc.setBlock(x,y,z,0)
    if decision(mc,x,y + 1,z):
        mc.setBlock(x,y + 1,z,0)

mc = Minecraft.create() #Minecraftとの接続を作成
pos = mc.player.getTilePos() #自分のいる位置を取得

#最初の風車を作成
now_posX = pos.x
now_posY = pos.y
now_posZ = pos.z

for i in range(4):
    now_posX+=1
    mining(mc,now_posX,now_posY,now_posZ)
    
for i in range(4):
    now_posZ+=1
    mining(mc,now_posX,now_posY,now_posZ)
    
now_posZ-=4
mc.setBlock(now_posX,now_posY,now_posZ,50)

for i in range(4):
    now_posZ-=1
    mining(mc,now_posX,now_posY,now_posZ)

now_posZ+=8
#初期のＴ字部分の作成を終了

#1週目の風車を作成していく
def_count = 0
def Direction_Determination():
    global def_count
    if (def_count%8 == 0):
        def_count+=1
        return (1,0,0)
    elif(def_count%8 == 1):
        def_count+=1
        return(-1,0,0)
    elif(def_count%8 == 2):
        def_count+=1
        return(0,0,1)
    elif(def_count%8 == 3):
        def_count+=1
        return(0,0,-1)
    elif(def_count%8 == 4):
        def_count+=1
        return(-1,0,0)
    elif(def_count%8 == 5):
        def_count+=1
        return(1,0,0)
    elif(def_count%8 == 6):
        def_count+=1
        return(0,0,-1)
    elif(def_count%8 == 7):
        def_count+=1
        return(0,0,1)
    

for i in range(4):
    x,y,z = Direction_Determination()#進む方向を設定
    
    #======飛び出ている部分を作る======#
    for j in range(4):
        now_posX+=x
        now_posY+=y
        now_posZ+=z
        
        mining(mc,now_posX,now_posY,now_posZ)
        time.sleep(0.1)

    mc.setBlock(now_posX,now_posY,now_posZ,50)#目印になるトーチを設置
    #掘った分戻る
    now_posX+=-4*x
    now_posY+=y
    now_posZ+=-4*z

    #======メインの部分を作る======#
    x,y,z = Direction_Determination()#進む方向を設定
    for j in range(8):
        now_posX+=x
        now_posY+=y
        now_posZ+=z

        mining(mc,now_posX,now_posY,now_posZ)

        time.sleep(0.1)

#掘った分進む
now_posX+=4

#循環して掘っていく(2週目以降)
def_count2 = 0
def Direction_Determination2():
    global def_count2
    if (def_count2%14 == 0):
        def_count2+=1
        return (0,0,1)
    elif(def_count2%14 == 1):
        def_count2+=1
        return(1,0,0)
    elif(def_count2%14 == 2):
        def_count2+=1
        return(-1,0,0)
    elif(def_count2%14 == 3):
        def_count2+=1
        return(-1,0,0)
    elif(def_count2%14 == 4):
        def_count2+=1
        return(0,0,1)
    elif(def_count2%14 == 5):
        def_count2+=1
        return(0,0,-1)
    elif(def_count2%14 == 6):
        def_count2+=1
        return(0,0,-1)
    elif(def_count2%14 == 7):
        def_count2+=1
        return(-1,0,0)
    elif(def_count2%14 == 8):
        def_count2+=1
        return(1,0,0)
    elif(def_count2%14 == 9):
        def_count2+=1
        return(1,0,0)
    elif(def_count2%14 == 10):
        def_count2+=1
        return(0,0,-1)
    elif(def_count2%14 == 11):
        def_count2+=1
        return(0,0,1)
    elif(def_count2%14 == 12):
        def_count2+=1
        return (0,0,1)
    elif(def_count2%14 == 13):
        def_count2+=1
        return(1,0,0)

def L_shape_zone(mc,now_posX,now_posY,now_posZ):
    while True:
        #0
        #L字部分
        x,y,z = Direction_Determination2()#進む方向を設定

        for j in range(4):
            now_posX+=x
            now_posY+=y
            now_posZ+=z
            
            mining(mc,now_posX,now_posY,now_posZ)

            time.sleep(0.1)

        
        x,y,z = Direction_Determination2()#進む方向を設定
        
        for j in range(4):
            now_posX+=x
            now_posY+=y
            now_posZ+=z
            
            if decision(mc,now_posX,now_posY + 1,now_posZ):
                mc.setBlock(now_posX,now_posY + 1,now_posZ,0)

            #トーチが有ればL字部分を作り続ける
            if (50 == mc.getBlock(now_posX,now_posY,now_posZ)) and (j==3):
                now_posX,now_posY,now_posZ = L_shape_zone(mc,now_posX,now_posY,now_posZ)
            #トーチが無ければwhileループを抜ける
            elif (50 != mc.getBlock(now_posX,now_posY,now_posZ)) and (j==3):
                mc.setBlock(now_posX,now_posY,now_posZ,50)#目印になるトーチを設置
                break
            else:
                if decision(mc,now_posX,now_posY,now_posZ):
                    mc.setBlock(now_posX,now_posY,now_posZ,0)

            time.sleep(0.1)
        return now_posX,now_posY,now_posZ

for _ in range(2):
    for _ in range(4):
        now_posX,now_posY,now_posZ = L_shape_zone(mc,now_posX, now_posY, now_posZ)
        
        #直線部分
        x,y,z = Direction_Determination2()#進む方向を設定
        while True:
            now_posX+=x
            now_posY+=y
            now_posZ+=z
            
            #トーチが有ればL字部分の制作に移る
            if (50 == mc.getBlock(now_posX,now_posY,now_posZ)):
                break

            mining(mc,now_posX,now_posY,now_posZ)
            time.sleep(0.1)
        