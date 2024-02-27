import pygame
import sys
import random


pygame.init()


width = 700
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulation of Roco Kingdom!")
clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsans', 25, False, True)
last = pygame.font.SysFont('comicsans',50,True)

bg = pygame.image.load('bg.jpg')
bg = pygame.transform.scale(bg, (width, height))


class Choice():

  def __init__(self, strpic, b_x,b_y):
    self.t = 55
    self.strpic = strpic
    self.picture = pygame.transform.scale(pygame.image.load(self.strpic), (self.t, self.t))
    self.b_x = b_x
    self.b_y = b_y
  
  def draw(self):
    win.blit(self.picture,(self.b_x, self.b_y))

choices1 = [Choice('placeholder.png',45,45), Choice('attack.jpg',45,45),Choice('heal.png',45,45),Choice('defend.png',45,45)]

choices2 = [Choice('placeholder.png',110,45), Choice('attack.jpg',110,45),Choice('heal.png',110,45),Choice('defend.png',110,45)]

choices3 = [Choice('placeholder.png',175,45), Choice('attack.jpg',175,45),Choice('heal.png',175,45),Choice('defend.png',175,45)]

choices4 = [Choice('placeholder.png',455,45), Choice('attack.jpg',455,45),Choice('heal.png',455,45),Choice('defend.png',455,45)]

choices5 = [Choice('placeholder.png',520,45), Choice('attack.jpg',520,45),Choice('heal.png',520,45),Choice('defend.png',520,45)]

choices6 = [Choice('placeholder.png',585,45), Choice('attack.jpg',585,45),Choice('heal.png',585,45),Choice('defend.png',585,45)]

choices = [choices1,choices2,choices3,choices4,choices5,choices6]

on_screen = [choices[0][0],choices[1][0],choices[2][0],choices[3][0],choices[4][0],choices[5][0]]


class Players:

  def __init__(self, t_x, t_y, picture, b_x, b_y):
    self.t_x = t_x
    self.t_y = t_y
    self.picture = pygame.transform.scale(pygame.image.load(picture), (self.t_x, self.t_y))
    self.b_x = b_x
    self.b_y = b_y
    self.vol = 50
  
  def draw_char(self):
    win.blit(self.picture,(self.b_x, self.b_y))
  
  def turn(self, c, d):
    while True:
      for i in range(1,4):
        on_screen[c]=choices[c][i]
        on_screen[c].draw()
        pygame.display.update()
        event = pygame.event.wait(d)
        if event.type == pygame.MOUSEBUTTONDOWN:
          return 0
        elif event.type == pygame.NOEVENT:
          continue

player = Players(180,160,'dimo.png', 50, 180)


class Bosses:

  def __init__(self, t_x, t_y, picture, b_x, b_y):
    self.t_x = t_x
    self.t_y = t_y
    self.picture = pygame.transform.scale(pygame.image.load(picture), (self.t_x, self.t_y))
    self.b_x = b_x
    self.b_y = b_y
    self.vol = 50
  
  def draw_char(self):
    win.blit(self.picture,(self.b_x, self.b_y))

  def turn(self):
    for i in range(3,6):
      c = random.randrange(1,4)
      on_screen[i]=choices[i][c]
      on_screen[i].draw()
      pygame.display.update()
      pygame.time.delay(800)

boss = Bosses(250,200,'boss.png', 415,140)


