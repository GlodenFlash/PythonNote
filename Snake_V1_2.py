import pygame
import time
import random

_display = pygame.display
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR = pygame.Color(230,230,230)

class MainGame():
    _SCREEN_WIDTH = 768
    _SCREEN_HEIGHT = 500

    WINDOW = None
    P1_Snake = None
    P1_Food = None

    point = 0

    snakeBodyList = []
    eatOne = False

    IfGameOver = False

    def startGame(self):
        _display.init()
        MainGame.WINDOW = _display.set_mode([MainGame._SCREEN_WIDTH,MainGame._SCREEN_HEIGHT])

        _display.set_caption('LikeEatSnake')

        MainGame.P1_Snake = MySnake(MainGame._SCREEN_WIDTH/2-15,MainGame._SCREEN_HEIGHT/3*2)

        MainGame.P1_Food = Food()

        while True:
            if MainGame.IfGameOver:
                MainGame.WINDOW.blit(self.showText('GameOver'),
                                     (MainGame._SCREEN_WIDTH / 3 - 32, MainGame._SCREEN_HEIGHT * 2 / 3 - 32))
                self.getEvent()
                _display.update()
            else:
                MainGame.WINDOW.fill(BG_COLOR)

                self.getEvent()

                MainGame.P1_Food.displayFood()

                if not MainGame.P1_Snake.stop:
                    MainGame.P1_Snake.move()

                self.displaySnakeBody()

                MainGame.P1_Snake.displaySnake()

                MainGame.P1_Snake.eatFood()

                MainGame.WINDOW.blit(self.showText(str(self.point)),
                                     (MainGame._SCREEN_WIDTH / 2 - 32, MainGame._SCREEN_HEIGHT / 2 - 32))

                MainGame.P1_Snake.crashBody()

                _display.update()

                time.sleep(0.08)


    def displaySnakeBody(self):
        if MainGame.P1_Snake.direction == 'W':
            body = SnakeBody(MainGame.P1_Snake.rect.left,
                             MainGame.P1_Snake.rect.top + MainGame.P1_Snake.rect.height)
        elif MainGame.P1_Snake.direction == 'S':
            body = SnakeBody(MainGame.P1_Snake.rect.left,
                             MainGame.P1_Snake.rect.top - MainGame.P1_Snake.rect.height)
        elif MainGame.P1_Snake.direction == 'A':
            body = SnakeBody(MainGame.P1_Snake.rect.left + MainGame.P1_Snake.rect.width,
                             MainGame.P1_Snake.rect.top)
        elif MainGame.P1_Snake.direction == 'D':
            body = SnakeBody(MainGame.P1_Snake.rect.left - MainGame.P1_Snake.rect.width,
                             MainGame.P1_Snake.rect.top)
        MainGame.snakeBodyList.append(body)

        for body in MainGame.snakeBodyList:
            body.display_Body()
        MainGame.P1_Snake.length = len(MainGame.snakeBodyList)
        if not MainGame.eatOne:
            del MainGame.snakeBodyList[0]
        else:
            MainGame.eatOne = False

    def showText(self,text):
        pygame.font.init()
        font = pygame.font.SysFont('Msyh', 64, True)
        text_Surface = font.render(text, True, TEXT_COLOR)
        return text_Surface

    def getEvent(self):
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                self.gameover()
            if event.type == pygame.KEYDOWN and not MainGame.IfGameOver:
                if event.key == pygame.K_UP:
                    if MainGame.P1_Snake.direction != 'S':
                        MainGame.P1_Snake.direction = 'W'
                        MainGame.P1_Snake.stop = False
                elif event.key == pygame.K_DOWN:
                    if MainGame.P1_Snake.direction != 'W':
                        MainGame.P1_Snake.direction = 'S'
                        MainGame.P1_Snake.stop = False
                elif event.key == pygame.K_LEFT:
                    if MainGame.P1_Snake.direction != 'D':
                        MainGame.P1_Snake.direction = 'A'
                        MainGame.P1_Snake.stop = False
                elif event.key == pygame.K_RIGHT:
                    if MainGame.P1_Snake.direction != 'A':
                        MainGame.P1_Snake.direction = 'D'
                        MainGame.P1_Snake.stop = False
                elif event.key == pygame.K_SPACE:
                    MainGame.P1_Food.randomChangePos()
                elif event.key == pygame.K_q:
                    self.gameover()

    def gameover(self):
        print('gameover')
        exit()

class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class MySnake(BaseItem):
    def __init__(self,posX,posY):
        self.images = {
                        'W':pygame.image.load('img/snakehead_w.png'),
                        'S':pygame.image.load('img/snakehead_s.png'),
                        'A':pygame.image.load('img/snakehead_a.png'),
                        'D':pygame.image.load('img/snakehead_d.png')
        }
        self.direction = 'W'
        self.image = self.images[self.direction]

        self.rect = self.image.get_rect()
        self.rect.left = posX
        self.rect.top = posY
        self.speed = 30
        self.stop = True

        self.length = 0

    def displaySnake(self):
        self.image = self.images[self.direction]
        MainGame.WINDOW.blit(self.image,self.rect)

    def move(self):
        if self.direction == 'W':
            if self.rect.top < 0:
                print('gameover')
                MainGame.IfGameOver = True
            else:
                self.rect.top -= self.speed
        elif self.direction == 'S':
            if self.rect.top > MainGame._SCREEN_HEIGHT - self.rect.height:
                print('gameover')
                MainGame.IfGameOver = True
            else:
                self.rect.top = self.rect.top + self.speed
        elif self.direction == 'A':
            if self.rect.left < 0:
                print('gameover')
                MainGame.IfGameOver = True
            else:
                self.rect.left -= self.speed
        elif self.direction == 'D':
            if self.rect.left > MainGame._SCREEN_WIDTH - self.rect.width:
                print('gameover')
                MainGame.IfGameOver = True
            else:
                self.rect.left = self.rect.left + self.speed

    def eatFood(self):
        if pygame.sprite.collide_rect(self,MainGame.P1_Food):
            MainGame.P1_Food.randomChangePos()
            MainGame.point += 1
            MainGame.eatOne = True

    def crashBody(self):
        for body in MainGame.snakeBodyList:
            if pygame.sprite.collide_rect(self,body):
                print('gameover')
                MainGame.IfGameOver = True

class SnakeBody(BaseItem):
    def __init__(self,posX,posY):
        self.image = pygame.image.load('img/snakebody.png')

        self.rect = self.image.get_rect()
        self.rect.left = posX
        self.rect.top = posY

    def display_Body(self):
        MainGame.WINDOW.blit(self.image,self.rect)

class Food(BaseItem):
    def __init__(self):
        self.image = pygame.image.load('img/food.png')

        self.rect = self.image.get_rect()
        self.rect.left = MainGame._SCREEN_WIDTH/2 - 15
        self.rect.top = MainGame._SCREEN_HEIGHT/3

    def displayFood(self):
        MainGame.WINDOW.blit(self.image,self.rect)

    def randomChangePos(self):
        self.rect.left = random.randint(0,MainGame._SCREEN_WIDTH - 30)
        self.rect.top = random.randint(0,MainGame._SCREEN_HEIGHT - 30)
        MainGame.WINDOW.blit(self.image, self.rect)

if __name__ == '__main__':
    maingame1 = MainGame()
    maingame1.startGame()
