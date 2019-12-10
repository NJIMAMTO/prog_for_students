##
##ブランチマイニングの自動化
##
from mcpi.minecraft import Minecraft #Minecraftクラスの呼び出し
from mcpi.block import * 

import time

mc = Minecraft.create() #Minecraftとの接続を作成

pos = mc.player.getTilePos() #自分のいる位置を取得

#最初の風車を作成
now_posX = pos.x
now_posY = pos.y
now_posZ = pos.z

for i in range(4):
    now_posX+=1
    if not (14 == mc.getBlock(now_posX,now_posY,now_posZ) or
        15 == mc.getBlock(now_posX,now_posY,now_posZ) or
        16 == mc.getBlock(now_posX,now_posY,now_posZ) or
        56 == mc.getBlock(now_posX,now_posY,now_posZ)):
        
        mc.setBlock(now_posX,now_posY,now_posZ,0)
    
    if not (14 == mc.getBlock(now_posX,now_posY + 1,now_posZ) or
        15 == mc.getBlock(now_posX,now_posY + 1,now_posZ) or
        16 == mc.getBlock(now_posX,now_posY + 1,now_posZ) or
        56 == mc.getBlock(now_posX,now_posY + 1,now_posZ)):
        
        mc.setBlock(now_posX,now_posY + 1,now_posZ,0)
    

for i in range(4):
    now_posZ+=1

    if not (14 == mc.getBlock(now_posX,now_posY,now_posZ) or
        15 == mc.getBlock(now_posX,now_posY,now_posZ) or
        16 == mc.getBlock(now_posX,now_posY,now_posZ) or
        56 == mc.getBlock(now_posX,now_posY,now_posZ)):
        
        mc.setBlock(now_posX,now_posY,now_posZ,0)
    
    if not (14 == mc.getBlock(now_posX,now_posY + 1,now_posZ) or
        15 == mc.getBlock(now_posX,now_posY + 1,now_posZ) or
        16 == mc.getBlock(now_posX,now_posY + 1,now_posZ) or
        56 == mc.getBlock(now_posX,now_posY + 1,now_posZ)):
        
        mc.setBlock(now_posX,now_posY + 1,now_posZ,0)
    

now_posZ-=4
mc.setBlock(now_posX,now_posY,now_posZ,50)

for i in range(4):
    now_posZ-=1
    if not (14 == mc.getBlock(now_posX,now_posY,now_posZ) or
        15 == mc.getBlock(now_posX,now_posY,now_posZ) or
        16 == mc.getBlock(now_posX,now_posY,now_posZ) or
        56 == mc.getBlock(now_posX,now_posY,now_posZ)):
        
        mc.setBlock(now_posX,now_posY,now_posZ,0)
    
    if not (14 == mc.getBlock(now_posX,now_posY + 1,now_posZ) or
        15 == mc.getBlock(now_posX,now_posY + 1,now_posZ) or
        16 == mc.getBlock(now_posX,now_posY + 1,now_posZ) or
        56 == mc.getBlock(now_posX,now_posY + 1,now_posZ)):
        
        mc.setBlock(now_posX,now_posY + 1,now_posZ,0)
    

mc.setBlock(now_posX,now_posY,now_posZ,50)
now_posZ+=8
mc.setBlock(now_posX,now_posY,now_posZ,50)
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
    x,y,z = Direction_Determination()
    mc.postToChat(x)
    for j in range(4):
        now_posX+=x
        now_posY+=y
        now_posZ+=z

        if not (14 == mc.getBlock(now_posX,now_posY,now_posZ) or
            15 == mc.getBlock(now_posX,now_posY,now_posZ) or
            16 == mc.getBlock(now_posX,now_posY,now_posZ) or
            56 == mc.getBlock(now_posX,now_posY,now_posZ)):
            
            mc.setBlock(now_posX,now_posY,now_posZ,0)
        
        if not (14 == mc.getBlock(now_posX,now_posY + 1,now_posZ) or
            15 == mc.getBlock(now_posX,now_posY + 1,now_posZ) or
            16 == mc.getBlock(now_posX,now_posY + 1,now_posZ) or
            56 == mc.getBlock(now_posX,now_posY + 1,now_posZ)):
            
            mc.setBlock(now_posX,now_posY + 1,now_posZ,0)
        time.sleep(2)

    mc.setBlock(now_posX,now_posY,now_posZ,50)
    now_posX+=-4*x
    now_posY+=y
    now_posZ+=-4*z

    x,y,z = Direction_Determination()
    mc.postToChat(def_count)
    for j in range(8):
        now_posX+=x
        now_posY+=y
        now_posZ+=z

        if not (14 == mc.getBlock(now_posX,now_posY,now_posZ) or
            15 == mc.getBlock(now_posX,now_posY,now_posZ) or
            16 == mc.getBlock(now_posX,now_posY,now_posZ) or
            56 == mc.getBlock(now_posX,now_posY,now_posZ)):
            
            mc.setBlock(now_posX,now_posY,now_posZ,0)
        
        if not (14 == mc.getBlock(now_posX,now_posY + 1,now_posZ) or
            15 == mc.getBlock(now_posX,now_posY + 1,now_posZ) or
            16 == mc.getBlock(now_posX,now_posY + 1,now_posZ) or
            56 == mc.getBlock(now_posX,now_posY + 1,now_posZ)):
            
            mc.setBlock(now_posX,now_posY + 1,now_posZ,0)

        time.sleep(2)
        