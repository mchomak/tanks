import pygame
import sys
import random
import pygame_menu
import time

pygame.init()

screen=pygame.display.set_mode((1500,1000))
pygame.display.set_caption("TankGame")

walkright1=pygame.image.load('танквправо1.png')
walkleft1=pygame.image.load('танквлево1.png')
walkup1=pygame.image.load('танквверх1.png')
walkdown1=pygame.image.load('танквниз1.png')
walkStand1=pygame.image.load('танквверх1.png')

walkright2=pygame.image.load('танквправо2.png')
walkleft2=pygame.image.load('танквлево2.png')
walkup2=pygame.image.load('танквверх2.png')
walkdown2=pygame.image.load('танквниз2.png')
walkStand2=pygame.image.load('танквверх2.png')




box_damage=pygame.image.load('коробка с уроном.png')
box_healse=pygame.image.load('коробка с сердцем.png')
box_speed=pygame.image.load('коробка скорость.png')
heart=pygame.image.load('сердечко.png')
speed=pygame.image.load('скорость.png')
damage=pygame.image.load('меч.png')

bg=pygame.image.load('задний фон2.png')
bg_menu=pygame.image.load('задний фон меню.png')
bg_controls=pygame.image.load('меню управления.png')

courier=pygame.font.SysFont('courier',36)

playerx2=300
playery2=300
speed2=4
heals2=10
damage2=1

playerx=800
playery=800
speed1=4
heals1=10
damage1=1

box_damageX,box_damageY=50,50
box_healseX,box_healseY=100,100
box_speedX,box_speedY=200,200
heartx1=50
heartx2=800


wusota=50
hirina=50

blue=(0,0,255)
red=(255,0,0)
header_color=(0,204,153)
white=(255,255,255)

left1=False
right1=False
up1=False
down1=False
animcount1=0
lastmove1="вправо"

left2=False
right2=False
up2=False
down2=False
animcount2=0
lastmove2="вправо"
distanse=0

clock=pygame.time.Clock()

def set_difficulty(value, difficulty):
    global distanse
    if difficulty==1:
        distanse=0
    else:
        distanse=100
class snaryad():
    def __init__(self, x, y, radius, color, facingx, facingy):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facingx = facingx
        self.facingy = facingy
        self.velx = 10 * facingx
        self.vely = 10 * facingy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class snaryad2():
    def __init__(self, x2, y2, radius2, color2, facingx2, facingy2):
        self.x2 = x2
        self.y2 = y2
        self.radius2 = radius2
        self.color2 = color2
        self.facingx2 = facingx2
        self.facingy2 = facingy2
        self.velx2 = 10 * facingx2
        self.vely2 = 10 * facingy2

    def draw(self, screen):
        pygame.draw.circle(screen, self.color2, (self.x2, self.y2), self.radius2)


def random_box_damage():
    global box_damageX
    global box_damageY
    box_damageX = random.randint(10,1490 )
    box_damageY = random.randint(160,990 )

def random_box_healse():
    global box_healseX
    global box_healseY
    box_healseX = random.randint(10,1490  )
    box_healseY = random.randint(160,990  )

def random_box_speed():
    global box_speedX
    global box_speedY
    box_speedX = random.randint(10,1490 )
    box_speedY = random.randint(160,990 )

def controls():
    while True:
        time.sleep(3)
        screen.blit(bg_controls, (0, 0))
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_ESCAPE]:
    #     screen.blit(bg_controls, (0, 0))


def drawwindow():
    global heartx
    pygame.draw.rect(screen, header_color, [0, 0, 1500, 150, ])

    text_heals1 = courier.render(f":{heals1}", 0, white)
    text_speed1 = courier.render(f":{speed1}", 0, white)
    text_damage1 = courier.render(f":{damage1}", 0, white)
    screen.blit(text_heals1, (100, 2))
    screen.blit(text_speed1, (100, 52))
    screen.blit(text_damage1, (100, 102))

    screen.blit(heart, (50, 2))
    screen.blit(speed, (50, 52))
    screen.blit(damage, (50, 102))
    screen.blit(walkup1, (400, 2))

    text_heals2 = courier.render(f":{heals2}", 0, white)
    text_speed2 = courier.render(f":{speed2}", 0, white)
    text_damage2 = courier.render(f":{damage2}", 0, white)

    screen.blit(text_heals2, (850, 2))
    screen.blit(text_speed2, (850, 52))
    screen.blit(text_damage2, (850, 102))

    screen.blit(heart, (800, 2))
    screen.blit(speed, (800, 52))
    screen.blit(damage, (800, 102))
    screen.blit(walkup2, (1100, 2))

    screen.blit(box_damage,(box_damageX,box_damageY))
    screen.blit(box_healse,(box_healseX,box_healseY))
    screen.blit(box_speed,(box_speedX,box_speedY))


def drawwindow1():
    global animcount1
    global walkStand1



    if animcount1 + 1 >= 30:
        animcount1 = 0

    if left1:
        screen.blit(walkleft1, (playerx, playery))
        walkStand1 = pygame.image.load('танквлево1.png')
    elif right1:
        screen.blit(walkright1, (playerx, playery))
        walkStand1 = pygame.image.load('танквправо1.png')
    elif up1:
        screen.blit(walkup1, (playerx, playery))
        walkStand1 = pygame.image.load('танквверх1.png')
    elif down1:
        screen.blit(walkdown1, (playerx, playery))
        walkStand1 = pygame.image.load('танквниз1.png')
    else:
        screen.blit(walkStand1, (playerx, playery))




