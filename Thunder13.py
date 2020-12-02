'''
v1.13
    1.增加音效处理
'''

import pygame
import random
import time


#将pygame.display方法改名
_display = pygame.display
BG_COLOR = pygame.Color(0,0,0)
TEXT_COLOR =pygame.Color(255,0,0)
#难度等级(1-10):
enemyDifficulty = 1
versions = 'v1.13'

#主逻辑类
class MainGame():
    SCREEN_WIDTH = 700
    SCREEN_HEIGHT = 850
    #窗口对象
    window = None #surface类型
    P1_Plane = None
    enemyPlaneList = []
    enemyPlaneNum = 5
    myBulletList = []
    eBulletList = []
    explode_list = []
    myScore = 0
    DeadStartTime = 0 #死亡开始计时
    DeadTime = 3 #复活时间

    #开始游戏
    def startGame(self):
        #加载游戏窗口(surface)
        _display.init()
        MainGame.window  = _display.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT])  #返回Surface类
        #设置游戏标题
        _display.set_caption('雷电'+versions)
        #v1.13新增播放音效
        self.show_main_music()
        #创建飞机
        MainGame.P1_Plane = myPlane(280,650)
        #创建敌方飞机
        MainGame.createEnemyPlane(self)

        while True:
            #渲染背景
            MainGame.window.fill(BG_COLOR)

            #调用时间处理方法
            self.getEvent()

            #调用字体显示方法
            MainGame.window.blit(self.showText('剩余敌机数量：%d'%self.enemyPlaneNum),(5,5))
            MainGame.window.blit(self.showText('当前分数：%d'%self.myScore), (550, 820))

            #调用展示我方飞机的方法
            self.show_P1_Plane()

            #调用展示敌方飞机的方法
            self.show_Enemy_Plane()

            #调用展示我方子弹的方法
            self.show_P1_Bullet()

            #调用展示敌方子弹的方法
            self.show_Enemy_Bullet()

            #调用展示爆炸的方法
            self.show_Explode()
            #刷新屏幕
            _display.update()
            #v1.4主逻辑休眠
            time.sleep(0.01)

    #播放音效的方法
    def show_main_music(self):
        main_Music = Musice('Music/Main Screen.mp3')
        main_Music.play_music(-1)

    #展示我方飞机的方法
    def show_P1_Plane(self):
        # 加载我方飞机
        if MainGame.P1_Plane:
            if MainGame.P1_Plane.live :
                MainGame.P1_Plane.display_plane()
                # 调用我方飞机移动的方法
                if not MainGame.P1_Plane.stop:
                    MainGame.P1_Plane.move()
            else:
                if MainGame.DeadStartTime == 0:
                    MainGame.DeadStartTime = time.time()
                if time.time() > MainGame.DeadStartTime + MainGame.DeadTime:
                    MainGame.P1_Plane.live = True
                    MainGame.DeadStartTime = 0

    #展示敌方飞机的方法
    def show_Enemy_Plane(self):
        # 加载敌方飞机
        for i in MainGame.enemyPlaneList:
            if i.elive:
                i.display_enemy_plane()
                # 地方飞机随机移动
                i.enemy_move()
                MainGame.enemyFire(self, i)
            else:
                MainGame.enemyPlaneList.remove(i)

    #展示我方子弹的方法
    def show_P1_Bullet(self):
        for j in MainGame.myBulletList:
            j.display_bullet()
            j.hit_Plane()
            if not j.bullet_move():
                MainGame.myBulletList.remove(j)

    #展示敌方子弹的方法
    def show_Enemy_Bullet(self):
        for k in MainGame.eBulletList:
            k.display_bullet()
            k.hit_MyPlane()
            if not k.bullet_move():
                MainGame.eBulletList.remove(k)

    #我方射击创建子弹
    def fire(self,plane):
        Bullet = bullet(plane)
        MainGame.myBulletList.append(Bullet)

    #创造敌方飞机
    def createEnemyPlane(self):
        for i in range(0,MainGame.enemyPlaneNum):
            random_randLeft = random.randint(1,MainGame.SCREEN_WIDTH)
            random_randSpeed = random.randint(1,3)
            enemy_Plane = enemyPlane(random_randLeft,1,random_randSpeed)
            MainGame.enemyPlaneList.append(enemy_Plane)

    #创造敌方子弹
    def createBullet(self,plane):
        Bullet = bullet(plane)
        MainGame.eBulletList.append(Bullet)

    #实现敌方飞机随机射击
    def enemyFire(self,plane):
        i = random.randint(0,100)
        if i < enemyDifficulty:
            MainGame.createBullet(self,plane)

    #展示爆炸
    def show_Explode(self):
        for explode in self.explode_list:
            if explode.live:
                explode.display_Explode()
            else:
                MainGame.explode_list.remove(explode)
    #获取事件响应
    def getEvent(self):
        eventList = pygame.event.get()
        for event in eventList:
            #type属性
            if event.type == pygame.QUIT:
                self.gameOver()

            if event.type == pygame.KEYDOWN:
                if MainGame.P1_Plane.live:
                    if event.key == pygame.K_LEFT:
                        #修改飞机方向，因为飞机的图片决定方向，修改方向的时候，意味着飞机会更新图片
                        MainGame.P1_Plane.direction = 'L'
                        MainGame.P1_Plane.stop = False
                    elif event.key == pygame.K_RIGHT:
                        MainGame.P1_Plane.direction = 'R'
                        MainGame.P1_Plane.stop = False
                    elif event.key == pygame.K_UP:
                        MainGame.P1_Plane.direction = 'U'
                        MainGame.P1_Plane.stop = False
                    elif event.key == pygame.K_DOWN:
                        MainGame.P1_Plane.direction = 'D'
                        MainGame.P1_Plane.stop = False
                    elif event.key == pygame.K_SPACE:
                        #发射子弹事件相应
                        print('BIU BIU BIU~~')
                        biu_music = Musice('music/Mei.mp3')
                        biu_music.play_music(1)
                        MainGame.fire(self,MainGame.P1_Plane)

                if event.key == pygame.K_q:
                    self.gameOver()

                if event.key == pygame.K_r and not MainGame.P1_Plane:
                    print("胡汉三又来了")
                    MainGame.P1_Plane = myPlane(280,650)


            if event.type == pygame.KEYUP:
                MainGame.P1_Plane.stop = True

    #给一个字符串，返回一个包含字符的表面（surface）
    def showText(self,text):
        #字体模块初始化
        pygame.font.init()
        #创建字体对象
        font = pygame.font.SysFont('华文楷体',18,True)
        #使用字体渲染内容
        text_Surface = font.render(text,True,TEXT_COLOR)
        #返回包含内容的surface
        return text_Surface

    def gameOver(self):
        print('游戏结束')
        exit()