class Player_health:

  def __init__(self,y):
    self.s_color = (154,154,154)
    self.dl_color = (125,0,0)
    self.ds_color = (0,0,150)
    self.x = 70
    self.y = y
    self.w = 150
    self.d_w = 150
    self.i_w = 0
    self.h = 20
    self.l_score = font.render(str(self.d_w//5)+"/30",1,(0,0,0))
    self.s_score = font.render(str(self.i_w//5)+"/30",1,(0,0,0))

  def draw_life(self):
    pygame.draw.rect(win, self.s_color,(self.x,self.y,self.w,self.h))
    pygame.draw.rect(win, self.dl_color,(self.x,self.y,self.d_w,self.h))
    win.blit(self.l_score, ((self.x+self.w+5),self.y))

  def draw_shield(self):
    pygame.draw.rect(win, self.s_color,(self.x,self.y,self.w,self.h))
    pygame.draw.rect(win, self.ds_color,(self.x,self.y,self.i_w,self.h))
    win.blit(self.s_score, ((self.x+self.w+5),self.y))  

player_life = Player_health(370)
player_shield = Player_health(400)


class Boss_health():

  def __init__(self, y):
    self.s_color = (154,154,154)
    self.dl_color = (125,0,0)
    self.ds_color = (0,0,150)
    self.x = 480
    self.y = y
    self.w = 150
    self.d_w = 150
    self.i_w = 0
    self.h = 20
    self.l_score = font.render(str(self.d_w//5)+"/30",1,(0,0,0))
    self.s_score = font.render(str(self.i_w//5)+"/30",1,(0,0,0))

  def draw_life(self):
    pygame.draw.rect(win, self.s_color,(self.x,self.y,self.w,self.h))
    pygame.draw.rect(win, self.dl_color,(self.x,self.y,self.d_w,self.h))
    win.blit(self.l_score, ((self.x+self.w+5),self.y))

  def draw_shield(self):
    pygame.draw.rect(win, self.s_color,(self.x,self.y,self.w,self.h))
    pygame.draw.rect(win, self.ds_color,(self.x,self.y,self.i_w,self.h))
    win.blit(self.s_score, ((self.x+self.w+5),self.y))

boss_life = Boss_health(370)
boss_shield = Boss_health(400)


def redraw_main():
  win.blit(bg, (0,0))
  player.draw_char()
  boss.draw_char()

  player_life.draw_life()
  player_shield.draw_shield()
  boss_life.draw_life()
  boss_shield.draw_shield()

  on_screen[0].draw()
  on_screen[1].draw()
  on_screen[2].draw()
  on_screen[3].draw()
  on_screen[4].draw()
  on_screen[5].draw()

  pygame.display.update()


def redraw_pc():
  c = 0
  d = 500
  while c < 3:
    while True:
      event = pygame.event.wait(200)
      if event.type == pygame.MOUSEBUTTONDOWN:
        player.turn(c, d)
        break
    c+=1 
    d-=150   


def redraw_bc():
  if on_screen[3].strpic == 'placeholder.png':
    boss.turn()


def result_pc(i):
  if on_screen[i].strpic == 'attack.jpg':
    if boss_shield.i_w == 0:
      boss_life.d_w -= player.vol
      boss_life.l_score = font.render(str(boss_life.d_w//5)+"/30",1,(0,0,0))
      redraw_main()
    elif boss_shield.i_w < player.vol:
      rest = player.vol - boss_shield.i_w
      boss_shield.i_w = 0
      boss_life.d_w -= rest
      boss_life.l_score = font.render(str(boss_life.d_w//5)+"/30",1,(0,0,0))
      boss_shield.s_score = font.render(str(boss_shield.i_w//5)+"/30",1,(0,0,0))
      redraw_main()
    else:
      boss_shield.i_w -= player.vol
      boss_shield.s_score = font.render(str(boss_shield.i_w//5)+"/30",1,(0,0,0))
      redraw_main()

  elif on_screen[i].strpic == 'heal.png':
    if player_life.d_w != 150:
      player_life.d_w += player.vol
      player_life.l_score = font.render(str(player_life.d_w//5)+"/30",1,(0,0,0))
      redraw_main()

  elif on_screen[i].strpic == 'defend.png':
    if player_shield.i_w != 150:
      player_shield.i_w += player.vol
      player_shield.s_score = font.render(str(player_shield.i_w//5)+"/30",1,(0,0,0))
      redraw_main()

  on_screen[i] = choices[i][0]
  on_screen[i].draw()


def result_bc(i):
  if on_screen[i].strpic == 'attack.jpg':
    if player_shield.i_w == 0:
      player_life.d_w -= boss.vol
      player_life.l_score = font.render(str(player_life.d_w//5)+"/30",1,(0,0,0))
      redraw_main()
    elif player_shield.i_w < boss.vol:
      rest = boss.vol - player_shield.i_w
      player_shield.i_w = 0
      player_life.d_w -= rest
      player_life.l_score = font.render(str(player_life.d_w//5)+"/30",1,(0,0,0))
      player_shield.s_score = font.render(str(player_shield.i_w//5)+"/30",1,(0,0,0))
      redraw_main()
    else:
      player_shield.i_w -= boss.vol
      player_shield.s_score = font.render(str(player_shield.i_w//5)+"/30",1,(0,0,0))
      redraw_main()

  elif on_screen[i].strpic == 'heal.png':
    if boss_life.d_w != 150:
      boss_life.d_w += boss.vol
      boss_life.l_score = font.render(str(boss_life.d_w//5)+"/30",1,(0,0,0))
      redraw_main()

  elif on_screen[i].strpic == 'defend.png':
    if boss_shield.i_w != 150:
      boss_shield.i_w += boss.vol
      boss_shield.s_score = font.render(str(boss_shield.i_w//5)+"/30",1,(0,0,0))
      redraw_main()

  on_screen[i] = choices[i][0]
  on_screen[i].draw()


ins = pygame.transform.scale(pygame.image.load('ins.jpg'),(width, height))

header = pygame.font.SysFont('comicsans', 50, True)
sub = pygame.font.SysFont('comicsans', 35, True,True)
text = pygame.font.SysFont('comicsans', 30)

i1 = Choice('heal.png',60,150)
i2 = Choice('defend.png',60,250)
i3 = Choice('attack.jpg',60,350)

#instruction
while True:
  win.blit(ins, (0,0))
  win.blit(header.render("Playing Instructions",1,(250,250,250)), (150,30))
  win.blit(sub.render("Click to activate/stop the wheel",1,(0,0,250)), (150,90))
  i1.draw()
  win.blit(text.render("This bottle will increase you blood, the red rectangle.",1,(0,0,250)), (150,150))
  win.blit(text.render("Game ends when your or enemy's blood empties.",1,(0,0,250)),(150,180))
  i2.draw()
  win.blit(text.render("The shield will increase the blue rectangle.",1,(0,0,250)), (150,265))
  i3.draw()
  win.blit(text.render("The sword can decrease the blue and red rectangle.",1,(0,0,250)), (150,355))
  win.blit(text.render("The sword will first clear the shield, then the blood.",1,(0,0,250)), (150,385))
  win.blit(sub.render("Click to continue",1,(250,0,0)), (240,440))
  pygame.display.update()

  event = pygame.event.wait(200)
  if event.type == pygame.MOUSEBUTTONDOWN:
    break


round_count = 1

#main loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  redraw_main()

  win.blit(last.render("Round " + str(round_count),1,(0,0,0)),(width//2-70,height//2))
  pygame.display.update()
  
  redraw_pc()
  redraw_bc()

  result_pc(0)
  pygame.display.update()
  pygame.time.delay(600)
  result_pc(1)
  pygame.display.update()
  pygame.time.delay(600)
  result_pc(2)
  pygame.display.update()
  pygame.time.delay(600)
  if boss_life.d_w == 0:
    win.blit(last.render("You Win!",1,(0,0,0)),(width//2-80,height//2))
    pygame.display.update()
    pygame.time.delay(600)
    break

  result_bc(3)
  pygame.display.update()
  pygame.time.delay(600)
  result_bc(4)
  pygame.display.update()
  pygame.time.delay(600)
  result_bc(5)
  pygame.display.update()
  pygame.time.delay(600)
  if player_life.d_w == 0:
    win.blit(last.render("You Lose!",1,(0,0,0)),(width//2-90,height//2))
    pygame.display.update()
    pygame.time.delay(600)
    break
  
  pygame.display.update()
  clock.tick(100)
  round_count +=1


pygame.quit()
sys.exit()