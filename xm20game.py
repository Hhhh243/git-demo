# import sys
import pygame
from time import sleep
WIDTH = 600
HEIGHT = 600
import random
class Snake:
    def __init__(self,screen):
        self.screen = screen
        self.body = []  #长度
        self.fx=pygame.K_RIGHT  #方向
        self.init_body()
    def init_body(self, length = 5 ):
        left,top=(0,0)
        for i in range(5):
            if self.body:
                left,top=self.body[0].left,self.body[0].top
                node=pygame.Rect(left+20,top,20,20)
            else:
                node=pygame.Rect(0,0,20,20)
            self.body.insert(0,node)
    def draw_snake(self):
        for n in self.body:
            pygame.draw.rect(self.screen,(62,122,178),n,0)

    def add_node(self,):
        if self.body:
            left,top=self.body[0].left,self.body[0].top
            if self.fx==pygame.K_RIGHT:
                left+=20
            elif self.fx==pygame.K_LEFT:
                left-=20
            elif self.fx==pygame.K_UP:
                top -= 20
            elif self.fx==pygame.K_DOWN:
                top+=20
            node=pygame.Rect(left,top,20,20)
            self.body.insert(0,node)
    def del_node(self):
        if self.body:
            self.body.pop()
    def move(self):
        self.del_node()
        self.add_node()
    def change(self,fx):
        LR=[pygame.K_LEFT, pygame.K_RIGHT]
        UD=[pygame.K_UP, pygame.K_DOWN]
        if fx in LR+UD:
            if fx in LR and self.fx in LR:
                return
            if fx in UD and self.fx in UD:
                return
            self.fx=fx
    def is_dead(self):
        if self.body[0].left not in range(WIDTH+1):
            return True
        if self.body[0].top not in range(HEIGHT+1):
            return True
        if self.body[0]  in self.body[1:]:
            return True
class Food:
    def __init__(self):
        self.node=pygame.Rect(60,80,20,20)
        self.flag=False
    def set(self):
        all_x_point=range(20,WIDTH-20,20)
        all_y_point=range(20,HEIGHT-20,20)
        left=random.choice(all_x_point)
        top=random.choice(all_y_point)
        self.node=pygame.Rect(left,top,20,20)
        self.flag=False
    def reset(self):
        self.flag=True
def show_text(screen, pos, text, color, font_bold = False, font_size = 60,font_italic = False):
    #获取系统字体,并设置文字大小
    cur_font = pygame.font.SysFont('幼圆', font_size)
    ##设置是否加粗属性
    cur_font.set_bold(font_bold)
    ##设置是否斜体属性
    cur_font.set_italic(font_italic)
    ##设置文字内容
    text_fmt = cur_font.render(text, 1, color)
    #绘制文字
    screen.blit(text_fmt, pos)

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH,HEIGHT]) #创建一个窗口
    clock = pygame.time.Clock()
    sk=Snake(screen)
    fd=Food()
    dead=False #标识蛇是否是死亡的
    while True:
        for e in pygame.event.get():  #获取事件
            if e.type == pygame.QUIT:
                pygame.quit()
                #sys.exit()
            if e.type == pygame.KEYDOWN:
                sk.change(e.key)
                if e.key == pygame.K_SPACE:
                    sk=Snake(screen)
                    fd=Food()
                    dead=False
        screen.fill((255,255,255))
        #画蛇
        sk.draw_snake()
        #蛇移动
        if not dead:
            sk.move()
        #判断是否死亡
        if sk.is_dead():
            show_text(screen, (75,250), "Game Over", (202,92,85),True,100)
            show_text(screen,(180,500),"按 空格 重新开始!",(116,181,103),False,30)
            dead=True
        #放食物
        if fd.flag:
            fd.set()
        pygame.draw.rect(screen,(231,175,95),fd.node,0)
        #吃食物
        if fd.node==sk.body[0]:
            sk.add_node()
            fd.reset()
        pygame.display.update()
        clock.tick(10)
        # sleep(0.1)
if __name__ == '__main__':
    main()

#查询支持的中文
# import pygame
# print(pygame.font.get_fonts()) 获取所有字体