#继承精灵类的类，供其他类来继承
class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

#飞机类
class plane(BaseItem):
    #初始化
    def __init__(self,posX,posY):
        self.images = {
                        'U':pygame.image.load('img/myPlaneUp.jpg'),
                        'D':pygame.image.load('img/myPlaneDown.jpg'),
                        'L':pygame.image.load('img/myPlaneLeft.jpg'),
                        'R':pygame.image.load('img/myPlaneRight.jpg')
        }
        self.direction = 'U'  #控制方向
        self.image = self.images[self.direction]
 
        self.rect = self.image.get_rect()
        self.rect.left = posX
        self.rect.top = posY
        self.speed = 5

        #控制飞机连续移动的开关
        self.stop = True
        self.live = True

    def display_plane(self):
        #设置飞机图片
        self.image = self.images[self.direction]
        #将飞机加入到窗口中
        MainGame.window.blit(self.image,self.rect)

    def move(self):
        #修改飞机坐标:取决于飞机的方向
        if self.direction == 'U':
            if self.rect.top > 0:
                #根据飞机速度，进行偏移
                self.rect.top -= self.speed
        elif self.direction == 'D':
           if self.rect.top < MainGame.SCREEN_HEIGHT - self.rect.height:
                self.rect.top += self.speed
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
             if self.rect.left < MainGame.SCREEN_WIDTH - self.rect.width:
                 self.rect.left += self.speed

#子类 我方飞机
class myPlane(plane):
    pass

