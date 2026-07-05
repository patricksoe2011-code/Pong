import pygame as py
import random as rd

py.init() 
clock = py.time.Clock()

#rectangle
class rectangle():

    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def make_rect(self):
        self.rectangle = py.rect.Rect(self.x,self.y,self.width,self.height)

    def draw(self):
        py.draw.rect(screen,self.color,self.rectangle)

# screen
w = 1200
l = 800
r = 0
g = 0
b = 0

screen = py.display.set_mode((w,l))
screen.fill((r,g,b))
py.display.flip()

# text
font = py.font.Font("font.ttf", 100)

txt1x = 275
txt1y = 20
text1 = font.render("0", True, (255,255,255))
screen.blit(text1,(txt1x,txt1y))

txt2x = 875
txt2y = 20
text2 = font.render("0", True, (255,255,255))
screen.blit(text2,(txt2x,txt2y))

#rectangle shape
rect1 = rectangle(50,325,30,150,(255,255,255))
rect1.make_rect()
rect1.draw()

#rectangle 2 shape
rect2 = rectangle(1120,325,30,150,(255,255,255))
rect2.make_rect()
rect2.draw()

#border
top_border = rectangle(0,-10,w,10,(255,255,255))
top_border.make_rect()
top_border.draw()

bottom_border = rectangle(0,l+10,w,10,(255,255,255))
bottom_border.make_rect()
bottom_border.draw()

#goals
left_goal = rectangle(-10,0,10,l,(255,255,255))
left_goal.make_rect()
left_goal.draw()

right_goal = rectangle(w,0,10,l,(255,255,255))
right_goal.make_rect()
right_goal.draw()

#line
thickness = 4
line = rectangle(600-thickness//2,0,thickness,l,(255,255,255))
line.make_rect()
line.draw()

#ball
ball = rectangle(600,400,20,20,(255,255,255))
ball.make_rect()
ball.draw()

start_ball_speed = 5
ball.dx = rd.choice([-start_ball_speed, start_ball_speed])
ball.dy = rd.choice([-start_ball_speed, start_ball_speed])

#game loop
pressed = False
running = True
clicked = False

while running:
    
    for event in py.event.get():
        if event.type == py.QUIT or (event.type == py.KEYDOWN and event.key == py.K_ESCAPE):
            running = False

    keys = py.key.get_pressed()
    if keys[py.K_w]:
        rect1.rectangle.y -= 10
    if keys[py.K_s]:
        rect1.rectangle.y += 10

    if keys[py.K_UP] or keys[py.K_i]:
        rect2.rectangle.y -= 10
    if keys[py.K_DOWN] or keys[py.K_k]:
        rect2.rectangle.y += 10

    if py.Rect.colliderect(rect1.rectangle,top_border.rectangle):
        rect1.rectangle.y += 10

    if py.Rect.colliderect(rect2.rectangle,top_border.rectangle):
        rect2.rectangle.y += 10

    if py.Rect.colliderect(rect1.rectangle,bottom_border.rectangle):
        rect1.rectangle.y -= 10

    if py.Rect.colliderect(rect2.rectangle,bottom_border.rectangle):
        rect2.rectangle.y -= 10

    screen.fill((r,g,b))
    screen.blit(text1,(txt1x,txt1y))
    screen.blit(text2,(txt2x,txt2y))
    rect1.draw()
    rect2.draw()
    top_border.draw()
    bottom_border.draw()
    left_goal.draw()
    right_goal.draw()
    line.draw()
    ball.draw()
    clock.tick(60)
    py.display.update()
