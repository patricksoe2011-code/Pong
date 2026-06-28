import pygame as py

py.init() 

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
w = 1500
l = 900
r = 0
g = 0
b = 0

screen = py.display.set_mode((w,l))
screen.fill((r,g,b))
py.display.flip()

# text
font = py.font.SysFont("Times New Roman",20)

text = font.render("idk", True, (255,0,255))
screen.blit(text,(100,100))

#rectangle shape
rect1 = rectangle(100,200,100,100,(0,255,0))
rect1.make_rect()
rect1.draw()

#ellipse shape


#insert image


#collision
def check_collision(shape1,shape2):
    ##somehow make both shapes have same class
    if py.Rect.colliderect(shape1.rectangle,shape2.ellipse):
        print("collide")
        return

#game loop
pressed = False
running = True
clicked = False
while running:
    
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    if event.type == py.KEYDOWN and pressed == False:

        pressed = True

        if event.key == py.K_LEFT:
            print("left arrow pressed")
            rect1.rectangle.move_ip(-50,0)
            
        if event.key == py.K_RIGHT:
            print("right arrow pressed")
            rect1.rectangle.move_ip(50,0)

        if event.key == py.K_UP:
            print("up arrow pressed")
            rect1.rectangle.move_ip(0,-50)

        if event.key == py.K_DOWN:
            print("down arrow pressed")
            rect1.rectangle.move_ip(0,50)

    elif event.type == py.KEYUP:
        pressed = False
    
    if event.type == py.MOUSEBUTTONDOWN and clicked == False:
        clicked = True
        print("clicked")
        print(py.mouse.get_pos())

        if rect1.rectangle.collidepoint(py.mouse.get_pos()):
            rect1.rectangle.scale_by_ip(1.5,3)
    elif event.type == py.MOUSEBUTTONUP:
        clicked = False

    screen.fill((r,g,b))
    screen.blit(text,(100,100))
    rect1.draw()
    py.display.update()
