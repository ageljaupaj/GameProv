import pygame
from settings import *
from Sprite import *


                   
#Game's windowd
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('kot')

playermoving = False

running = True
while running:
  #Ndertimi i lojes(Backgrounds, pngs, rect etc.)
  screen.fill(background_colour)
  screen.blit(character, imagerect)
  screen.blit(turret, turretrect)
  screen.blit(turret, turretrect2)
  turretrect2.center = (290, 150)
  screen.blit(Coin, Coinrect)
  Coinrect.center = (COINx, COINy)
  imagerect.center = (x, y)
  turretrect.center = (150, 15)
  RedBallrect.center = (RedBAll_x, RedBAll_y)
  RedBallrect_2.center = (RedBall_2_x, RedBall_2_y)
  keys = pygame.key.get_pressed() 
  #Perplasia ne mure 
  if x < 10:
    x = x + speed
  if x > 290:
    x = x - speed
  if y < 10:
    y = y + speed
  if y > 290:
    y = y - speed
  #RedBallat
  if playermoving:
    screen.blit(RedBall, RedBallrect)
    RedBAll_y = RedBAll_y + ball_speed
    screen.blit(RedBall, RedBallrect_2)
    RedBall_2_x = RedBall_2_x - ball_speed
    
  #Slowmotion
  if keys[pygame.K_SPACE]:
    speed = 0.015
    ball_speed = 0.01
  
  if keys[pygame.K_SPACE] == False:
    speed = 0.03
    ball_speed = 0.035
  #Movement
  if keys[pygame.K_w]: 
    x = x + 0
    y = y -speed
    playermoving = True
  if keys[pygame.K_s]:
    x = x + 0
    y = y + speed
    playermoving = True
  if keys[pygame.K_a]:
    x = x -speed
    y = y + 0
    playermoving = True
  if keys[pygame.K_d]:
    x = x + speed
    y = y + 0
    playermoving = True
  #Kthimi prap i Redballit 
  if RedBAll_y > 310:
    RedBAll_x = 150
    RedBAll_y = 35
  if RedBAll_y < -10:
    RedBAll_x = 150
    RedBAll_y = 35
  if RedBAll_x < -10:
    RedBAll_x = 150
    RedBAll_y = 35
  if RedBAll_x > 310:
    RedBAll_x = 150
    RedBAll_y = 35
    
  if RedBall_2_y > 310:
    RedBall_2_x = 290
    RedBall_2_y = 150
  if RedBall_2_y < -10:
   RedBall_2_x = 290
   RedBall_2_y = 150
  if RedBall_2_x < -10:
    RedBall_2_x = 290
    RedBall_2_y = 150
  if RedBall_2_x > 310:
    RedBall_2_x = 290
    RedBall_2_y = 150
  #Collusion
  if RedBallrect.colliderect(imagerect):
    RedBAll_x = 150
    RedBAll_y = 35
    life = life - 1
    print('You are left with', life, 'HP!')

  if RedBallrect_2.colliderect(imagerect):
    RedBall_2_x = 290
    RedBall_2_y = 150
    life = life - 1
    if life > 0:
      print('You are left with', life, 'HP!')
    if life == 0:
      print("You Died!")
  
  if imagerect.colliderect(Coinrect):
    COINx = random.uniform(20, 280)
    COINy = random.uniform(20, 280)
    score = score + 1
    
  #Jeta
  if life == 0:
    print('Your score score is', score, "!")
    running = False
    
  pygame.display.flip()
  #Game's close
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      