bullets=[]
bullets2=[]

def drawwindow2():
    global animcount2
    global walkStand2



    if animcount2 + 1 >= 30:
        animcount2 = 0

    if left2:
        screen.blit(walkleft2, (playerx2, playery2))
        walkStand2 = pygame.image.load('танквлево2.png')
    elif right2:
        screen.blit(walkright2, (playerx2, playery2))
        walkStand2 = pygame.image.load('танквправо2.png')
    elif up2:
        screen.blit(walkup2, (playerx2, playery2))
        walkStand2 = pygame.image.load('танквверх2.png')
    elif down2:
        screen.blit(walkdown2, (playerx2, playery2))
        walkStand2 = pygame.image.load('танквниз2.png')
    else:
        screen.blit(walkStand2, (playerx2, playery2))

def start_the_game():

    global playery2
    global playerx2
    global playery
    global playerx
    global left1
    global right1
    global up1
    global down1
    global animcount1
    global left2
    global right2
    global up2
    global down2
    global animcount2
    global heals1
    global heals2
    global lastmove1
    global damage1
    global lastmove2
    global damage2
    global speed1
    global speed2
    global distanse
    playerx2 = 300
    playery2 = 300
    speed2 = 4
    heals2 = 10
    damage2 = 1

    playerx = 800
    playery = 800
    speed1 = 4
    heals1 = 10
    damage1 = 1
    random_box_damage()
    random_box_healse()
    random_box_speed()
    while True:
        keys = pygame.key.get_pressed()

        clock.tick(40)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        if heals1<=0 or heals2<=0:
            break
        if keys[pygame.K_ESCAPE]:
            break


        for bullet in bullets:
                if bullet.x<1500 and bullet.x>0:
                      bullet.x+=bullet.velx
                else:
                      bullets.pop(bullets.index(bullet))
                if bullet.y<1000 and bullet.y>150:
                      bullet.y += bullet.vely
                else:
                      bullets.pop(bullets.index(bullet))

                if lastmove1 == 'вправо' or lastmove1 == 'вверх':
                    if (playery2<=bullet.y and bullet.y<=playery2+50) and (playerx2<=bullet.x and bullet.x<=playerx2+50):
                        bullets.pop(bullets.index(bullet))
                        heals2 = heals2 - damage1
                        print('жизни второго игрока', heals2)
                elif lastmove1 == 'влево' or lastmove1 == 'вниз':
                    if (playery2<=bullet.y and bullet.y<=playery2+50) and (playerx2+50>=bullet.x and bullet.x>=playerx2):
                        bullets.pop(bullets.index(bullet))
                        heals2 = heals2 - damage1
                        print('жизни второго игрока', heals2)
                else:
                    pass


        for bullet2 in bullets2:
               if bullet2.x2 < 1500 and bullet2.x2 > 0:
                    bullet2.x2 += bullet2.velx2
               else:
                    bullets2.pop(bullets2.index(bullet2))
               if bullet2.y2 < 1000 and bullet2.y2 > 150:
                    bullet2.y2 += bullet2.vely2
               else:
                    bullets2.pop(bullets2.index(bullet2))

               if lastmove2=='вправо' or lastmove2 == 'вверх':
                    if (playery<=bullet2.y2 and bullet2.y2<=playery+50) and (playerx<=bullet2.x2 and bullet2.x2<=playerx+50):
                        bullets2.pop(bullets2.index(bullet2))
                        heals1 = heals1 - damage2
                        print('жизни первого игрока', heals1)
               elif lastmove2=='влево' or lastmove2 == 'вниз':
                    if (playery<=bullet2.y2 and bullet2.y2<=playery+50) and (playerx+50>=bullet2.x2 and bullet2.x2>=playerx):
                        bullets2.pop(bullets2.index(bullet2))
                        heals1=heals1-damage2
                        print('жизни первого игрока',heals1)
               else:
                   pass


        if keys[pygame.K_SPACE]:
                if lastmove2 == "вправо":
                        facingx2 = 1
                        facingy2 = 0
                elif lastmove2 == "влево":
                        facingx2 = -1
                        facingy2 = 0
                elif lastmove2 == "вверх":
                        facingx2 = 0
                        facingy2 = -1
                else:
                    lastmove2 == "вниз"
                    facingx2 = 0
                    facingy2 = 1


                if len(bullets2)<1:
                      bullets2.append(snaryad2(round(playerx2+hirina//2),
                                     (round(playery2+wusota//2)),
                                      5,red,facingx2,facingy2))

        if (playerx<=playerx2 and playerx2<=playerx+50) or (playerx<=playerx2+50 and playerx2+50<=playerx+50):
            if playery2<=playery:
                lastmove2 == "вверх"
                facingx1 = 0
                facingy1 = -1
                up1 = True
                if len(bullets) < 1:
                    bullets.append(snaryad(round(playerx + hirina // 2),
                                         (round(playery + wusota // 2)),
                                         5, red, facingx1, facingy1))

        if (playerx2 <= playerx <= playerx2 + 50) or (playerx2 <= playerx + 50 <= playerx2 + 50):
            if playery >= playery:
                lastmove1 == "вниз"
                facingx1 = 0
                facingy1 = 1
                down1 = True
                if len(bullets) < 1:
                    bullets.append(snaryad(round(playerx + hirina // 2),
                                         (round(playery + wusota // 2)),
                                         5, red, facingx1, facingy1))

        if (playery2<=playery<=playery2+50) or (playery2<=playery+50<=playery2+50):
            if playerx<=playerx2:
                lastmove1 =="вправо"
                facingx1 =1
                facingy1=0
                right1 = True
                if len(bullets) < 1:
                    bullets.append(snaryad(round(playerx + hirina // 2),
                                         (round(playery + wusota // 2)),
                                         5, red, facingx1, facingy1))

        if (playery2 <= playery <= playery2 + 50) or (playery2 <= playery + 50 <= playery2 + 50):
            if playerx >= playerx2:
                lastmove1 == "влево"
                facingx1 = -1
                facingy1 = 0
                left1 = True
                if len(bullets) < 1:
                    bullets.append(snaryad(round(playerx + hirina // 2),
                                         (round(playery + wusota // 2)),
                                         5, red, facingx1, facingy1))



        if keys[pygame.K_a] and playerx2 >= 10:
              if abs(playerx2-playerx)<50 and abs(playery2-playery)<50 and lastmove2 =="влево":
                  pass
              else:
                  playerx2 -= speed2
                  left2 = True
                  right2 = False
                  up2 = False
                  down2 = False
                  lastmove2 = "влево"
              if ((playerx2 <= box_damageX and box_damageX <= playerx2 + 50) or (
                          playerx2 <= box_damageX + 20 and box_damageX + 20 <= playerx2 + 50)) and ((
                                                        playery2 <= box_damageY and box_damageY <= playery2 + 50) or (
                                                        playery2 <= box_damageY + 20 and box_damageY + 20 <= playery2 + 50)):
                      damage1 = damage1 + 1
                      random_box_damage()

              if ((playerx2 <= box_healseX and box_healseX <= playerx2 + 50) or (
                          playerx2 <= box_healseX + 20 and box_healseX + 20 <= playerx2 + 50)) and ((
                                                        playery2 <= box_healseY and box_healseY <= playery2 + 50) or (
                                                        playery2 <= box_healseY + 20 and box_healseY + 20 <= playery2 + 50)):
                      if heals1 < 10:
                          heals1 = heals1 + 1
                          random_box_healse()

              if ((playerx2 <= box_speedX and box_speedX <= playerx2 + 50) or (
                          playerx2 <= box_speedX + 20 and box_speedX + 20 <= playerx2 + 50)) and ((
                                                            playery2 <= box_speedY and box_speedY <= playery2 + 50) or (
                                                            playery2 <= box_speedY + 20 and box_speedY + 20 <= playery2 + 50)):
                      speed1 = speed1 + 1
                      random_box_speed()
        elif keys[pygame.K_d] and playerx2 <= 1440:
              if abs(playerx2-playerx)<50 and abs(playery2-playery)<50 and lastmove2 == "вправо":
                  pass
              else:
                  playerx2 += speed2
                  left2 = False
                  right2 = True
                  up2 = False
                  down2 = False
                  lastmove2 = "вправо"
              if (playerx2 <= box_damageX and box_damageX <= playerx2 + 50) and (
                      playery2 <= box_damageY and box_damageY <= playery2 + 50):
                  damage2 = damage2 + 1
                  random_box_damage()

              if (playerx2 <= box_healseX and box_healseX <= playerx2 + 50) and (
                      playery2 <= box_healseY and box_healseY <= playery2 + 50):
                  if heals2<10:
                      heals2 = heals2 + 1
                      random_box_healse()

              if (playerx2 <= box_speedX and box_speedX <= playerx2 + 50) and (
                      playery2 <= box_speedY and box_speedY <= playery2 + 50):
                  speed2 = speed2 + 1
                  random_box_speed()
        elif keys[pygame.K_w] and playery2 >= 160:
              if abs(playery2-playery)<50 and abs(playerx2-playerx)<50 and lastmove2 == "вверх"  :
                  pass
              else:
                  playery2 -= speed2
                  up2 = True
                  down2 = False
                  left2 = False
                  right2 = False
                  lastmove2 = "вверх"
              if (playerx2 <= box_damageX and box_damageX <= playerx2 + 50) and (
                      playery2 <= box_damageY and box_damageY <= playery2 + 50):
                  damage2 = damage2 + 1
                  random_box_damage()

              if (playerx2 <= box_healseX and box_healseX <= playerx2 + 50) and (
                      playery2 <= box_healseY and box_healseY <= playery2 + 50):
                  heals2 = heals2 + 1
                  random_box_healse()

              if (playerx2 <= box_speedX and box_speedX <= playerx2 + 50) and (
                      playery2 <= box_speedY and box_speedY <= playery2 + 50):
                  speed2 = speed2 + 1
                  random_box_speed()

        elif keys[pygame.K_s] and playery2 <= 940:
              if abs(playery2-playery)<50 and abs(playerx2-playerx)<50 and lastmove2 == "вниз"  :
                  pass
              else:
                  playery2 += speed2
                  up2 = False
                  down2 = True
                  left2 = False
                  right2 = False
                  lastmove2 = "вниз"
              if (playerx2 <= box_damageX and box_damageX <= playerx2 + 50) and (
                      playery2 <= box_damageY and box_damageY <= playery2 + 50):
                  damage2 = damage2 + 1
                  random_box_damage()

              if (playerx2 <= box_healseX and box_healseX <= playerx2 + 50) and (
                      playery2 <= box_healseY and box_healseY <= playery2 + 50):
                  heals2 = heals2 + 1
                  random_box_healse()

              if (playerx2 <= box_speedX and box_speedX <= playerx2 + 50) and (
                      playery2 <= box_speedY and box_speedY <= playery2 + 50):
                  speed2 = speed2 + 1
                  random_box_speed()
        else:
              left2 = False
              right2 = False
              up2 = False
              down2 = False
              animcount2 = 0

        distanse = 0
        poiskX=playerx2
        poiskY=playery2
        if heals1<10:
            poiskX=box_healseX
            poiskY=box_healseY
            distanse=0
        if abs(playerx-box_speedX)<=200 and abs(playery-box_speedY)<=200:
            poiskX=box_speedX
            poiskY=box_speedY
        if abs(playerx-box_damageX)<=200 and abs(playery-box_damageY)<=200:
            poiskX=box_damageX
            poiskY=box_damageY

        if poiskX+10<playerx and playerx>=10 and abs(playerx-poiskX)>distanse:
                if abs(playerx-playerx2)<50 and abs(playery-playery2)<50 and lastmove1 =="влево":
                    pass
                else:
                      playerx -= speed1
                      left1 = True
                      right1 = False
                      up1 = False
                      down1 = False
                      lastmove1 = "влево"
                if ((playerx <= box_damageX and box_damageX <= playerx + 50) or (playerx <= box_damageX+20 and box_damageX+20 <= playerx + 50)) and ((
                          playery <= box_damageY and box_damageY <= playery + 50) or (playery <= box_damageY+20 and box_damageY+20 <= playery + 50)):
                      damage1 = damage1 + 1
                      random_box_damage()

                if ((playerx <= box_healseX and box_healseX <= playerx + 50) or (playerx <= box_healseX+20 and box_healseX+20 <= playerx + 50)) and ((
                          playery <= box_healseY and box_healseY <= playery + 50) or (playery <= box_healseY+20 and box_healseY+20 <= playery + 50)):
                    if heals1<10:
                        heals1 = heals1 + 1
                        random_box_healse()

                if ((playerx <= box_speedX and box_speedX <= playerx + 50) or (playerx <= box_speedX+20 and box_speedX+20 <= playerx + 50)) and ((
                          playery <= box_speedY and box_speedY <= playery + 50) or (playery <= box_speedY+20 and box_speedY+20 <= playery + 50)):
                      speed1 = speed1 + 1
                      random_box_speed()

        elif poiskX>playerx and playerx <= 1440 and abs(playerx-poiskX)>distanse:
                  if abs(playerx-playerx2)<50 and abs(playery-playery2)<50 and lastmove1 == "вправо":
                      pass
                  else:
                      playerx += speed1
                      left1 = False
                      right1 = True
                      up1 = False
                      down1 = False
                      lastmove1 = "вправо"
                  if ((playerx <= box_damageX and box_damageX <= playerx + 50) or (playerx <= box_damageX+20 and box_damageX+20 <= playerx + 50)) and ((
                          playery <= box_damageY and box_damageY <= playery + 50) or (playery <= box_damageY+20 and box_damageY+20 <= playery + 50)):
                      damage1 = damage1 + 1
                      random_box_damage()

                  if ((playerx <= box_healseX and box_healseX <= playerx + 50) or (playerx <= box_healseX+20 and box_healseX+20 <= playerx + 50)) and ((
                          playery <= box_healseY and box_healseY <= playery + 50) or (playery <= box_healseY+20 and box_healseY+20 <= playery + 50)):
                      if heals1<10:
                        heals1 = heals1 + 1
                        random_box_healse()

                  if ((playerx <= box_speedX and box_speedX <= playerx + 50) or (playerx <= box_speedX+20 and box_speedX+20 <= playerx + 50)) and ((
                          playery <= box_speedY and box_speedY <= playery + 50) or (playery <= box_speedY+20 and box_speedY+20 <= playery + 50)):
                      speed1 = speed1 + 1
                      random_box_speed()

        elif poiskY+10<playery and playery >= 160 and abs(playery-poiskY)>distanse:
                  if abs(playery-playery2)<50 and abs(playerx-playerx2)<50 and lastmove1 == "вверх"  :
                      pass
                  else:
                      playery -= speed1
                      up1 = True
                      down1 = False
                      left1 = False
                      right1 = False
                      lastmove1 = "вверх"
                  if ((playerx <= box_damageX and box_damageX <= playerx + 50) or (playerx <= box_damageX+20 and box_damageX+20 <= playerx + 50)) and ((
                          playery <= box_damageY and box_damageY <= playery + 50) or (playery <= box_damageY+20 and box_damageY+20 <= playery + 50)):
                      damage1 = damage1 + 1
                      random_box_damage()

                  if ((playerx <= box_healseX and box_healseX <= playerx + 50) or (playerx <= box_healseX+20 and box_healseX+20 <= playerx + 50)) and ((
                          playery <= box_healseY and box_healseY <= playery + 50) or (playery <= box_healseY+20 and box_healseY+20 <= playery + 50)):
                      if heals1<10:
                        heals1 = heals1 + 1
                        random_box_healse()

                  if ((playerx <= box_speedX and box_speedX <= playerx + 50) or (playerx <= box_speedX+20 and box_speedX+20 <= playerx + 50)) and ((
                          playery <= box_speedY and box_speedY <= playery + 50) or (playery <= box_speedY+20 and box_speedY+20 <= playery + 50)):
                      speed1 = speed1 + 1
                      random_box_speed()

        elif poiskY>playery and playery <= 940 and abs(playery-poiskY)>distanse:
                  if abs(playery-playery2)<50 and abs(playerx-playerx2)<50 and lastmove1 == "вниз"  :
                      pass
                  else:
                      playery += speed1
                      up1 = False
                      down1 = True
                      left1 = False
                      right1 = False
                      lastmove1 = "вниз"

                  if ((playerx <= box_damageX and box_damageX <= playerx + 50) or (playerx <= box_damageX+20 and box_damageX+20 <= playerx + 50)) and ((
                          playery <= box_damageY and box_damageY <= playery + 50) or (playery <= box_damageY+20 and box_damageY+20 <= playery + 50)):
                      damage1 = damage1 + 1
                      random_box_damage()

                  if ((playerx <= box_healseX and box_healseX <= playerx + 50) or (playerx <= box_healseX+20 and box_healseX+20 <= playerx + 50)) and ((
                          playery <= box_healseY and box_healseY <= playery + 50) or (playery <= box_healseY+20 and box_healseY+20 <= playery + 50)):
                      if heals1<10:
                        heals1 = heals1 + 1
                        random_box_healse()

                  if ((playerx <= box_speedX and box_speedX <= playerx + 50) or (playerx <= box_speedX+20 and box_speedX+20 <= playerx + 50)) and ((
                          playery <= box_speedY and box_speedY <= playery + 50) or (playery <= box_speedY+20 and box_speedY+20 <= playery + 50)):
                      speed1 = speed1 + 1
                      random_box_speed()
        else:
                left1 = False
                right1 = False
                up1 = False
                down1 = False
                animcount1 = 0


        drawwindow1()
        drawwindow2()
        drawwindow()
        for bullet in bullets:
              bullet.draw(screen)
        for bullet2 in bullets2:
              bullet2.draw(screen)
        pygame.display.update()
        screen.blit(bg, (0, 0))

def start_the_game2():

    global playery2
    global playerx2
    global playery
    global playerx
    global left1
    global right1
    global up1
    global down1
    global animcount1
    global left2
    global right2
    global up2
    global down2
    global animcount2
    global heals1
    global heals2
    global lastmove1
    global damage1
    global lastmove2
    global damage2
    global speed1
    global speed2
    global distanse
    global event
    playerx2 = 300
    playery2 = 300
    speed2 = 4
    heals2 = 10
    damage2 = 1

    playerx = 800
    playery = 800
    speed1 = 4
    heals1 = 10
    damage1 = 1
    random_box_damage()
    random_box_healse()
    random_box_speed()
    while True:
        keys = pygame.key.get_pressed()

        clock.tick(40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if heals1 <= 0 or heals2 <= 0:
            break
        if keys[pygame.K_ESCAPE]:
            break

        for bullet in bullets:
            if bullet.x < 1500 and bullet.x > 0:
                bullet.x += bullet.velx
            else:
                bullets.pop(bullets.index(bullet))
            if bullet.y < 1000 and bullet.y > 150:
                bullet.y += bullet.vely
            else:
                bullets.pop(bullets.index(bullet))

            if lastmove1 == 'вправо' or lastmove1 == 'вверх':
                if (playery2 <= bullet.y and bullet.y <= playery2 + 50) and (
                        playerx2 <= bullet.x and bullet.x <= playerx2 + 50):
                    bullets.pop(bullets.index(bullet))
                    heals2 = heals2 - damage1
                    print('жизни второго игрока', heals2)
            elif lastmove1 == 'влево' or lastmove1 == 'вниз':
                if (playery2 <= bullet.y and bullet.y <= playery2 + 50) and (
                        playerx2 + 50 >= bullet.x and bullet.x >= playerx2):
                    bullets.pop(bullets.index(bullet))
                    heals2 = heals2 - damage1
                    print('жизни второго игрока', heals2)
            else:
                pass

        for bullet2 in bullets2:
            if bullet2.x2 < 1500 and bullet2.x2 > 0:
                bullet2.x2 += bullet2.velx2
            else:
                bullets2.pop(bullets2.index(bullet2))
            if bullet2.y2 < 1000 and bullet2.y2 > 150:
                bullet2.y2 += bullet2.vely2
            else:
                bullets2.pop(bullets2.index(bullet2))

            if lastmove2 == 'вправо' or lastmove2 == 'вверх':
                if (playery <= bullet2.y2 and bullet2.y2 <= playery + 50) and (
                        playerx <= bullet2.x2 and bullet2.x2 <= playerx + 50):
                    bullets2.pop(bullets2.index(bullet2))
                    heals1 = heals1 - damage2
                    print('жизни первого игрока', heals1)
            elif lastmove2 == 'влево' or lastmove2 == 'вниз':
                if (playery <= bullet2.y2 and bullet2.y2 <= playery + 50) and (
                        playerx + 50 >= bullet2.x2 and bullet2.x2 >= playerx):
                    bullets2.pop(bullets2.index(bullet2))
                    heals1 = heals1 - damage2
                    print('жизни первого игрока', heals1)
            else:
                pass


        if keys[pygame.K_KP_ENTER]:
            if lastmove1 == "вправо":
                facingx1 = 1
                facingy1 = 0
            elif lastmove1 == "влево":
                facingx1 = -1
                facingy1 = 0
            elif lastmove1 == "вверх":
                facingx1 = 0
                facingy1 = -1
            else:
                lastmove1 == "вниз"
                facingx1 = 0
                facingy1 = 1

            if len(bullets) < 1:
                bullets.append(snaryad(round(playerx + hirina // 2),
                                       (round(playery + wusota // 2)),
                                       5, red, facingx1, facingy1))

        if keys[pygame.K_SPACE]:
            if lastmove2 == "вправо":
                facingx2 = 1
                facingy2 = 0
            elif lastmove2 == "влево":
                facingx2 = -1
                facingy2 = 0
            elif lastmove2 == "вверх":
                facingx2 = 0
                facingy2 = -1
            else:
                lastmove2 == "вниз"
                facingx2 = 0
                facingy2 = 1

            if len(bullets2) < 1:
                bullets2.append(snaryad2(round(playerx2 + hirina // 2),
                                         (round(playery2 + wusota // 2)),
                                         5, red, facingx2, facingy2))

        if keys[pygame.K_LEFT] and playerx >= 10:
            if abs(playerx - playerx2) < 50 and abs(playery - playery2) < 50 and lastmove1 == "влево":
                pass
            else:
                playerx -= speed1
                left1 = True
                right1 = False
                up1 = False
                down1 = False
                lastmove1 = "влево"
                if ((playerx <= box_damageX and box_damageX <= playerx + 50) or (
                        playerx <= box_damageX + 20 and box_damageX + 20 <= playerx + 50)) and ((
                                                                                                        playery <= box_damageY and box_damageY <= playery + 50) or (
                                                                                                        playery <= box_damageY + 20 and box_damageY + 20 <= playery + 50)):
                    damage1 = damage1 + 1
                    random_box_damage()

                if ((playerx <= box_healseX and box_healseX <= playerx + 50) or (
                        playerx <= box_healseX + 20 and box_healseX + 20 <= playerx + 50)) and ((
                                                                                                        playery <= box_healseY and box_healseY <= playery + 50) or (
                                                                                                        playery <= box_healseY + 20 and box_healseY + 20 <= playery + 50)):
                    if heals1 < 10:
                        heals1 = heals1 + 1
                        random_box_healse()

                if ((playerx <= box_speedX and box_speedX <= playerx + 50) or (
                        playerx <= box_speedX + 20 and box_speedX + 20 <= playerx + 50)) and ((
                                                                                                      playery <= box_speedY and box_speedY <= playery + 50) or (
                                                                                                      playery <= box_speedY + 20 and box_speedY + 20 <= playery + 50)):
                    speed1 = speed1 + 1
                    random_box_speed()

        elif keys[pygame.K_RIGHT] and playerx <= 1440:
            if abs(playerx - playerx2) < 50 and abs(playery - playery2) < 50 and lastmove1 == "вправо":
                pass
            else:
                playerx += speed1
                left1 = False
                right1 = True
                up1 = False
                down1 = False
                lastmove1 = "вправо"
            if ((playerx <= box_damageX and box_damageX <= playerx + 50) or (
                    playerx <= box_damageX + 20 and box_damageX + 20 <= playerx + 50)) and ((
                                                                                                    playery <= box_damageY and box_damageY <= playery + 50) or (
                                                                                                    playery <= box_damageY + 20 and box_damageY + 20 <= playery + 50)):
                damage1 = damage1 + 1
                random_box_damage()

            if ((playerx <= box_healseX and box_healseX <= playerx + 50) or (
                    playerx <= box_healseX + 20 and box_healseX + 20 <= playerx + 50)) and ((
                                                                                                    playery <= box_healseY and box_healseY <= playery + 50) or (
                                                                                                    playery <= box_healseY + 20 and box_healseY + 20 <= playery + 50)):
                if heals1 < 10:
                    heals1 = heals1 + 1
                    random_box_healse()

            if ((playerx <= box_speedX and box_speedX <= playerx + 50) or (
                    playerx <= box_speedX + 20 and box_speedX + 20 <= playerx + 50)) and ((
                                                                                                  playery <= box_speedY and box_speedY <= playery + 50) or (
                                                                                                  playery <= box_speedY + 20 and box_speedY + 20 <= playery + 50)):
                speed1 = speed1 + 1
                random_box_speed()

        elif keys[pygame.K_UP] and playery >= 160:
            if abs(playerx - playerx2) < 50 and abs(playery - playery2) < 50 and lastmove1 == "вверх":
                pass
            else:
                playery -= speed1
                up1 = True
                down1 = False
                left1 = False
                right1 = False
                lastmove1 = "вверх"
            if ((playerx <= box_damageX and box_damageX <= playerx + 50) or (
                    playerx <= box_damageX + 20 and box_damageX + 20 <= playerx + 50)) and ((
                                                                                                    playery <= box_damageY and box_damageY <= playery + 50) or (
                                                                                                    playery <= box_damageY + 20 and box_damageY + 20 <= playery + 50)):
                damage1 = damage1 + 1
                random_box_damage()

            if ((playerx <= box_healseX and box_healseX <= playerx + 50) or (
                    playerx <= box_healseX + 20 and box_healseX + 20 <= playerx + 50)) and ((
                                                                                                    playery <= box_healseY and box_healseY <= playery + 50) or (
                                                                                                    playery <= box_healseY + 20 and box_healseY + 20 <= playery + 50)):
                if heals1 < 10:
                    heals1 = heals1 + 1
                    random_box_healse()

            if ((playerx <= box_speedX and box_speedX <= playerx + 50) or (
                    playerx <= box_speedX + 20 and box_speedX + 20 <= playerx + 50)) and ((
                                                                                                  playery <= box_speedY and box_speedY <= playery + 50) or (
                                                                                                  playery <= box_speedY + 20 and box_speedY + 20 <= playery + 50)):
                speed1 = speed1 + 1
                random_box_speed()


        elif keys[pygame.K_DOWN] and playery <= 940:
            if abs(playerx - playerx2) < 50 and abs(playery - playery2) < 50 and lastmove1 == "вниз":
                pass
            else:
                playery += speed1
                up1 = False
                down1 = True
                left1 = False
                right1 = False
                lastmove1 = "вниз"
            if ((playerx <= box_damageX and box_damageX <= playerx + 50) or (
                    playerx <= box_damageX + 20 and box_damageX + 20 <= playerx + 50)) and ((
                                                                                                    playery <= box_damageY and box_damageY <= playery + 50) or (
                                                                                                    playery <= box_damageY + 20 and box_damageY + 20 <= playery + 50)):
                damage1 = damage1 + 1
                random_box_damage()

            if ((playerx <= box_healseX and box_healseX <= playerx + 50) or (
                    playerx <= box_healseX + 20 and box_healseX + 20 <= playerx + 50)) and ((
                                                                                                    playery <= box_healseY and box_healseY <= playery + 50) or (
                                                                                                    playery <= box_healseY + 20 and box_healseY + 20 <= playery + 50)):
                if heals1 < 10:
                    heals1 = heals1 + 1
                    random_box_healse()

            if ((playerx <= box_speedX and box_speedX <= playerx + 50) or (
                    playerx <= box_speedX + 20 and box_speedX + 20 <= playerx + 50)) and ((
                                                                                                  playery <= box_speedY and box_speedY <= playery + 50) or (
                                                                                                  playery <= box_speedY + 20 and box_speedY + 20 <= playery + 50)):
                speed1 = speed1 + 1
                random_box_speed()



        else:
            left1 = False
            right1 = False
            up1 = False
            down1 = False
            animcount1 = 0

        if keys[pygame.K_a] and playerx2 >= 10:
            if abs(playerx2 - playerx) < 50 and abs(playery2 - playery) < 50 and lastmove2 == "влево":
                pass
            else:
                playerx2 -= speed2
                left2 = True
                right2 = False
                up2 = False
                down2 = False
                lastmove2 = "влево"
                if ((playerx2 <= box_damageX and box_damageX <= playerx2 + 50) or (
                        playerx2 <= box_damageX + 20 and box_damageX + 20 <= playerx2 + 50)) and ((
                                                                                                          playery2 <= box_damageY and box_damageY <= playery2 + 50) or (
                                                                                                          playery2 <= box_damageY + 20 and box_damageY + 20 <= playery2 + 50)):
                    damage1 = damage1 + 1
                    random_box_damage()

                if ((playerx2 <= box_healseX and box_healseX <= playerx2 + 50) or (
                        playerx2 <= box_healseX + 20 and box_healseX + 20 <= playerx2 + 50)) and ((
                                                                                                          playery2 <= box_healseY and box_healseY <= playery2 + 50) or (
                                                                                                          playery2 <= box_healseY + 20 and box_healseY + 20 <= playery2 + 50)):
                    if heals1 < 10:
                        heals1 = heals1 + 1
                        random_box_healse()

                if ((playerx2 <= box_speedX and box_speedX <= playerx2 + 50) or (
                        playerx2 <= box_speedX + 20 and box_speedX + 20 <= playerx2 + 50)) and ((
                                                                                                        playery2 <= box_speedY and box_speedY <= playery2 + 50) or (
                                                                                                        playery2 <= box_speedY + 20 and box_speedY + 20 <= playery2 + 50)):
                    speed1 = speed1 + 1
                    random_box_speed()
        elif keys[pygame.K_d] and playerx2 <= 1440:
            if abs(playerx2 - playerx) < 50 and abs(playery2 - playery) < 50 and lastmove2 == "вправо":
                pass
            else:
                playerx2 += speed2
                left2 = False
                right2 = True
                up2 = False
                down2 = False
                lastmove2 = "вправо"
            if ((playerx2 <= box_damageX and box_damageX <= playerx2 + 50) or (
                    playerx2 <= box_damageX + 20 and box_damageX + 20 <= playerx2 + 50)) and ((
                                                                                                      playery2 <= box_damageY and box_damageY <= playery2 + 50) or (
                                                                                                      playery2 <= box_damageY + 20 and box_damageY + 20 <= playery2 + 50)):
                damage1 = damage1 + 1
                random_box_damage()

            if ((playerx2 <= box_healseX and box_healseX <= playerx2 + 50) or (
                    playerx2 <= box_healseX + 20 and box_healseX + 20 <= playerx2 + 50)) and ((
                                                                                                      playery2 <= box_healseY and box_healseY <= playery2 + 50) or (
                                                                                                      playery2 <= box_healseY + 20 and box_healseY + 20 <= playery2 + 50)):
                if heals1 < 10:
                    heals1 = heals1 + 1
                    random_box_healse()

            if ((playerx2 <= box_speedX and box_speedX <= playerx2 + 50) or (
                    playerx2 <= box_speedX + 20 and box_speedX + 20 <= playerx2 + 50)) and ((
                                                                                                    playery2 <= box_speedY and box_speedY <= playery2 + 50) or (
                                                                                                    playery2 <= box_speedY + 20 and box_speedY + 20 <= playery2 + 50)):
                speed1 = speed1 + 1
                random_box_speed()
        elif keys[pygame.K_w] and playery2 >= 160:
            if abs(playery2 - playery) < 50 and abs(playerx2 - playerx) < 50 and lastmove2 == "вверх":
                pass
            else:
                playery2 -= speed2
                up2 = True
                down2 = False
                left2 = False
                right2 = False
                lastmove2 = "вверх"
            if ((playerx2 <= box_damageX and box_damageX <= playerx2 + 50) or (
                    playerx2 <= box_damageX + 20 and box_damageX + 20 <= playerx2 + 50)) and ((
                                                                                                      playery2 <= box_damageY and box_damageY <= playery2 + 50) or (
                                                                                                      playery2 <= box_damageY + 20 and box_damageY + 20 <= playery2 + 50)):
                damage1 = damage1 + 1
                random_box_damage()

            if ((playerx2 <= box_healseX and box_healseX <= playerx2 + 50) or (
                    playerx2 <= box_healseX + 20 and box_healseX + 20 <= playerx2 + 50)) and ((
                                                                                                      playery2 <= box_healseY and box_healseY <= playery2 + 50) or (
                                                                                                      playery2 <= box_healseY + 20 and box_healseY + 20 <= playery2 + 50)):
                if heals1 < 10:
                    heals1 = heals1 + 1
                    random_box_healse()

            if ((playerx2 <= box_speedX and box_speedX <= playerx2 + 50) or (
                    playerx2 <= box_speedX + 20 and box_speedX + 20 <= playerx2 + 50)) and ((
                                                                                                    playery2 <= box_speedY and box_speedY <= playery2 + 50) or (
                                                                                                    playery2 <= box_speedY + 20 and box_speedY + 20 <= playery2 + 50)):
                speed1 = speed1 + 1
                random_box_speed()
        elif keys[pygame.K_s] and playery2 <= 940:
            if abs(playery2 - playery) < 50 and abs(playerx2 - playerx) < 50 and lastmove2 == "вниз":
                pass
            else:
                playery2 += speed2
                up2 = False
                down2 = True
                left2 = False
                right2 = False
                lastmove2 = "вниз"
            if ((playerx2 <= box_damageX and box_damageX <= playerx2 + 50) or (
                    playerx2 <= box_damageX + 20 and box_damageX + 20 <= playerx2 + 50)) and ((
                                                                                                      playery2 <= box_damageY and box_damageY <= playery2 + 50) or (
                                                                                                      playery2 <= box_damageY + 20 and box_damageY + 20 <= playery2 + 50)):
                damage1 = damage1 + 1
                random_box_damage()

            if ((playerx2 <= box_healseX and box_healseX <= playerx2 + 50) or (
                    playerx2 <= box_healseX + 20 and box_healseX + 20 <= playerx2 + 50)) and ((
                                                                                                      playery2 <= box_healseY and box_healseY <= playery2 + 50) or (
                                                                                                      playery2 <= box_healseY + 20 and box_healseY + 20 <= playery2 + 50)):
                if heals1 < 10:
                    heals1 = heals1 + 1
                    random_box_healse()

            if ((playerx2 <= box_speedX and box_speedX <= playerx2 + 50) or (
                    playerx2 <= box_speedX + 20 and box_speedX + 20 <= playerx2 + 50)) and ((
                                                                                                    playery2 <= box_speedY and box_speedY <= playery2 + 50) or (
                                                                                                    playery2 <= box_speedY + 20 and box_speedY + 20 <= playery2 + 50)):
                speed1 = speed1 + 1
                random_box_speed()


        else:
            left2 = False
            right2 = False
            up2 = False
            down2 = False
            animcount2 = 0

        drawwindow1()
        drawwindow2()
        drawwindow()
        for bullet in bullets:
            bullet.draw(screen)
        for bullet2 in bullets2:
            bullet2.draw(screen)
        pygame.display.update()
        screen.blit(bg, (0, 0))



menu = pygame_menu.Menu(500, 500, 'Welcome',
                            theme=pygame_menu.themes.THEME_BLUE)

menu.add_text_input('Name :', default='Player 1')
# menu.add_selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add_button('1 player', start_the_game)
menu.add_button('2 players', start_the_game2)
menu.add_button('controls', controls)
menu.add_button('Quit', pygame_menu.events.EXIT)

while True:

    screen.blit(bg_menu,(0,0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)

    pygame.display.update()