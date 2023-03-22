import pygame
import sys

pygame.init()

screen=pygame.display.set_mode((1000,1000))
pygame.display.set_caption("TankGame")



walkright2=pygame.image.load('танквправо2.png')
walkleft2=pygame.image.load('танквлево2.png')
walkup2=pygame.image.load('танквверх2.png')
walkdown2=pygame.image.load('танквниз2.png')
walkStand2=pygame.image.load('танквверх2.png')

bg=pygame.image.load('задний фон1.png')



playerx2=100
playery2=100

speed=3
wusota=50
hirina=50

blue=(0,0,255)
red=(255,0,0)



left2=False
right2=False
up2=False
down2=False
animcount2=0
lastmove2="вправо"

clock=pygame.time.Clock()

class snaryad2():
      def __init__(self,x2,y2,radius2,color2,facingx2,facingy2):
            self.x2=x2
            self.y2=y2
            self.radius2    =radius2
            self.color2 =color2
            self.facingx2 = facingx2
            self.facingy2 = facingy2
            self.velx2=10*facingx2
            self.vely2 = 10 * facingy2
      def draw(self,screen):
            pygame.draw.circle(screen,self.color2,(self.x2,self.y2),self.radius2)


def drawwindow2():
      global animcount2
      global walkStand2
      screen.blit(bg, (0, 0))

      if animcount2+1>=30:
            animcount2=0

      if left2:
            screen.blit(walkleft2,(playerx2,playery2))
            walkStand2=pygame.image.load('танквлево2.png')
      elif right2:
            screen.blit(walkright2,(playerx2,playery2))
            walkStand2 = pygame.image.load('танквправо2.png')
      elif up2:
            screen.blit(walkup2,(playerx2,playery2))
            walkStand2 = pygame.image.load('танквверх2.png')
      elif down2:
            screen.blit(walkdown2,(playerx2,playery2))
            walkStand2 = pygame.image.load('танквниз2.png')
      else:
            screen.blit(walkStand2,(playerx2,playery2))
      for bullet2 in bullets2:
            bullet2.draw(screen)

      pygame.display.update()





bullets2=[]
while True:
      clock.tick(20)


      for event in pygame.event.get():
            if event.type==pygame.QUIT:
                  pygame.quit()
                  sys.exit()

      for bullet2 in bullets2:
            if bullet2.x2<1000 and bullet2.x2>0:
                  bullet2.x2+=bullet2.velx2
            else:
                  bullets2.pop(bullets2.index(bullet2))
            if bullet2.y2<1000 and bullet2.y2>0:
                  bullet2.y2 += bullet2.vely2
            else:
                  bullets2.pop(bullets2.index(bullet2))


      keys1=pygame.key.get_pressed()
      keys2 = pygame.key.get_pressed()

      if keys2[pygame.K_SPACE]:
            if lastmove2 =="вправо":
                  facingx2 =1
                  facingy2=0
            elif lastmove2 =="влево":
                  facingx2 =-1
                  facingy2=0
            elif lastmove2 =="вверх":
                  facingx2 =0
                  facingy2 = -1
            else:
                  lastmove2 == "вниз"
                  facingx2 = 0
                  facingy2 = 1

            if len(bullets2)<1:
                  bullets2.append(snaryad2(round(playerx2+hirina//2),
                                 (round(playery2+wusota//2)),
                                  5,red,facingx2,facingy2))



      if keys2[pygame.K_a] and playerx2>=10:
            playerx2-=speed
            left2=True
            right2=False
            up2  =False
            down2=False
            lastmove2    = "влево"
      elif keys2[pygame.K_d] and playerx2<=940:
            playerx2+=speed
            left2 = False
            right2 = True
            up2 = False
            down2 = False
            lastmove2       = "вправо"
      elif keys2[pygame.K_w] and playery2>=10:
            playery2-=speed
            up2=True
            down2 =False
            left2 = False
            right2 = False
            lastmove2 = "вверх"
      elif keys2[pygame.K_s] and playery2<=940:
            playery2+=speed
            up2 = False
            down2 = True
            left2 = False
            right2 = False
            lastmove2    = "вниз"


      else:
            left2=False
            right2 = False
            up2 = False
            down2 = False
            animcount2   = 0


      drawwindow2()