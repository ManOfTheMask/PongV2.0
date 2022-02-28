#TODO Fix movement, add scoring, add ball and ball physics
#note pygame local docs cmd python -m pygame.docs 
import pygame

pygame.init()

# global variables
ScreenWidth = 640
ScreenHeight = 480

font = pygame.font.Font("ARCADECLASSIC.TTF", 100)

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

    def MovePaddle(self, PaddleDown, PaddleUp):
        global IsOpen
        # control the paddles
        if PaddleDown:
            self.ycoord += 1
        if PaddleUp:
            self.ycoord -= 1

        if self.ycoord > ScreenHeight - 50:
            self.ycoord = ScreenHeight - 50
        if self.ycoord < 0:
            self.ycoord = 0
        
#create objects
paddle1 = Paddles(50, 240, 10, 60)
paddle2 = Paddles(560, 240, 10, 60)

#event method
def Events():
    global IsOpen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IsOpen = False
    # control the paddles
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                paddle1.MovePaddle(False, True)

            elif event.key == pygame.K_DOWN:
                paddle1.MovePaddle(True, False)

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                paddle1.MovePaddle(False, False)

#render method
def Render():
    window.fill((0, 0, 0))
    paddle1.RenderPaddle()
    paddle2.RenderPaddle()
    window.blit(font.render("0", False, (255, 255, 255)), (ScreenWidth - 570, ScreenHeight - 420))
    window.blit(font.render("0", False, (255, 255, 255)), (ScreenWidth - 130, ScreenHeight - 420))
    pygame.display.update()

#game loop
while IsOpen:
    clock.tick(FPS)
    Events()
    Render()
pygame.quit()