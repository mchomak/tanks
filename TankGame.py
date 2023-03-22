import pygame
import sys
import random
import math
import time
pygame.init()
screen=pygame.display.set_mode((1500,1000))
icon =pygame.image.load('игра\icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("TankGame")

def skin_defolt():
    global walkright2,walkleft2,walkup2,walkdown2,skin
    walkright2 = pygame.image.load('танки\танквправо2.png')
    walkleft2 = pygame.image.load('танки\танквлево2.png')
    walkup2 = pygame.image.load('танки\танквверх2.png')
    walkdown2 = pygame.image.load('танки\танквниз2.png')
    skin=defolt_skin2

def skin_firetank():
    global walkright2,walkleft2,walkup2,walkdown2,skin
    walkright2 = pygame.image.load('танки\скин огненный танк вправо.png')
    walkleft2 = pygame.image.load('танки\скин огненный танк влево.png')
    walkup2 = pygame.image.load('танки\скин огненный танк вверх.png')
    walkdown2 = pygame.image.load('танки\скин огненный танк вниз.png')
    skin = firetank_skin

def skin_freeztank():
    global walkright2,walkleft2,walkup2,walkdown2,skin
    walkright2 = pygame.image.load('танки\скин ледянной танк вправо.png')
    walkleft2 = pygame.image.load('танки\скин ледянной танк влево.png')
    walkup2 = pygame.image.load('танки\скин ледянной танк вверх.png')
    walkdown2 = pygame.image.load('танки\скин ледянной танк вниз.png')
    skin = freeztank_skin

def skin_duotank():
    global walkright2, walkleft2, walkup2, walkdown2, skin
    pass
walkright1=pygame.image.load('танки\танквправо1.png')
walkleft1=pygame.image.load('танки\танквлево1.png')
walkup1=pygame.image.load('танки\танквверх1.png')
walkdown1=pygame.image.load('танки\танквниз1.png')
walkStand1=pygame.image.load('танки\танквверх1.png')

freeztank_skin = pygame.image.load('танки\ледяной скин.png')
firetank_skin = pygame.image.load('танки\огненный скин.png')
defolt_skin2 = pygame.image.load('танки\дефолт скин.png')
defolt_skin1 = pygame.image.load('танки\дефолт2.png')
duotank_skin = pygame.image.load('танки\скиг двойной танк.png')
skin=defolt_skin2

sellect_button=pygame.image.load('кнопки\выбрать.png')
left_button=pygame.image.load('кнопки\стрелка влево.png')
right_button=pygame.image.load('кнопки\стрелка вправо.png')
play_button=pygame.image.load('кнопки\играть.png')
player1_button=pygame.image.load('кнопки\один игрок.png')
player2_button=pygame.image.load('кнопки\два игрока.png')
quit_button=pygame.image.load('кнопки\выход.png')
settings_button=pygame.image.load('кнопки\настройки.png')
apgrate_button=pygame.image.load('кнопки\улучшение.png')
menu_batton=pygame.image.load('кнопки\менюшка.png')
magazin_button=pygame.image.load('кнопки\менюшка.png')
buy_button=pygame.image.load('кнопки\купить.png')
easy_button=pygame.image.load('кнопки\легкий.png')
normal_button=pygame.image.load('кнопки\нормально.png')
hard_button=pygame.image.load('кнопки\сложно.png')
company_button=pygame.image.load('кнопки\компания.png')

box_TNT=pygame.image.load('игра\коробка с tnt.png')
box_damage=pygame.image.load('игра\коробка с уроном.png')
box_healse=pygame.image.load('игра\коробка с сердцем.png')
box_speed=pygame.image.load('игра\коробка скорость.png')
heart=pygame.image.load('игра\сердечко.png')
speed=pygame.image.load('игра\скорость.png')
damage=pygame.image.load('игра\меч.png')
money=pygame.image.load('игра\монета.png')
kill=pygame.image.load('игра\череп.png')
kirpichi=pygame.image.load('игра\кирпичи.png')
upgrade_heal=pygame.image.load('игра\прокачка жизни.png')
upgrade_damage=pygame.image.load('игра\прокачка урон.png')
upgrade_speed=pygame.image.load('игра\прокачка скорость.png')
oneheal=pygame.image.load('игра\одна жизнь.png')
onedamage=pygame.image.load('игра\одна урон.png')
onespeed=pygame.image.load('игра\одна скорость.png')

print_start_raund_left=pygame.image.load('игра\надпись в начале боя 1.png')
print_start_raund_right=pygame.image.load('игра\надпись в начале боя 2.png')
print_start_raund=pygame.image.load('игра\надпись в начале боя.png')
bg_menu3=pygame.image.load('игра\задний фон 3.png')
bg_menu2=pygame.image.load('игра\задний фон 2.png')
bg_menu4=pygame.image.load('игра\задний фон 4.png')
bg_menu5=pygame.image.load('игра\задний фон 5.png')
bg_controls=pygame.image.load('игра\меню управления.png')
base_locate=pygame.image.load('игра\основная локация.png')
desert_locate=pygame.image.load('игра\пустыня.png')
forest_locate=pygame.image.load('игра\лес.png')
glade_locate=pygame.image.load('игра\поляна.png')
locate=base_locate

saundON=pygame.image.load('кнопки\звук1.png')
saundOFF=pygame.image.load('кнопки\звук выкл.png')
levelON=pygame.image.load('игра\открытый уровень.png')
levelOFF=pygame.image.load('игра\закрытый уровень.png')

map1=pygame.image.load('игра\карта 1.png')
map2=pygame.image.load('игра\карта 2.png')
map3=pygame.image.load('игра\карта 3.png')

pygame.mixer.music.load('музыка\выстрел.wav')
boom = pygame.mixer.Sound('музыка\выстрел.wav')
pygame.mixer.music.load('музыка\кнопка.wav')
buton = pygame.mixer.Sound('музыка\кнопка.wav')
pygame.mixer.music.load('музыка\основная музыка.wav')
music=pygame.mixer.Sound('музыка\основная музыка.wav')
pygame.mixer.music.load('музыка\пауза.wav')
pauseON = pygame.mixer.Sound('музыка\пауза.wav')
pygame.mixer.music.load('музыка\выключение паузы.wav')
pauseOFF = pygame.mixer.Sound('музыка\выключение паузы.wav')
pygame.mixer.music.load('музыка\авария.wav')
avaria = pygame.mixer.Sound('музыка\авария.wav')
pygame.mixer.music.load('музыка\усиление.wav')
upgrade = pygame.mixer.Sound('музыка\усиление.wav')
pygame.mixer.music.load('музыка\проигрышь.wav')
fail = pygame.mixer.Sound('музыка\проигрышь.wav')
pygame.mixer.music.load('музыка\прохождение игры.wav')
game_complete = pygame.mixer.Sound('музыка\прохождение игры.wav')
pygame.mixer.music.load('музыка\файт.wav')
fight = pygame.mixer.Sound('музыка\файт.wav')
pygame.mixer.music.load('музыка\уровень пройден.wav')
level_complite=pygame.mixer.Sound('музыка\уровень пройден.wav')

BLOCK=pygame.image.load('игра\блок2.png')
music.play(-1)

courier=pygame.font.SysFont('courier',36)
saund=saundON
playerx2=300
playery2=300
speed2=2
heals2=10
damage2=1

moneys1=0
kills1=0

moneys2=0
kills2=0

box_damageX,box_damageY=50,50
box_healseX,box_healseY=100,100
box_speedX,box_speedY=200,200
heartx1=50
heartx2=800

wusota=50
hirina=50
map=0
blue=(0,0,255)
red=(255,0,0)
header_color=(0,204,153)
white=(255,255,255)
black=(0,0,0)
orange=(255,174,1)

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

cost_upgrade_heal=1
cost_upgrade_damage=1
cost_upgrade_speed=1
cost_freeztank_skin=5
cost_firetank_skin=5
cost_duotank_skin=5

skin_number=1
win=0
game_overs=0
companys=0
clock=pygame.time.Clock()
def set_volume(boom_volume,buton_volume,music_volume,pause_volume,avaria_volume,upgrade_volume,fail_volume,game_complete_volume,fight_volume):
    boom.set_volume(boom_volume)
    buton.set_volume(buton_volume)
    music.set_volume(music_volume)
    pauseON.set_volume(pause_volume)
    pauseOFF.set_volume(pause_volume)
    avaria.set_volume(avaria_volume)
    upgrade.set_volume(upgrade_volume)
    fail.set_volume(fail_volume)
    game_complete.set_volume(game_complete_volume)
    fight.set_volume(fight_volume)
    level_complite.set_volume(fail_volume)

set_volume(0.05,1,1,1,1,1,1,1,1)
def save():
    global moneys2, kills2,dop_heals2,dop_speed2,dop_damage2,run_level
    global collect_freeztank_skin,collect_firetank_skin,collect_duotank_skin
    file = open('save_data.txt', 'w')
    file.seek(0)
    buf=str(moneys2)
    file.write(buf)
    file.write(' \n')
    buf=str(kills2)
    file.write(buf)
    file.write(' \n')
    buf = str(collect_freeztank_skin)
    file.write(buf)
    file.write(' \n')
    buf = str(collect_firetank_skin)
    file.write(buf)
    file.write(' \n')
    buf = str(collect_duotank_skin)
    file.write(buf)
    file.write(' \n')
    buf = str(dop_heals2)
    file.write(buf)
    file.write(' \n')
    buf = str(dop_speed2)
    file.write(buf)
    file.write(' \n')
    buf = str(dop_damage2)
    file.write(buf)
    file.write(' \n')
    buf=str(run_level)
    file.write(buf)
    file.write(' \n')

def get_save():
    global moneys2, kills2,dop_heals2,dop_speed2,dop_damage2,run_level
    global collect_freeztank_skin, collect_firetank_skin, collect_duotank_skin
    # 1-moneys,2-kills,3-collect_freeztank_skin,4-collect_firetank_skin,5-collect_duotank_skin
    # 6- ,7- ,8-
    file = open('save_data.txt', 'r')
    buf=file.readline()
    moneys2 = int(buf)
    buf=file.readline()
    kills2 = int(buf)
    buf = file.readline()
    collect_freeztank_skin = int(buf)
    buf = file.readline()
    collect_firetank_skin = int(buf)
    buf = file.readline()
    collect_duotank_skin = int(buf)
    buf = file.readline()
    dop_heals2 = int(buf)
    buf = file.readline()
    dop_speed2 = int(buf)
    buf = file.readline()
    dop_damage2 = int(buf)
    buf=file.readline()
    run_level=int(buf)
x_massive=['1','2','3','4','5','6','7','8',
           '9','10','11','12','13','14','15',
           '16','17','18','19','20','21','22',
           '23','24','25','26','27','28','29','30']

y_massive=['1','2','3','4','5','6','7','8',
           '9','10','11','12','13','14','15',
           '16','17','18','19','20','21']

permissible_x_massive=['0','1','2','3','4','5','6','7','8',
           '9','10','11','12','13','14','15',
           '16','17','18','19','20','21','22',
           '23','24','25','26','27','28','29','30']

permissible_y_massive=['0','1','2','3','4','5','6','7','8',
           '9','10','11','12','13','14','15',
           '16','17','18','19','20','21']

def permissible_massive():
    for block in block_massiv:
        buf_x=block.x/50
        buf_y=block.y/50
        buf_x = math.ceil(buf_x)
        buf_y = math.ceil(buf_y)
        buf_xx = str(buf_x)
        buf_yy = str(buf_y )
        for i in permissible_x_massive:
            if i ==buf_xx:
                permissible_x_massive.remove(buf_xx)

        for f in permissible_y_massive:
            if f == buf_yy:
                permissible_y_massive.remove(buf_yy)

player_rect1=[]
player_rect2=[]
player_rect_left=[]
player_rect_right = []
player_rect_up = []
player_rect_down = []
fps=0

def calculation_rect(poiskX,poiskY):
    global x_rect,y_rect,player_rectx1,player_recty1,player_rectx2,player_recty2,player_rect2
    global player_rect_left,player_rect_right,player_rect_up,player_rect_down
    global player_rect_leftx,player_rect_lefty,player_rect_rightx,player_rect_righty
    global player_rect_upx,player_rect_upy,player_rect_downx,player_rect_downy,x,y
    global go_left11,go_down11,go_right11,go_up11

    buf_playerx=(playerx-2)/50
    buf_playery=(playery-2)/50
    buf_playerx=math.ceil(buf_playerx)
    buf_playery=math.ceil(buf_playery )
    player_rectx1=x_massive[buf_playerx]
    player_recty1 = y_massive[buf_playery]

    buf_playerx2 = (poiskX-2) / 50
    buf_playery2 = (poiskY-2) / 50
    buf_playerx2 = math.ceil(buf_playerx2)
    buf_playery2 = math.ceil(buf_playery2)
    player_rectx2 = x_massive[buf_playerx2 - 1]
    player_recty2 = y_massive[buf_playery2 - 1]

    player_rect1=[]
    player_rect1.append(player_rectx1)
    player_rect1.append(player_recty1)
    player_rectx1=(buf_playerx)*50
    player_recty1=(buf_playery)*50

    player_rect2 = []
    player_rect2.append(player_rectx2)
    player_rect2.append(player_recty2)
    player_rectx2 = (buf_playerx2 - 1) * 50
    player_recty2 = (buf_playery2 - 1) * 50

    player_rect_left = []
    bufx=x_massive[buf_playerx-1]
    bufy=y_massive[buf_playery ]
    bufxx=str(bufx)
    bufyy=str(bufy)
    x = 0
    y = 0
    for i in permissible_x_massive:
        if i==bufxx:
            x=1
    for f in permissible_y_massive:
        if f==bufyy:
            y=1
    if x==1 or y==1:
        player_rect_left.append(bufx)
        player_rect_left.append(bufy)
        go_left11 = 1
    else:
        go_left11=0
    player_rect_leftx = (buf_playerx - 1) * 50
    player_rect_lefty = (buf_playery ) * 50

    player_rect_right = []
    bufx = x_massive[buf_playerx+1 ]
    bufy = y_massive[buf_playery ]
    bufxx = str(bufx)
    bufyy = str(bufy)
    x = 0
    y = 0
    for i in permissible_x_massive:
        if i==bufxx:
            x=1
    for f in permissible_y_massive:
        if f==bufyy:
            y=1
    if x==1 or y==1:
        player_rect_right.append(bufx)
        player_rect_right.append(bufy)
        go_right11 = 1
    else:
        go_right11=0
    player_rect_rightx=(buf_playerx+1)*50
    player_rect_righty = (buf_playery) * 50

    player_rect_up = []
    bufx = x_massive[buf_playerx]
    bufy = y_massive[buf_playery-1 ]
    bufxx = str(bufx)
    bufyy = str(bufy)
    x = 0
    y = 0
    for i in permissible_x_massive:
        if i==bufxx:
            x=1
    for f in permissible_y_massive:
        if f==bufyy:
            y=1
    if x==1 or y==1:
        player_rect_up.append(bufx)
        player_rect_up.append(bufy)
        go_up11 = 1
    else:
        go_up11=0
    player_rect_upx = (buf_playerx) * 50
    player_rect_upy = (buf_playery-1) * 50
    player_rect_up.append(bufx)
    player_rect_up.append(bufy)

    player_rect_down = []
    bufx = x_massive[buf_playerx]
    bufy = y_massive[buf_playery+1]
    bufxx = str(bufx)
    bufyy = str(bufy)
    x = 0
    y = 0
    for i in permissible_x_massive:
        if i==bufxx:
            x=1
    for f in permissible_y_massive:
        if f==bufyy:
            y=1
    if x==1 or y==1:
        player_rect_down.append(bufx)
        player_rect_down.append(bufy)
        go_down11 = 1
    else:
        go_down11=0
    player_rect_downx = (buf_playerx) * 50
    player_rect_downy = (buf_playery+1) * 50

    if poiskX!=playerx2:
        if poiskY!=playery2:
            if abs(poiskX-playerx)<=50 and abs(poiskY-playery)<=50:
                if poiskX-playerx>0:
                    go_right1()
                elif poiskX-playerx<0:
                    go_left1()
                else:
                    pass
                if poiskY-playery>0:
                    go_down1()
                elif poiskY-playery<0:
                    go_up1()
                else:
                    pass

    # print()
    # print(player_rect2,player_rectx2,player_recty2)
    # print(player_rect1,player_rectx1,player_recty1)
    # print(player_rect_left,player_rect_leftx,player_rect_lefty)
    # print(player_rect_right,player_rect_rightx,player_rect_righty)
    # print(player_rect_up,player_rect_upx,player_rect_upy)
    # print(player_rect_down,player_rect_downx,player_rect_downy)

def poisk_wey(poiskX,poiskY):
    global way,buf_poisk
    calculation_rect(poiskX,poiskY)
    distance_left =  10000000
    distance_right = 10000000
    distance_up =    10000000
    distance_down =  10000000

    if go_left11==1:
        bufx=abs(player_rect_leftx-playerx)
        bufy=abs(player_rect_lefty-playery)
        distance_left=bufx+bufy
        bufx=abs(int(player_rect_left[0])-int(player_rect2[0]))+1
        bufy = abs(int(player_rect_left[1]) - int(player_rect2[1]))+1
        distance_left=distance_left+(bufx*50)+(bufy*50)

    if go_right11==1:
        bufx = abs(player_rect_rightx - playerx)
        bufy = abs(player_rect_righty - playery)
        distance_right = bufx + bufy
        bufx = abs(int(player_rect_right[0]) - int(player_rect2[0])) + 1
        bufy = abs(int(player_rect_right[1]) - int(player_rect2[1])) + 1
        distance_right = distance_right + (bufx*50) + (bufy*50)

    if go_up11==1:
        bufx = abs(player_rect_upx - playerx)
        bufy = abs(player_rect_upy - playery)
        distance_up = bufx + bufy
        bufx = abs(int(player_rect_up[0]) - int(player_rect2[0])) + 1
        bufy = abs(int(player_rect_up[1]) - int(player_rect2[1])) + 1
        distance_up = distance_up + bufx*50 + bufy*50

    if go_down11==1:
        bufx = abs(player_rect_downx - playerx)
        bufy = abs(player_rect_downy - playery)
        distance_down = bufx + bufy
        bufx = abs(int(player_rect_down[0]) - int(player_rect2[0])) + 1
        bufy = abs(int(player_rect_down[1]) - int(player_rect2[1])) + 1
        distance_down = distance_down + bufx*50 + bufy*50

    if distance_left<=distance_right:
        way_x=distance_left
        buf_wayx='left'
    elif distance_right<distance_left:
        way_x=distance_right
        buf_wayx = 'right'

    if distance_up<=distance_down:
        way_y=distance_up
        buf_wayy = 'up'
    elif distance_down<distance_up:
        way_y = distance_down
        buf_wayy = 'down'

    if  way_x<=way_y:
        way=buf_wayx
    elif way_y<way_x:
        way = buf_wayy

    buf_poisk=way
    buf_poisk_rect()
    # print()
    # print(way)
    # print(distance_left)
    # print(distance_right)
    # print(distance_up)
    # print(distance_down)
    # print(buf_poisk)
    # print(player_rectx1,player_recty1)
    # print(playerx, playery)
    # print(buf_poiskX, buf_poiskY)

def buf_poisk_rect():
    global player_rect_leftx, player_rect_lefty, player_rect_rightx, player_rect_righty
    global player_rect_upx, player_rect_upy, player_rect_downx, player_rect_downy
    global buf_poiskX,buf_poiskY,buf_poisk
    if buf_poisk=='left':
        buf_poiskX=player_rect_leftx
        buf_poiskY=player_rect_lefty
    elif buf_poisk=='right':
        buf_poiskX = player_rect_rightx
        buf_poiskY = player_rect_righty
    elif buf_poisk=='up':
        buf_poiskX = player_rect_upx
        buf_poiskY = player_rect_upy
    elif buf_poisk=='down':
        buf_poiskX = player_rect_downx
        buf_poiskY = player_rect_downy

class Difficulte:
    def __init__(self,healse,damage,speed,distance):
        self.healse=healse
        self.damage=damage
        self.speed=speed
        self.distance=distance

difficulte=Difficulte(0,0,0,0)
difficulte1=Difficulte(8,1,4,100)
difficulte2=Difficulte(8,1,4,50)
difficulte3=Difficulte(10,1,4,0)

levels_massive=[]
class Levels:
    def __init__(self,map_level,difficult,number,foto,location,name):
        self.map_level=map_level
        self.difficult=difficult
        self.number=number
        self.foto=foto
        self.name=name
        self.location=location

def create_levels():
    levels_massive.append(Levels(1,1,1,levelON,base_locate,'training'))
    levels_massive.append(Levels(1, 1, 2, levelOFF,base_locate, 'first battle'))
    levels_massive.append(Levels(1, 2, 3, levelOFF,forest_locate, 'forest'))
    levels_massive.append(Levels(1, 2, 4, levelOFF,forest_locate ,'forest'))
    levels_massive.append(Levels(1, 2, 5, levelOFF,desert_locate, 'desert'))
    levels_massive.append(Levels(1, 2, 6, levelOFF,desert_locate, 'desert'))
    levels_massive.append(Levels(1, 3, 7, levelOFF, glade_locate, 'glade'))
    levels_massive.append(Levels(1, 3, 8, levelOFF, glade_locate, 'glade'))

def drow_levels():
    global difficulte,levelx,levely,map,locate,companys,level_number
    company,win = 0,0
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    for level in levels_massive:
        if level.number==5:
            levelx=50
            levely=levely+350
        if (mouse[0] >= levelx and mouse[0] <= levelx+300) and (mouse[1] >= levely and mouse[1] <= levely+300):
            if click[0] == 1:
                if level.foto==levelON:
                    level_number=level.number
                    difficulte=difficulte1
                    map=level.map_level
                    locate=level.location
                    companys=1
                    start_the_game()
        if run_level>=level.number:
            level.foto=levelON
        else:
            level.foto=levelOFF
        screen.blit(level.foto, (levelx, levely))
        print_text(level.name,levelx,levely-45,black,40)
        levelx=levelx+360
        clock.tick(40)

def calculation_level():
    global run_level,colcut_level,moneys2
    if win==1:
        moneys2=moneys2+1
        if level_number-run_level==0:
            run_level = run_level + 1

def company():
    global level,levels_massive,level_number,foto,name,difficult,map_level
    global levelx, levely
    while True:
        levelx=50
        levely=300
        screen.blit(bg_menu3, (0, 0))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                save()
                pygame.quit()
                sys.exit()
        if keys[pygame.K_ESCAPE]:
            menu()
        drow_levels()

        pygame.display.update()
        clock.tick(10)

class Block:
    def __init__(self,x,y,block):
        self.x = x
        self.y = y
        self.block=block
    def draw_block(self):
        screen.blit(self.block, (self.x, self.y))

block_massiv=[]

def create_block():
    global block_massiv
    block_massiv = []
    if map==1:
        pass
    if map==2:
        # левый верхний угол
        block_massiv.append(Block(160, 210, BLOCK))
        block_massiv.append(Block(160, 240, BLOCK))
        block_massiv.append(Block(160, 270, BLOCK))
        block_massiv.append(Block(160, 300, BLOCK))
        block_massiv.append(Block(160, 330, BLOCK))
        block_massiv.append(Block(160, 360, BLOCK))
        block_massiv.append(Block(160, 390, BLOCK))
        block_massiv.append(Block(160, 420, BLOCK))

        block_massiv.append(Block(190, 210, BLOCK))
        block_massiv.append(Block(220, 210, BLOCK))
        block_massiv.append(Block(250, 210, BLOCK))
        block_massiv.append(Block(280, 210, BLOCK))
        block_massiv.append(Block(310, 210, BLOCK))
        block_massiv.append(Block(340, 210, BLOCK))
        block_massiv.append(Block(370, 210, BLOCK))
        # левый нижний угол
        block_massiv.append(Block(160, 960, BLOCK))
        block_massiv.append(Block(160, 930, BLOCK))
        block_massiv.append(Block(160, 900, BLOCK))
        block_massiv.append(Block(160, 870, BLOCK))
        block_massiv.append(Block(160, 840, BLOCK))
        block_massiv.append(Block(160, 810, BLOCK))
        block_massiv.append(Block(160, 780, BLOCK))
        block_massiv.append(Block(160, 750, BLOCK))

        block_massiv.append(Block(190, 960, BLOCK))
        block_massiv.append(Block(220, 960, BLOCK))
        block_massiv.append(Block(250, 960, BLOCK))
        block_massiv.append(Block(280, 960, BLOCK))
        block_massiv.append(Block(310, 960, BLOCK))
        block_massiv.append(Block(340, 960, BLOCK))
        block_massiv.append(Block(370, 960, BLOCK))
        # правый верхний угол
        block_massiv.append(Block(1310, 210, BLOCK))
        block_massiv.append(Block(1310, 240, BLOCK))
        block_massiv.append(Block(1310, 270, BLOCK))
        block_massiv.append(Block(1310, 300, BLOCK))
        block_massiv.append(Block(1310, 330, BLOCK))
        block_massiv.append(Block(1310, 360, BLOCK))
        block_massiv.append(Block(1310, 390, BLOCK))
        block_massiv.append(Block(1310, 420, BLOCK))

        block_massiv.append(Block(1310, 210, BLOCK))
        block_massiv.append(Block(1280, 210, BLOCK))
        block_massiv.append(Block(1250, 210, BLOCK))
        block_massiv.append(Block(1220, 210, BLOCK))
        block_massiv.append(Block(1190, 210, BLOCK))
        block_massiv.append(Block(1160, 210, BLOCK))
        block_massiv.append(Block(1130, 210, BLOCK))
        block_massiv.append(Block(1100, 210, BLOCK))
        # правый нижний угол
        block_massiv.append(Block(1310, 960, BLOCK))
        block_massiv.append(Block(1310, 930, BLOCK))
        block_massiv.append(Block(1310, 900, BLOCK))
        block_massiv.append(Block(1310, 870, BLOCK))
        block_massiv.append(Block(1310, 840, BLOCK))
        block_massiv.append(Block(1310, 810, BLOCK))
        block_massiv.append(Block(1310, 780, BLOCK))
        block_massiv.append(Block(1310, 750, BLOCK))

        block_massiv.append(Block(1310, 960, BLOCK))
        block_massiv.append(Block(1280, 960, BLOCK))
        block_massiv.append(Block(1250, 960, BLOCK))
        block_massiv.append(Block(1220, 960, BLOCK))
        block_massiv.append(Block(1190, 960, BLOCK))
        block_massiv.append(Block(1160, 960, BLOCK))
        block_massiv.append(Block(1130, 960, BLOCK))
    if map==3:

        block_massiv.append(Block(710,440,BLOCK))
        block_massiv.append(Block(710, 470, BLOCK))
        block_massiv.append(Block(710, 500, BLOCK))
        block_massiv.append(Block(710, 530, BLOCK))
        block_massiv.append(Block(710, 560, BLOCK))
        block_massiv.append(Block(710, 590, BLOCK))
        block_massiv.append(Block(710, 620, BLOCK))
        block_massiv.append(Block(710, 650, BLOCK))
        block_massiv.append(Block(710, 680, BLOCK))

        block_massiv.append(Block(0, 510,BLOCK))
        block_massiv.append(Block(30,510, BLOCK))
        block_massiv.append(Block(60,510, BLOCK))
        block_massiv.append(Block(90,510, BLOCK))
        block_massiv.append(Block(120,510, BLOCK))
        block_massiv.append(Block(150,510, BLOCK))
        block_massiv.append(Block(180,510, BLOCK))
        block_massiv.append(Block(210, 510, BLOCK))

        block_massiv.append(Block(1470, 510, BLOCK))
        block_massiv.append(Block(1440, 510, BLOCK))
        block_massiv.append(Block(1410, 510, BLOCK))
        block_massiv.append(Block(1380, 510, BLOCK))
        block_massiv.append(Block(1350, 510, BLOCK))
        block_massiv.append(Block(1320, 510, BLOCK))
        block_massiv.append(Block(1290, 510, BLOCK))
        block_massiv.append(Block(1260, 510, BLOCK))

        block_massiv.append(Block(710, 150, BLOCK))
        block_massiv.append(Block(710, 180, BLOCK))
        block_massiv.append(Block(710, 210, BLOCK))
        block_massiv.append(Block(710, 240, BLOCK))
        block_massiv.append(Block(710, 270, BLOCK))

        block_massiv.append(Block(710, 970, BLOCK))
        block_massiv.append(Block(710, 940, BLOCK))
        block_massiv.append(Block(710, 910, BLOCK))
        block_massiv.append(Block(710, 880, BLOCK))
        block_massiv.append(Block(710, 850, BLOCK))

def draw_massive(massive):
    for block in massive:
        block.draw_block()

def proverka_bullet():
    global heals1,heals2,damage1,damage2
    for bullet in bullets:
            if bullet.x<1500 and bullet.x>0:
                bullet.x+=bullet.velx
                boom.play()
            else:
                  bullets.pop(bullets.index(bullet))
            if bullet.y<1000 and bullet.y>150:
                  bullet.y += bullet.vely
                  boom.play()
            else:
                  bullets.pop(bullets.index(bullet))
            for block in block_massiv:
                if (block.y <= bullet.y and bullet.y <= block.y + 30) and (
                        block.x <= bullet.x and bullet.x <= block.x + 30):
                    if bullet in bullets:
                        bullets.pop(bullets.index(bullet))
            if lastmove1 == 'вправо' or lastmove1 == 'вверх':
                if (playery2<=bullet.y and bullet.y<=playery2+50) and (playerx2<=bullet.x and bullet.x<=playerx2+50):
                    bullets.pop(bullets.index(bullet))
                    heals2 = heals2 - damage1
            elif lastmove1 == 'влево' or lastmove1 == 'вниз':
                if (playery2<=bullet.y and bullet.y<=playery2+50) and (playerx2+50>=bullet.x and bullet.x>=playerx2):
                    bullets.pop(bullets.index(bullet))
                    heals2 = heals2 - damage1
            else:
                pass

    for bullet2 in bullets2:
           if bullet2.x2 < 1500 and bullet2.x2 > 0:
                bullet2.x2 += bullet2.velx2
                boom.play()
           else:
                bullets2.pop(bullets2.index(bullet2))
           if bullet2.y2 < 1000 and bullet2.y2 > 150:
                bullet2.y2 += bullet2.vely2
                boom.play()
           else:
                bullets2.pop(bullets2.index(bullet2))
           for block in block_massiv:
               if (block.y <= bullet2.y2 and bullet2.y2 <= block.y + 30) and (
                       block.x <= bullet2.x2 and bullet2.x2 <= block.x + 30):
                   if bullet2 in bullets2:
                       bullets2.pop(bullets2.index(bullet2))
           if lastmove2=='вправо' or lastmove2 == 'вверх':
                if (playery<=bullet2.y2 and bullet2.y2<=playery+50) and (playerx<=bullet2.x2 and bullet2.x2<=playerx+50):
                    bullets2.pop(bullets2.index(bullet2))
                    heals1 = heals1 - damage2
           elif lastmove2=='влево' or lastmove2 == 'вниз':
                if (playery<=bullet2.y2 and bullet2.y2<=playery+50) and (playerx+50>=bullet2.x2 and bullet2.x2>=playerx):
                    bullets2.pop(bullets2.index(bullet2))
                    heals1=heals1-damage2
           else:
               pass

def proverka1(lastdown1,barriers):
    global go1,playerx,playery
    go1 = 1
    if lastdown1 == 'left':
        if (abs(playerx - playerx2) <= distanse+50 and abs(playery - playery2) <= distanse+50 and lastmove1 == "влево"):
            go1 = 0
            avaria.play(1)

        for barrier in barriers:
            if (abs(playerx - barrier.x) <= 30  and lastmove1 == "влево"):
                if barrier.y<=playery:
                    if abs(playery - barrier.y) <= 30:
                        go1 = 0
                        avaria.play(1)

                if barrier.y>playery:
                    if abs(playery - barrier.y) <= 50:
                        go1 = 0
                        avaria.play(1)

    if lastdown1 == 'right':
        if (abs(playerx - playerx2) <= distanse+50 and abs(playery - playery2) <= distanse+50 and lastmove1 == "вправо"):
            go1 = 0
            avaria.play(1)

        for barrier in barriers:
            if (abs(playerx - barrier.x) <= 50  and lastmove1 == "вправо"):
                if barrier.y<=playery:
                    if abs(playery - barrier.y) <= 30:
                        go1 = 0
                        avaria.play(1)
                if barrier.y>playery:
                    if abs(playery - barrier.y) <= 50:
                        go1 = 0
                        avaria.play(1)
    if lastdown1 == 'down':
        if (abs(playerx - playerx2) <= distanse+50 and abs(playery - playery2) <= distanse+50 and lastmove1 == "вниз"):
            go1 = 0
            avaria.play(1)

        for barrier in barriers:
            if (abs(playery - barrier.y) <= 50  and lastmove1 == "вниз"):
                if barrier.x<=playerx:
                    if abs(playerx - barrier.x) <= 30:
                        go1 = 0
                        avaria.play(1)

                if barrier.x>playerx:
                    if abs(playerx - barrier.x) <= 50:
                        go1 = 0
                        avaria.play(1)

    if lastdown1 == 'up':
        if (abs(playerx - playerx2) <= distanse+50 and abs(playery - playery2) <= distanse+50 and lastmove1 == "вверх"):
            go1 = 0

        for barrier in barriers:
            if (abs(playery - barrier.y) <= 30  and lastmove1 == "вверх"):
                if barrier.x<=playerx:
                    if abs(playerx - barrier.x) <= 30:
                        go1 = 0
                        avaria.play(1)

                if barrier.x>playerx:
                    if abs(playerx - barrier.x) <= 50:
                        go1 = 0
                        avaria.play(1)

def proverka2(lastdown2,barriers):
    global go2,playerx2,playery2
    go2 = 1
    if lastdown2 == 'left':
        if (abs(playerx - playerx2) < 50 and abs(playery - playery2) < 50 and lastmove2 == "влево"):
            go2 = 0
            avaria.play(1)

        for barrier in barriers:
            if (abs(playerx2 - barrier.x) <= 30  and lastmove2 == "влево"):
                if barrier.y<=playery2:
                    if abs(playery2 - barrier.y) <= 30:
                        go2 = 0
                        avaria.play(1)
                if barrier.y>playery2:
                    if abs(playery2 - barrier.y) <= 50:
                        go2 = 0
                        avaria.play(1)

    elif lastdown2 == 'right':
        if (abs(playerx - playerx2) < 50 and abs(playery - playery2) < 50 and lastmove2 == "вправо"):
            go2 = 0
            avaria.play(1)

        for barrier in barriers:
            if (abs(playerx2 - barrier.x) <= 50  and lastmove2 ==  "вправо"):
                if barrier.y<=playery2:
                    if abs(playery2 - barrier.y) <= 30:
                        go2 = 0
                        avaria.play(1)

                if barrier.y>playery2:
                    if abs(playery2 - barrier.y) <= 50:
                        go2 = 0
                        avaria.play(1)

    elif lastdown2 == 'down':
        if (abs(playerx - playerx2) < 50 and abs(playery - playery2) < 50 and lastmove2 == "вниз"):
            go2 = 0
            avaria.play(1)

        for barrier in barriers:
            if (abs(playery2 - barrier.y) <= 50  and lastmove2 == "вниз"):
                if barrier.x<=playerx2:
                    if abs(playerx2 - barrier.x) <= 30:
                        go2 = 0
                        avaria.play(1)

                if barrier.x>playerx2:
                    if abs(playerx2 - barrier.x) <= 50:
                        go2 = 0
                        avaria.play(1)

    elif lastdown2 == 'up':
        if (abs(playerx - playerx2) < 50 and abs(playery - playery2) < 50 and lastmove2 == "вверх"):
            go2 = 0
            avaria.play(1)

        for barrier in barriers:
            if (abs(playery2 - barrier.y) <= 30  and lastmove2 == "вверх"):
                if barrier.x<=playerx2:
                    if abs(playerx2 - barrier.x) <= 30:
                        go2 = 0
                        avaria.play(1)

                if barrier.x>playerx2:
                    if abs(playerx2 - barrier.x) <= 50:
                        go2 = 0
                        avaria.play(1)

def dop_proverka2():
    global playery2,tp2,playerx2
    tp2 = 0
    for block in block_massiv:
        if block.x<playerx2<block.x+30:
            if block.y<playery2<block.y+30:
                tp2=1

        if block.x<playerx2+50<block.x+30:
            if block.y<playery2<block.y+30:
                tp2=1

        if block.x<playerx2<block.x+30:
            if block.y<playery2+50<block.y+30:
                tp2=1

        if block.x<playerx2+50<block.x+30:
            if block.y<playery2+50<block.y+30:
                tp2=1

    if lastmove2=='влево':
        if tp2==1:
            playerx2=playerx2+10
    if lastmove2=='вправо':
        if tp2==1:
            playerx2=playerx2-10
    if lastmove2=='вверх':
        if tp2==1:
            playery2=playery2+10
    if lastmove2=='вниз':
        if tp2==1:
            playery2=playery2-10

def dop_proverka1():
    global playery,tp1,playerx
    tp1 = 0

    for block in block_massiv:
        if block.x<playerx<block.x+30:
            if block.y<playery<block.y+30:
                tp1=1
        if block.x<playerx+50<block.x+30:
            if block.y<playery<block.y+30:
                tp1=1
        if block.x<playerx<block.x+30:
            if block.y<playery+50<block.y+30:
                tp1=1
        if block.x<playerx+50<block.x+30:
            if block.y<playery+50<block.y+30:
                tp1=1

    if lastmove1=='влево':
        if tp1==1:
            playerx=playerx+10
    if lastmove1=='вправо':
        if tp1==1:
            playerx=playerx-10
    if lastmove1=='вверх':
        if tp1==1:
            playery=playery+10
    if lastmove1=='вниз':
        if tp1==1:
            playery=playery-10

def proverka_box1():
    global damage1,heals1,speed1
    if ((playerx <= box_damageX and box_damageX <= playerx + 50) or (
            playerx <= box_damageX + 20 and box_damageX + 20 <= playerx + 50)) and ((
                                                                                            playery <= box_damageY and box_damageY <= playery + 50) or (
                                                                                            playery <= box_damageY + 20 and box_damageY + 20 <= playery + 50)):
        damage1 = damage1 + 1
        random_box_damage()
        upgrade.play()

    if ((playerx <= box_healseX and box_healseX <= playerx + 50) or (
            playerx <= box_healseX + 20 and box_healseX + 20 <= playerx + 50)) and ((
                                                                                            playery <= box_healseY and box_healseY <= playery + 50) or (
                                                                                            playery <= box_healseY + 20 and box_healseY + 20 <= playery + 50)):
        if heals1 < 10:
            heals1 = heals1 + 1
            random_box_healse()
            upgrade.play()

    if ((playerx <= box_speedX and box_speedX <= playerx + 50) or (
            playerx <= box_speedX + 20 and box_speedX + 20 <= playerx + 50)) and ((
                                                                                          playery <= box_speedY and box_speedY <= playery + 50) or (
                                                                                          playery <= box_speedY + 20 and box_speedY + 20 <= playery + 50)):
        if speed2 < 15:
            speed1 = speed1 + 1
            random_box_speed()
            upgrade.play()

    if ((playerx <= box_TNTX and box_TNTX <= playerx + 50) or (
            playerx <= box_TNTX + 20 and box_TNTX + 20 <= playerx + 50)) and ((
                                                                                      playery <= box_TNTY and box_TNTY <= playery + 50) or (
                                                                                      playery <= box_TNTY + 20 and box_TNTY + 20 <= playery + 50)):
        heals1 = heals1 - 1
        random_box_TNT()
        upgrade.play()
    else:
        pass

def proverka_box2():
    global damage2,heals2,speed2
    if ((playerx2 <= box_damageX and box_damageX <= playerx2 + 50) or (
            playerx2 <= box_damageX + 20 and box_damageX + 20 <= playerx2 + 50)) and ((
                                                                                              playery2 <= box_damageY and box_damageY <= playery2 + 50) or (
                                                                                              playery2 <= box_damageY + 20 and box_damageY + 20 <= playery2 + 50)):
        damage2 = damage2 + 1
        random_box_damage()
        upgrade.play()

    if ((playerx2 <= box_healseX and box_healseX <= playerx2 + 50) or (
            playerx2 <= box_healseX + 20 and box_healseX + 20 <= playerx2 + 50)) and ((
                                                                                              playery2 <= box_healseY and box_healseY <= playery2 + 50) or (
                                                                                              playery2 <= box_healseY + 20 and box_healseY + 20 <= playery2 + 50)):
        if heals2 < 10:
            heals2 = heals2 + 1
            random_box_healse()
            upgrade.play()

    if ((playerx2 <= box_speedX and box_speedX <= playerx2 + 50) or (
            playerx2 <= box_speedX + 20 and box_speedX + 20 <= playerx2 + 50)) and ((
                                                                                            playery2 <= box_speedY and box_speedY <= playery2 + 50) or (
                                                                                            playery2 <= box_speedY + 20 and box_speedY + 20 <= playery2 + 50)):
        if speed2 < 15:
            speed2 = speed2 + 1
            random_box_speed()
            upgrade.play()

    if ((playerx2 <= box_TNTX and box_TNTX <= playerx2 + 50) or (
            playerx2 <= box_TNTX + 20 and box_TNTX + 20 <= playerx2 + 50)) and ((
                                                                                        playery2 <= box_TNTY and box_TNTY <= playery2 + 50) or (
                                                                                        playery2 <= box_TNTY + 20 and box_TNTY + 20 <= playery2 + 50)):
        heals2 = heals2 - 1
        random_box_TNT()
        upgrade.play()

def print_text(massege,text_x,text_y,color_text,font_size,font_type='шрифт.TTF'):
    font_type=pygame.font.Font(font_type,font_size)
    text=font_type.render(massege,True,color_text)
    screen.blit(text,(text_x,text_y))

def upgrate():
    global moneys2,dop_heals2,dop_damage2,dop_speed2,skin
    global cost_upgrade_heal,cost_upgrade_damage,cost_upgrade_speed
    global collect_freeztank_skin,collect_firetank_skin,collect_duotank_skin
    ctranica=defolt_skin2
    nomer_ctranica = 1
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                save()
                pygame.quit()
                sys.exit()
        if keys[pygame.K_ESCAPE]:
            menu()

        screen.blit(bg_menu5,(0,0))
        if nomer_ctranica==1:
            button1 = sellect_button
            ctranica=defolt_skin2
            screen.blit(button1, (180, 630))
            if (mouse[0] >= 180 and mouse[0] <= 480) and (mouse[1] >= 630 and mouse[1] <= 730):
                if click[0] == 1:
                    buton.play()
        if nomer_ctranica == 2:
            ctranica = freeztank_skin
            if collect_freeztank_skin==1:
                button1=sellect_button
            else:
                button1=buy_button
            screen.blit(button1, (180, 630))
            if (mouse[0] >= 180 and mouse[0] <= 480) and (mouse[1] >= 630 and mouse[1] <= 730):
                if click[0] == 1:
                    buton.play()
                    if moneys2>=cost_freeztank_skin:
                        skin_number=2
                        if collect_freeztank_skin==0:
                            moneys2 = moneys2 - cost_freeztank_skin
                            collect_freeztank_skin=1
                    if collect_freeztank_skin==1:
                        skin_number = 2

        if nomer_ctranica == 3:
            ctranica = firetank_skin
            if collect_firetank_skin==1:
                button2=sellect_button
            else:
                button2=buy_button
            screen.blit(button2, (180, 630))
            if (mouse[0] >= 180 and mouse[0] <= 480) and (mouse[1] >= 630 and mouse[1] <= 730):
                if click[0] == 1:
                    buton.play()
                    if moneys2>=cost_firetank_skin:
                        skin_number=3
                        if collect_firetank_skin==0:
                            moneys2 = moneys2 - cost_firetank_skin
                            collect_firetank_skin = 1
                    if collect_firetank_skin==1:
                        skin_number = 3

        if nomer_ctranica == 4:
            ctranica = duotank_skin
            if collect_duotank_skin==1:
                button3=sellect_button
            else:
                button3=buy_button
            screen.blit(button3, (180, 630))
            if (mouse[0] >= 180 and mouse[0] <= 480) and (mouse[1] >= 630 and mouse[1] <= 730):
                if click[0] == 1:
                    buton.play()
                    if moneys2>=cost_duotank_skin:
                        skin_number=4
                        if collect_duotank_skin==0:
                            moneys2 = moneys2 - cost_duotank_skin
                            collect_duotank_skin = 1
                    if collect_duotank_skin==1:
                        skin_number = 4

        screen.blit(ctranica, (180, 295))
        screen.blit(left_button, (120, 400))
        if (mouse[0] >= 120 and mouse[0] <= 170) and (mouse[1] >= 400 and mouse[1] <=500):
            if click[0] == 1:
                buton.play()
                if nomer_ctranica>1:
                    nomer_ctranica=nomer_ctranica-1

        screen.blit(right_button, (500, 400))
        if (mouse[0] >= 500 and mouse[0] <= 550) and (mouse[1] >= 400 and mouse[1] <=500):
            if click[0] == 1:
                buton.play()
                if nomer_ctranica<4:
                    nomer_ctranica = nomer_ctranica + 1

        print_text(f":{cost_upgrade_heal}", 1200, 535, orange,60)
        screen.blit(money, (1260, 540))
        screen.blit(upgrade_heal, (900,525))
        if (mouse[0] >= 900 and mouse[0] <= 1200) and (mouse[1] >= 525 and mouse[1] <=625):
            if click[0] == 1:
                buton.play()
                if moneys2>=cost_upgrade_heal and dop_heals2<=6:
                    dop_heals2=dop_heals2+1
                    moneys2 = moneys2 - cost_upgrade_heal
                    cost_upgrade_heal=cost_upgrade_heal+1
        if dop_heals2 > 0:
            screen.blit(oneheal, (1136, 530))
        if dop_heals2 > 1:
            screen.blit(oneheal, (1105, 530))
        if dop_heals2 > 2:
            screen.blit(oneheal, (1074, 530))
        if dop_heals2 > 3:
            screen.blit(oneheal, (1043, 530))
        if dop_heals2 > 4:
            screen.blit(oneheal, (1012, 530))
        if dop_heals2 > 5:
            screen.blit(oneheal, (981, 530))
        if dop_heals2 > 6:
            screen.blit(oneheal, (950, 530))

        print_text(f":{cost_upgrade_damage}", 1200, 410, orange,60)
        screen.blit(money, (1260, 420))
        screen.blit(upgrade_damage, (900,400))
        if (mouse[0] >= 900 and mouse[0] <= 1200) and (mouse[1] >= 400 and mouse[1] <=500):
            if click[0] == 1:
                buton.play()
                if moneys2>=cost_upgrade_damage and dop_damage2<=6:
                    dop_damage2=dop_damage2+1
                    moneys2 = moneys2 - cost_upgrade_damage
                    cost_upgrade_damage=cost_upgrade_damage+1
        if dop_damage2 > 0:
            screen.blit(onedamage, (1136, 405))
        if dop_damage2 > 1:
            screen.blit(onedamage, (1105, 405))
        if dop_damage2 > 2:
            screen.blit(onedamage, (1074, 405))
        if dop_damage2 > 3:
            screen.blit(onedamage, (1043, 405))
        if dop_damage2 > 4:
            screen.blit(onedamage, (1012, 405))
        if dop_damage2 > 5:
            screen.blit(onedamage, (981, 405))
        if dop_damage2 > 6:
            screen.blit(onedamage, (950, 405))

        print_text(f":{cost_upgrade_speed}", 1200, 280, orange,60)
        screen.blit(money, (1260, 290))
        screen.blit(upgrade_speed, (900, 275))
        if (mouse[0] >= 900 and mouse[0] <= 1200) and (mouse[1] >= 275 and mouse[1] <=375):
            if click[0] == 1:
                buton.play()
                if moneys2>=cost_upgrade_speed and dop_speed2<=6:
                    dop_speed2=dop_speed2+1
                    moneys2 = moneys2 - cost_upgrade_speed
                    cost_upgrade_speed = cost_upgrade_speed + 1
        if dop_speed2 > 0:
            screen.blit(onespeed, (1136, 280))
        if dop_speed2 > 1:
            screen.blit(onespeed, (1105, 280))
        if dop_speed2 > 2:
            screen.blit(onespeed, (1074, 280))
        if dop_speed2 > 3:
            screen.blit(onespeed, (1043, 280))
        if dop_speed2 > 4:
            screen.blit(onespeed, (1012, 280))
        if dop_speed2 > 5:
            screen.blit(onespeed, (981, 280))
        if dop_speed2 > 6:
            screen.blit(onespeed, (950, 280))

        print_text(f"moneys:{moneys2}", 1200, 250,orange,30)
        pygame.display.update()
        clock.tick(10)

def SELLECT_MAP():
    if map==1:
        pass
    if map==2:
        draw_massive(block_massiv)
    if map==3:
        draw_massive(block_massiv)

def sellect_map(plaeyrs):
    global map
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if keys[pygame.K_ESCAPE]:
            menu()
        screen.blit(bg_menu3,(0,0))

        screen.blit(map1, (200,300))
        print_text("first map",200,265,black,40)
        screen.blit(sellect_button,(210,530))
        if (mouse[0] >= 210 and mouse[0] <= 510) and (mouse[1] >= 530 and mouse[1] <=630):
            if click[0] == 1:
                buton.play()
                map = 1
                if plaeyrs==1:
                    bg_difficulty()
                elif plaeyrs==2:
                    start_the_game2()
                SELLECT_MAP()

        screen.blit(map2, (550, 300))
        print_text("second map", 550, 265, black, 40)
        screen.blit(sellect_button, (560, 530))
        if (mouse[0] >= 560 and mouse[0] <= 860) and (mouse[1] >= 530 and mouse[1] <= 630):
            if click[0] == 1:
                buton.play()
                map = 2
                if plaeyrs == 1:
                    bg_difficulty()
                elif plaeyrs == 2:
                    start_the_game2()
                SELLECT_MAP()

        screen.blit(map3, (900, 300))
        print_text("second map", 900, 265, black, 40)
        screen.blit(sellect_button, (910, 530))
        if (mouse[0] >= 910 and mouse[0] <= 1210) and (mouse[1] >= 530 and mouse[1] <= 630):
            if click[0] == 1:
                buton.play()
                map = 3
                SELLECT_MAP()
                if plaeyrs == 1:
                    bg_difficulty()
                if plaeyrs == 2:
                    start_the_game2()

        pygame.display.update()
        clock.tick(10)

def bg_difficulty():
    global distanse,difficulte,speed1,heals1,damage1
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if keys[pygame.K_ESCAPE]:
            menu()
        screen.blit(bg_menu2, (0, 0))
        print_text('select difficulty', 630, 250, black,30)
        screen.blit(easy_button, (590, 400))
        if (mouse[0] >= 550 and mouse[0] <= 590 + 200) and (mouse[1] >= 300 and mouse[1] <= 400 + 100):
            if click[0] == 1:
                buton.play()
                difficulte=difficulte1
                start_the_game()
        screen.blit(normal_button,(590, 550))
        if (mouse[0] >= 550 and mouse[0] <= 590 + 200) and (mouse[1] >= 450 and mouse[1] <= 550 + 100):
            if click[0] == 1:
                buton.play()
                difficulte=difficulte2
                start_the_game()
        screen.blit(hard_button,(590, 700))
        if (mouse[0] >= 550 and mouse[0] <= 590 + 200) and (mouse[1] >= 600 and mouse[1] <= 700 + 100):
            if click[0] == 1:
                difficulte=difficulte3
                start_the_game()
        pygame.display.update()
        clock.tick(10)

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
    global box_damageX,box_damageY
    box_damageX = random.randint(40,1460 )
    box_damageY = random.randint(190,960 )
    for block in block_massiv:
        if block.x<=box_damageX<=block.x+30:
            if block.y <= box_damageY+30 <= block.y:
                random_box_damage()
    if playerx<=box_damageX<=playerx+50 or playerx2<=box_damageX<=playerx2+50:
        if playery <= box_damageY <= playery + 50 or playery2 <= box_damageY <= playery2 + 50:
            random_box_damage()

def random_box_healse():
    global box_healseX,box_healseY
    box_healseX = random.randint(40,1460 )
    box_healseY = random.randint(190,960 )
    for block in block_massiv:
        if block.x<=box_healseX<=block.x+30:
            if block.y <= box_healseY <= block.y+30:
                random_box_healse()
    if playerx<=box_healseX<=playerx+50 or playerx2<=box_healseX<=playerx2+50:
        if playery <= box_healseY <= playery + 50 or playery2 <= box_healseY <= playery2 + 50:
            random_box_healse()

def random_box_speed():
    global box_speedX,box_speedY
    box_speedX = random.randint(40,1460)
    box_speedY = random.randint(190,960 )
    for block in block_massiv:
        if block.x<=box_speedX<=block.x+30:
            if block.y <= box_speedY <= block.y+30:
                random_box_speed()
    if playerx<=box_speedX<=playerx+50 or playerx2<=box_speedX<=playerx2+50:
        if playery <= box_speedY <= playery + 50 or playery2 <= box_speedY <= playery2 + 50:
            random_box_speed()

def random_box_TNT():
    global box_TNTX,box_TNTY
    box_TNTX=random.randint(40,1460)
    box_TNTY=random.randint(190,960)
    for block in block_massiv:
        if block.x<=box_TNTX<=block.x+30:
            if block.y <= box_TNTY <= block.y+30:
                random_box_TNT()
    if playerx <= box_TNTX <= playerx + 50 or playerx2 <= box_TNTX <= playerx2 + 50:
        if playery <= box_TNTY <= playery + 50 or playery2 <= box_TNTY <= playery2 + 50:
            random_box_TNT()

def controls():
    while True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        screen.blit(bg_controls,(0,0))
        print_text('Press Escape to continue', 500, 250,black,30)
        if keys[pygame.K_ESCAPE]:
            break
        pygame.display.update()
        clock.tick(10)

def pause():
    pauseON.play()
    global saund
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save()
            pygame.quit()
            sys.exit
    paused=True
    while paused:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                save()
                pygame.quit()
                sys.exit()
        screen.blit(bg_menu3, (0,0))
        print_text('Paused. press Enter to continue', 450, 250,black,30)

        screen.blit(saund,(900,300))
        if (mouse[0]>=900 and mouse[0]<=1000) and (mouse[1]>=300 and mouse[1]<=400):
            if click[0]==1:
                buton.play()
                if saund==saundON:
                    saund=saundOFF
                    screen.blit(saund, (900, 300))
                    set_volume(0,0,0,0,0,0,0,0,0)
                else:
                    saund =saundON
                    set_volume(1,1,1,1,1,1,1,1,1)


        screen.blit(settings_button, (550, 300))
        if (mouse[0]>=550 and mouse[0]<=850) and (mouse[1]>=300 and mouse[1]<=400):
            if click[0]==1:
                buton.play()
                controls()

        screen.blit(menu_batton, (550, 450))
        if (mouse[0] >= 550 and mouse[0] <= 850) and (mouse[1] >= 450 and mouse[1] <= 550):
            if click[0] == 1:
                buton.play()
                menu()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused=False


        pygame.display.update()
        clock.tick(10)
    pauseOFF.play()

def play():
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save()
                pygame.quit()
                sys.exit
        screen.blit(bg_menu4, (0, 0))
        screen.blit(player1_button, (200, 650))
        if (mouse[0] >= 200 and mouse[0] <= 500) and (mouse[1] >= 650 and mouse[1] <= 750):
            if click[0] == 1:
                buton.play()
                sellect_map(1)
        screen.blit(player2_button, (965, 650))
        if (mouse[0] >= 965 and mouse[0] <= 1265) and (mouse[1] >= 650 and mouse[1] <= 750):
            if click[0] == 1:
                buton.play()
                sellect_map(2)
        clock.tick(10)
        pygame.display.update()

def menu():
    global game_overs
    if game_overs==1:
        calculation_level()
        game_overs=0
    while True:
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                save()
                sys.exit
                pygame.quit()
        screen.blit(bg_menu2, (0, 0))
        screen.blit(play_button, (590, 400))
        if (mouse[0]>=590 and mouse[0]<=890) and (mouse[1]>=400 and mouse[1]<=500):
            if click[0]==1:
                buton.play()
                play()

        screen.blit(company_button, (590, 550))
        if (mouse[0] >= 590 and mouse[0] <= 890) and (mouse[1] >= 570 and mouse[1] <= 650):
            if click[0] == 1:
                buton.play()
                company()

        screen.blit(apgrate_button, (590, 700))
        if (mouse[0] >= 590 and mouse[0] <= 890) and (mouse[1]>=720 and mouse[1]<=800):
            if click[0] == 1:
                buton.play()
                upgrate()

        screen.blit(quit_button, (590, 850))
        if (mouse[0]>=590 and mouse[0]<=890) and (mouse[1]>=870 and mouse[1]<=950):
            if click[0]==1:
                buton.play()
                save()
                pygame.quit()
                sys.exit()
        clock.tick(10)
        pygame.display.update()

if skin_number==1:
    walkStand2 = pygame.image.load('танки\танквверх2.png')
if skin_number==2:
    walkStand2 = pygame.image.load('танки\скин ледянной танк вверх.png')
if skin_number==3:
    walkStand2 = pygame.image.load('танки\скин огненный танк вверх.png')
if skin_number==4:
    pass
def sellect_skin():
    if skin_number==1:
        skin_defolt()
    if skin_number==2:
        skin_freeztank()
    if skin_number==3:
        skin_firetank()
    if skin_number==4:
        skin_duotank()

create_levels()
def drawwindow():
    global heartx,fps
    screen.blit(locate, (0, 0))
    # linex=0
    # liney=150
    # linex2=0
    # liney2=1000
    # liney3=150
    # liney4=150
    # for line in range(30):
    #     pygame.draw.line(screen, white, (linex, liney), (linex2, liney2), 1)
    #     pygame.draw.line(screen, white, (0, liney3), (1500, liney4), 1)
    #     linex=linex+50
    #     linex2=linex2+50
    #     liney3=liney3+50
    #     liney4=liney4+50
    screen.blit(kirpichi,(0,0))
    sellect_skin()
    print_text(f":{heals2}",250,8,black,25)
    print_text(f":{speed2}", 250, 58,black,25)
    print_text(f":{damage2}", 250, 108,black,25)
    print_text(f":{moneys2}",360, 8,black,25 )
    print_text(f":{kills2}", 360, 58,black,25)

    screen.blit(heart, (200, 2))
    screen.blit(speed, (200, 52))
    screen.blit(damage, (200, 102))
    screen.blit(walkup2, (420, 52))
    screen.blit(money,(310,2))
    screen.blit(kill, (310, 52))

    print_text(f":{heals1}", 850, 8,black,25)
    print_text(f":{speed1}", 850, 58,black,25)
    print_text(f":{damage1}", 850, 108,black,25)
    print_text(f":{moneys1}", 960, 8,black,25)
    print_text(f":{kills1}", 960, 58,black,25)

    screen.blit(heart, (800, 2))
    screen.blit(speed, (800, 52))
    screen.blit(damage, (800, 102))
    screen.blit(walkup1, (1020, 52))
    screen.blit(money, (910, 2))
    screen.blit(kill, (910, 52))

    screen.blit(box_damage,(box_damageX,box_damageY))
    screen.blit(box_healse,(box_healseX,box_healseY))
    screen.blit(box_speed,(box_speedX,box_speedY))
    screen.blit(box_TNT,(box_TNTX,box_TNTY))
    for bullet in bullets:
        bullet.draw(screen)
    for bullet2 in bullets2:
        bullet2.draw(screen)
    fps = fps + 1
    drawwindow2()
    drawwindow1()
    SELLECT_MAP()
    clock.tick(80)
    pygame.display.update()

def drawwindow1():
    global animcount1
    global walkStand1

    if animcount1 + 1 >= 30:
        animcount1 = 0

    if left1==True:
        screen.blit(walkleft1, (playerx, playery))
        walkStand1 = walkleft1
    elif right1==True:
        screen.blit(walkright1, (playerx, playery))
        walkStand1 = walkright1
    elif up1==True:
        screen.blit(walkup1, (playerx, playery))
        walkStand1 = walkup1
    elif down1==True:
        screen.blit(walkdown1, (playerx, playery))
        walkStand1 = walkdown1
    screen.blit(walkStand1, (playerx, playery))

bullets=[]
bullets2=[]

def drawwindow2():
    global animcount2
    global walkStand2
    if animcount2 + 1 >= 30:
        animcount2 = 0
    if left2==True:
        screen.blit(walkleft2, (playerx2, playery2))
        walkStand2 =walkleft2
    if right2==True:
        screen.blit(walkright2, (playerx2, playery2))
        walkStand2 = walkright2
    if up2==True:
        screen.blit(walkup2, (playerx2, playery2))
        walkStand2 = walkup2
    if down2==True:
        screen.blit(walkdown2, (playerx2, playery2))
        walkStand2 =walkdown2
    screen.blit(walkStand2, (playerx2, playery2))

def game_over():
    global players,win,colcut_level,game_overs,companys
    play_musik=0
    while True:
        play_musik = play_musik+1
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save()
                pygame.quit()
                sys.exit
        screen.blit(bg_menu2,(0,0))
        if players==1:
            if heals2<=0:
                screen.blit(defolt_skin2,(590,550))
                print_text('YOU LUSE', 530, 400, black, 60)
                if play_musik==1:
                    fail.play(1)
                if companys==1:
                    win=0
                    game_overs=1
            if heals1<=0:
                screen.blit(defolt_skin2, (590, 550))
                print_text('YOU WON', 565, 350, black, 60)
                if play_musik == 5:
                    if run_level==8:
                        music.stop()
                        game_complete.play(1)
                if play_musik >= 5:
                    if run_level==8:
                        print_text('Game comlited', 440, 400, black, 70)
                if play_musik==1:
                    level_complite.play(1)
                if companys == 1:
                    win = 1
                    game_overs=1
        if players==2:
            if heals2<=0:
                screen.blit(defolt_skin1,(590,550))
                print_text('plaer one ',615,400,black,40)
                print_text('WON', 620, 450, black, 90)
            if heals1<=0:
                screen.blit(defolt_skin2, (590, 550))
                print_text('plaer two ', 615, 400, black, 40)
                print_text('WON', 620, 450, black, 90)
        print_text('Paused. press escape to continue', 500,900, black, 30)
        if keys[pygame.K_ESCAPE]:
            menu()
        clock.tick(10)
        pygame.display.update()

def go_left1():
    global  playerx,left1,right1,up1,down1,lastmove1,playery
    playerx -= speed1
    left1 = True
    right1 = False
    up1 = False
    down1 = False
    lastmove1 = "влево"

def go_right1():
    global playerx, left1, right1, up1, down1, lastmove1,playery
    playerx += speed1
    left1 = False
    right1 = True
    up1 = False
    down1 = False
    lastmove1 = "вправо"

def go_up1():
    global playerx, left1, right1, up1, down1, lastmove1,playery
    playery -= speed1
    up1 = True
    down1 = False
    left1 = False
    right1 = False
    lastmove1 = "вверх"

def go_down1():
    global playerx, left1, right1, up1, down1, lastmove1,playery
    playery += speed1
    up1 = False
    down1 = True
    left1 = False
    right1 = False
    lastmove1 = "вниз"

def go_left2():
    global playerx2, left2, right2, up2, down2, lastmove2,playery2
    playerx2 -= speed2
    left2 = True
    right2 = False
    up2 = False
    down2 = False
    lastmove2 = "влево"

def go_right2():
    global playerx2, left2, right2, up2, down2, lastmove2, playery2
    playerx2 += speed2
    left2 = False
    right2 = True
    up2 = False
    down2 = False
    lastmove2 = "вправо"

def go_up2():
    global playerx2, left2, right2, up2, down2, lastmove2, playery2
    playery2 -= speed2
    up2 = True
    down2 = False
    left2 = False
    right2 = False
    lastmove2 = "вверх"

def go_down2():
    global playerx2, left2, right2, up2, down2, lastmove2, playery2
    playery2 += speed2
    up2 = False
    down2 = True
    left2 = False
    right2 = False
    lastmove2 = "вниз"

def start_the_game():
    global playery2, playery, left1, up1, animcount1, right2, down2, heals1, lastmove1, lastmove2, speed1, distanse, moneys2, kills1,goup1,go_left_stenka,go_down_stenka
    global playerx2, playerx, right1, down1, left2, up2, animcount2, heals2, damage1, damage2, speed2, event, kills2, moneys1,players,go_right_stenka,go_up_stenka
    players = 1
    playerx2 = 251
    playery2 = 251
    playerx = 1201
    playery = 851
    speed2 = 4+dop_speed2
    heals2 = 10+dop_heals2
    damage2 = 1+dop_damage2
    heals1=difficulte.healse
    damage1 = difficulte.damage
    speed1 = difficulte.speed
    distance = difficulte.distance
    goup1=0
    x1,y1 = 1500,300
    x2,y2 = -750,300
    x_rect1,y_rect1=-3000,0
    x_rect2, y_rect2 = 3000, 600
    fps=0
    go_left_stenka=0
    go_down_stenka=0
    go_right_stenka=0
    go_up_stenka=0
    poiskX = playerx2
    poiskY = playery2
    random_box_damage()
    random_box_healse()
    random_box_speed()
    random_box_TNT()
    create_block()
    permissible_massive()
    poisk_wey(poiskX,poiskY)
    speed_rect1,speed_rect2=40,40
    speed_print1,speed_print2=20,20
    game_complete.stop()
    for i in range(200):
        screen.blit(locate,(0,0))
        screen.blit(print_start_raund_right, (x1, y1))
        screen.blit(defolt_skin1, (x1+275, y1))
        screen.blit(print_start_raund_left, (x2, y2))
        screen.blit(skin, (x2 + 275, y2))
        pygame.draw.rect(screen,black,(x_rect1,y_rect1,1500,300))
        pygame.draw.rect(screen, black, (x_rect2, y_rect2, 1500, 600))
        x_rect1=x_rect1+speed_rect1
        x_rect2 = x_rect2 - speed_rect2

        if x_rect1>=-1000:
            speed_rect1=5
        if x_rect1>=-500:
            speed_rect1=40
        if x_rect2<=1000:
            speed_rect2=5
        if x_rect2<=500:
            speed_rect2=40

        x1 = x1 - speed_print1
        x2 = x2 + speed_print2
        if x2>-250:
            speed_print2=5
        if x2>=10:
            speed_print2=0

        if x1<1000:
            speed_print1=5
        if x1<=740:
            speed_print1=0

        pygame.display.update()
    while True:
        if fps==1:
            fight.play()
            time.sleep(1.5)
        keys = pygame.key.get_pressed()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                save()
                pygame.quit()
                sys.exit()
        if heals1<=0:
            moneys2=moneys2+1
            kills2 = kills2 + 1
            game_over()
        if heals2<=0:
            moneys1 = moneys1 + 1
            kills1=kills1+1
            game_over()
        if keys[pygame.K_ESCAPE]:
            pause()
        proverka_bullet()
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
            lastdown2 = 'left'
            proverka2(lastdown2,block_massiv)
            if go2 == 1:
                go_left2()
            proverka_box2()

        elif keys[pygame.K_d] and playerx2 <= 1440:
            lastdown2 = 'right'
            proverka2(lastdown2,block_massiv)
            if go2 == 1:
                go_right2()
            proverka_box2()

        elif keys[pygame.K_w] and playery2 >= 160:
            lastdown2 = 'up'
            proverka2(lastdown2,block_massiv)
            if go2 == 1:
                go_up2()
            proverka_box2()

        elif keys[pygame.K_s] and playery2 <= 940:
            lastdown2 = 'down'
            proverka2(lastdown2,block_massiv)
            if go2 == 1:
                go_down2()
            proverka_box2()
        else:
            left2 = False
            right2 = False
            up2 = False
            down2 = False
            animcount2 = 0

        poiskX=playerx2
        poiskY=playery2
        if heals1<10:
            poiskX=box_healseX
            poiskY=box_healseY
        if abs(playerx-box_speedX)<=50 and abs(playery-box_speedY)<=50:
            poiskX=box_speedX
            poiskY=box_speedY
        if abs(playerx-box_damageX)<=50 and abs(playery-box_damageY)<=50:
            poiskX=box_damageX
            poiskY=box_damageY
        if buf_poiskX-2<playerx<buf_poiskX+2 and buf_poiskY-2<playery<buf_poiskY+2:
            poisk_wey(poiskX,poiskY)
        run1 = 0
        if abs(playerx-buf_poiskX)>0:
            if buf_poiskX-2<playerx<buf_poiskX+2:
                pass
            else:
                if playerx-buf_poiskX>=0:
                    if run1==0:
                        if  playerx>=10 :
                            lastdown1 = 'left'
                            proverka1(lastdown1,block_massiv)
                            if go1 == 1:
                                go_left1()
                                run1=1
                            proverka_box1()
                elif playerx-buf_poiskX<0:
                    if run1 == 0:
                        if  playerx <= 1440 :
                            lastdown1 = 'right'
                            proverka1(lastdown1,block_massiv)
                            if go1 == 1:
                                go_right1()
                                run1 = 1
                            proverka_box1()
                else:
                    pass

        if abs(playery-buf_poiskY)>0:
            if buf_poiskY-2<playery<buf_poiskY+2:
                pass
            else:
                if playery-buf_poiskY>=0:
                    if run1 == 0:
                        if  playery >= 160 :
                            lastdown1 = 'up'
                            proverka1(lastdown1,block_massiv)
                            if go1 == 1:
                                go_up1()
                                run1 = 1
                            proverka_box1()
                elif playery-buf_poiskY<0:
                    if run1 == 0:
                        if  playery <= 940 :
                            lastdown1 = 'down'
                            proverka1(lastdown1,block_massiv)
                            if go1 == 1:
                                go_down1()
                                run1 = 1
                            proverka_box1()
                else:
                    pass
        else:
            left1 = False
            right1 = False
            up1 = False
            down1 = False
            animcount1 = 0
        drawwindow()

def start_the_game2():
    global playery2,playery,left1,up1,animcount1,right2,down2,heals1,lastmove1,lastmove2,speed1,distanse,moneys2,kills1
    global playerx2,playerx,right1,down1,left2,up2,animcount2,heals2,damage1,damage2,speed2,event,kills2,moneys1,players
    players = 2
    playerx2 = 251
    playery2 = 251
    speed2 = 4+dop_speed2
    heals2 = 10+dop_heals2
    damage2 = 1+dop_damage2
    distanse = 0
    playerx = 1201
    playery = 851
    speed1 = 4
    heals1 = 10
    damage1 = 1
    x1, y1 = 1500, 300
    x2, y2 = -750, 300
    x_rect1, y_rect1 = -3000, 0
    x_rect2, y_rect2 = 3000, 600
    speed_rect1, speed_rect2 = 40, 40
    speed_print1, speed_print2 = 20, 20
    fps = 0
    random_box_damage()
    random_box_healse()
    random_box_speed()
    random_box_TNT()
    create_block()
    game_complete.stop()
    for i in range(200):
        screen.blit(locate,(0,0))
        screen.blit(print_start_raund_right, (x1, y1))
        screen.blit(defolt_skin1, (x1+275, y1))
        screen.blit(print_start_raund_left, (x2, y2))
        screen.blit(skin, (x2 + 275, y2))
        pygame.draw.rect(screen,black,(x_rect1,y_rect1,1500,300))
        pygame.draw.rect(screen, black, (x_rect2, y_rect2, 1500, 600))
        x_rect1=x_rect1+speed_rect1
        x_rect2 = x_rect2 - speed_rect2

        if x_rect1>=-1000:
            speed_rect1=5
        if x_rect1>=-500:
            speed_rect1=40
        if x_rect2<=1000:
            speed_rect2=5
        if x_rect2<=500:
            speed_rect2=40

        x1 = x1 - speed_print1
        x2 = x2 + speed_print2
        if x2>-250:
            speed_print2=5
        if x2>=10:
            speed_print2=0

        if x1<1000:
            speed_print1=5
        if x1<=740:
            speed_print1=0

        pygame.display.update()
    while True:
        keys = pygame.key.get_pressed()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save()
                pygame.quit()
                sys.exit()
        if heals1<=0:
            moneys2=moneys2+1
            kills2 = kills2 + 1
            game_over()
        if heals2<=0:
            moneys1 = moneys1 + 1
            kills1=kills1+1
            game_over()
        if keys[pygame.K_ESCAPE]:
            pause()

        proverka_bullet()

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
        dop_proverka1()
        if keys[pygame.K_LEFT] and playerx >= 10:
            lastdown1 = 'left'
            proverka1(lastdown1, block_massiv)
            if go1 == 1:
                go_left1()
            proverka_box1()

        elif keys[pygame.K_RIGHT] and playerx <= 1440:
            lastdown1 = 'right'
            proverka1(lastdown1, block_massiv)
            if go1 == 1:
                go_right1()
            proverka_box1()

        elif keys[pygame.K_UP] and playery >= 160:
            lastdown1 = 'up'
            proverka1(lastdown1, block_massiv)
            if go1 == 1:
                go_up1()
            proverka_box1()

        elif keys[pygame.K_DOWN] and playery <= 940:
            lastdown1 = 'down'
            proverka1(lastdown1, block_massiv)
            if go1 == 1:
                go_down1()
            proverka_box1()

        else:
            left1 = False
            right1 = False
            up1 = False
            down1 = False
            animcount1 = 0

        dop_proverka2()
        if keys[pygame.K_a] and playerx2 >= 10:
            lastdown2 = 'left'
            proverka2(lastdown2, block_massiv)
            if go2 == 1:
                go_left2()
            proverka_box2()

        elif keys[pygame.K_d] and playerx2 <= 1440:
            lastdown2 = 'right'
            proverka2(lastdown2, block_massiv)
            if go2 == 1:
                go_right2()
            proverka_box2()

        elif keys[pygame.K_w] and playery2 >= 160:
            lastdown2 = 'up'
            proverka2(lastdown2, block_massiv)
            if go2 == 1:
                go_up2()
            proverka_box2()

        elif keys[pygame.K_s] and playery2 <= 940:
            lastdown2 = 'down'
            proverka2(lastdown2, block_massiv)
            if go2 == 1:
                go_down2()
            proverka_box2()
        else:
            left2 = False
            right2 = False
            up2 = False
            down2 = False
            animcount2 = 0

        drawwindow()
while True:
    get_save()
    menu()