import pygame
import sys

pygame.init()

screen=pygame.display.set_mode((1000,1000))
pygame.display.set_caption("TankGame")

walkright1=pygame.image.load('танквправо1.png')
walkleft1=pygame.image.load('танквлево1.png')
walkup1=pygame.image.load('танквверх1.png')
walkdown1=pygame.image.load('танквниз1.png')
walkStand1=pygame.image.load('танквверх1.png')



bg=pygame.image.load('задний фон1.png')

playerx=900
playery=900



speed=3
wusota=50
hirina=50

blue=(0,0,255)
red=(255,0,0)

left1=False
right1=False
up1=False
down1=False
animcount1=0
lastmove1="вправо"



clock=pygame.time.Clock()

class snaryad():
      def __init__(self,x,y,radius,color,facingx,facingy):
            self.x=x
            self.y=y
            self.radius=radius
            self.color=color
            self.facingx = facingx
            self.facingy = facingy
            self.velx=10*facingx
            self.vely = 10 * facingy
      def draw(self,screen):
            pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)


def drawwindow1():
      global animcount1
      global walkStand1
      screen.blit(bg, (0, 0))

      if animcount1+1>=30:
            animcount1=0

      if left1:
            screen.blit(walkleft1,(playerx,playery))
            walkStand1=pygame.image.load('танквлево1.png')
      elif right1:
            screen.blit(walkright1,(playerx,playery))
            walkStand1 = pygame.image.load('танквправо1.png')
      elif up1:
            screen.blit(walkup1,(playerx,playery))
            walkStand1 = pygame.image.load('танквверх1.png')
      elif down1:
            screen.blit(walkdown1,(playerx,playery))
            walkStand1 = pygame.image.load('танквниз1.png')
      else:
            screen.blit(walkStand1,(playerx,playery))
      for bullet in bullets:
            bullet.draw(screen)

      pygame.display.update()





bullets=[]
while True:
      clock.tick(20)


      for event in pygame.event.get():
            if event.type==pygame.QUIT:
                  pygame.quit()
                  sys.exit()

      for bullet in bullets:
            if bullet.x<1000 and bullet.x>0:
                  bullet.x+=bullet.velx
            else:
                  bullets.pop(bullets.index(bullet))
            if bullet.y<1000 and bullet.y>0:
                  bullet.y += bullet.vely
            else:
                  bullets.pop(bullets.index(bullet))


      keys=pygame.key.get_pressed()

      if event.type==pygame.MOUSEBUTTONDOWN:
            if lastmove1 =="вправо":
                  facingx =1
                  facingy=0
            elif lastmove1 =="влево":
                  facingx =-1
                  facingy=0
            elif lastmove1 =="вверх":
                  facingx =0
                  facingy = -1
            else:
                  lastmove1 == "вниз"
                  facingx = 0
                  facingy = 1

            if len(bullets)<1:
                  bullets.append(snaryad(round(playerx+hirina//2),
                                 (round(playery+wusota//2)),
                                  5,red,facingx,facingy))



      if keys[pygame.K_LEFT] and playerx>=10:
            playerx-=speed
            left1=True
            right1=False
            up1  =False
            down1=False
            lastmove1    = "влево"
      elif keys[pygame.K_RIGHT] and playerx<=940:
            playerx+=speed
            left1 = False
            right1 = True
            up1 = False
            down1 = False
            lastmove1    = "вправо"
      elif keys[pygame.K_UP] and playery>=10:
            playery-=speed
            up1=True
            down1=False
            left1 = False
            right1 = False
            lastmove1 = "вверх"
      elif keys[pygame.K_DOWN] and playery<=940:
            playery+=speed
            up1 = False
            down1 = True
            left1 = False
            right1 = False
            lastmove1    = "вниз"


      else:
            left1=False
            right1 = False
            up1 = False
            down1 = False
            animcount1 = 0


      drawwindow1()










