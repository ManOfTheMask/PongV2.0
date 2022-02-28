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
        
#create objects
paddle1 = Paddles(100, 240, 10, 60)
paddle2 = Paddles(565, 240, 10, 60)

#event method
def Events():
    global IsOpen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IsOpen = False
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