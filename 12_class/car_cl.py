#------------------
# 車クラス
#------------------
class CarClass:
    #初期化
    def __init__(self,owner,carColor,carType,speed):
        
        self.speedNow=speed #初期のスピード
        print('{}さんの{}色の{}!'
              .format(owner,carColor,carType))
        print('初期{}Kmです'.format(speed))

    #スピードアップの処理  
    def speedup(self,speed):
        self.speedNow+=speed
        print('加速{}Kmです'.format(self.speedNow))
    #スピードダウンの処理  
    def speeddown(self,speed):
        self.speedNow-=speed
        print('減速{}Kmです'.format(self.speedNow))
    
    #ライトの点灯
    #クラクション

# cr=CarClass('hideT','黒','SUV',50)  #インスタンス化
# cr.speedup(10)                      #加速する
# cr.speeddown(20)                    #減速