#子类 敌方飞机
class enemyPlane(plane):
    def __init__(self,left,top,speed):
        self.images = {
            'U': pygame.image.load('img/enemyPlaneU.png'),
            'D': pygame.image.load('img/enemyPlaneD.png'),
            'L': pygame.image.load('img/enemyPlaneL.png'),
            'R': pygame.image.load('img/enemyPlaneR.png')
        }
        self.direction = self.enemyDirection()  # 控制方向
        self.image = self.images[self.direction]  #返回一个surface图层

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = speed

        self.step = 0
        self.elive = True

    def enemyDirection(self):
        dirnum = random.randint(1,4)
        if dirnum == 1:
            self.direction = 'U'
        elif dirnum == 2:
            self.direction = 'D'
        elif dirnum == 3:
            self.direction = 'L'
        elif dirnum == 4:
            self.direction = 'R'
        return self.direction

    def display_enemy_plane(self):
        #设置飞机图片
        self.image = self.images[self.direction]
        #将飞机加入到窗口中
        MainGame.window.blit(self.image,self.rect)

    def enemy_move(self):
        #随机移动距离
        if self.step == 0:
            # 随机方向
            self.direction = self.enemyDirection()
            self.step = random.randint(1,50)
        else:
            self.move()
            self.step -= 1

#子弹类
class bullet(BaseItem):
    def __init__(self,plane):
        self.image = pygame.image.load('img/bullet.png')
        self.direction = plane.direction
        self.rect = self.image.get_rect()

        if plane.direction == 'U':
            self.rect.left = plane.rect.left + plane.rect.width / 2 - self.rect.width / 2
            self.rect.top = plane.rect.top - self.rect.height
        elif plane.direction == 'D':
            self.rect.left = plane.rect.left + plane.rect.width / 2 - self.rect.width / 2
            self.rect.top = plane.rect.top + plane.rect.height
        elif plane.direction == 'L':
            self.rect.left = plane.rect.left - self.rect.width
            self.rect.top = plane.rect.top + plane.rect.height / 2 - self.rect.height / 2
        elif plane.direction == 'R':
            self.rect.left = plane.rect.left + plane.rect.width
            self.rect.top = plane.rect.top + plane.rect.height / 2 - self.rect.height / 2

        self.speed = MainGame.P1_Plane.speed*1.5
        self.live = True

    def display_bullet(self):
        MainGame.window.blit(self.image,self.rect)

    def bullet_move(self):
        if 0 < self.rect.top < MainGame.SCREEN_HEIGHT or 0 < self.rect.left < MainGame.SCREEN_WIDTH:
            if self.direction == 'U':
                self.rect.top -= self.speed
            elif self.direction == 'D':
                self.rect.top += self.speed
            elif self.direction == 'L':
                self.rect.left -= self.speed
            elif self.direction == 'R':
                self.rect.left += self.speed
            return self.live
        else:
            self.live = False
            return self.live

    #v1.9 新增 子弹与敌方飞机碰撞的方法
    def hit_Plane(self):
        for ePlane in MainGame.enemyPlaneList:
            if pygame.sprite.collide_rect(self,ePlane):
                self.live = False
                ePlane.elive = False
                MainGame.enemyPlaneNum -= 1
                MainGame.myScore += 100

                #v1.10新增爆炸效果
                explode = Explode(ePlane.rect)
                MainGame.explode_list.append(explode)

    def hit_MyPlane(self):
        if MainGame.P1_Plane:
            if MainGame.P1_Plane.live:
                if pygame.sprite.collide_rect(self,MainGame.P1_Plane):
                    self.live = False
                    MainGame.P1_Plane.live = False

                    MainGame.myScore -= 100
                    explode = Explode(MainGame.P1_Plane.rect)
                    MainGame.explode_list.append(explode)

#爆炸类
class Explode(BaseItem):
    def __init__(self,rect):
        self.images = [
            pygame.image.load('img/blast0.gif'),
            pygame.image.load('img/blast1.gif'),
            pygame.image.load('img/blast2.gif'),
            pygame.image.load('img/blast3.gif'),
            pygame.image.load('img/blast4.gif'),
            pygame.image.load('img/blast5.gif'),
            pygame.image.load('img/blast6.gif')
        ]
        self.rect = rect
        self.image = self.images[0]
        self.live = True

        #记录图片索引
        self.step = 0

    def display_Explode(self):
        if self.step < len(self.images):
            MainGame.window.blit(self.image,self.rect)
            self.image = self.images[self.step]
            self.step += 1
        else:
            self.live = False
            self.step = 0
#音效类
#V1.13 新增音效处理
class Musice():
    def __init__(self,music):
        self.music = music
        pygame.mixer.init()
        pygame.mixer_music.load(self.music)
    def play_music(self,num):
        pygame.mixer.music.play(num)

mainGame1 = MainGame()
mainGame1.startGame()
# import sys
# value = sys.path
# for path in value:
#     print(path)