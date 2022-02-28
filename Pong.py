#TODO add all object classes, add all object functions, figure out how to put this game all together
#note pygame local docs cmd python -m pygame.docs 
import pygame

pygame.init()

# global variables
ScreenWidth = 640
ScreenHeight = 480

IsOpen = True
FPS = 200


window = pygame.display.set_mode((ScreenWidth, ScreenHeight))
clock = pygame.time.Clock()

#paddle class
class Paddles:
    def __init__(self, xcoord, ycoord, width, height):
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.width = width
        self.height = height
        
    def RenderPaddle(self):
        # x, y, width, height
         pygame.draw.rect(window, (255, 255, 255), pygame.Rect(self.xcoord, self.ycoord, self.width, self.height))

    def MovePaddle(self, PaddleUp=False, PaddleDown=False):
        # control the paddles
        if PaddleUp:
            self.ycoord += 1
        if PaddleDown:
            self.ycoord -= 1
        if self.ycoord > ScreenHeight - 50:
            self.ycoord = ScreenHeight - 50
        if self.ycoord < 0:
                self.ycoord = 0
        
#create objects
paddle1 = Paddles(50, 240, 10, 60)
paddle2 = Paddles(500, 240, 10, 60)

#event method
def Events():
    global IsOpen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IsOpen = False
    
    # control the paddles
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddle1.MovePaddle(True)
            if event.key == pygame.K_DOWN:
                paddle1.MovePaddle(False, True)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP :
                paddle1.MovePaddle()
            if event.key == pygame.K_DOWN:
                paddle1.MovePaddle()
#render method
def Render():
    window.fill((0, 0, 0))
    paddle1.RenderPaddle()
    paddle2.RenderPaddle()
    pygame.display.update()

#game loop
while IsOpen:
    clock.tick(FPS)
    Events()
    Render()
pygame.quit()