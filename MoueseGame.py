import pygame, sys
import random

from settings import *
from Sprite import *

pygame.init()

                 
#Game's windowd
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game')

playermoving = False
#screen.blit(pista, pista_rect)
#pista_rect.center = (200, 200)

player_3Hp = True
player_2Hp = True
player_1Hp = True

Start_up = True
Dead = False
running = True


while running:
  screen.fill(background_colour)
  if Start_up:
    screen.blit(pista, pista_rect) 
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          Start_up = False
      if event.type == pygame.QUIT:
        running = False

  elif life == 0:
    screen.blit(pista, pista_rect)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          life = 3
          player_3Hp = True
          player_2Hp = True
          player_1Hp = True
          x = 150
          y = 150
          RedBAll_x = 150
          RedBAll_y = 35
          RedBall_2_x = 265
          RedBall_2_y = 150
          RedBall_2_x_1 = 265
          RedBall_2_y_1 = 150
          RedBall_2_x_2 = 265
          RedBall_2_y_2 = 150
          
      if event.type == pygame.QUIT:
        running = False
    
  else:
  #Ndertimi i lojes(Backgrounds, pngs, rect etc.)
    screen.blit(character, imagerect)
    screen.blit(turret, turretrect)
    screen.blit(turret2, turretrect2)
    turretrect2.center = (285, 150)
    screen.blit(Coin, Coinrect)
    Coinrect.center = (COINx, COINy)
    imagerect.center = (x, y)
    turretrect.center = (150, 15)
    RedBallrect.center = (RedBAll_x, RedBAll_y)
    RedBallrect_2.center = (RedBall_2_x, RedBall_2_y)
    RedBallrect_2_1.center = (RedBall_2_x_1, RedBall_2_y_1)
    RedBallrect_2_2.center = (RedBall_2_x_2, RedBall_2_y_2)
    screen.blit(EmptyHeart, EmptyHeart_rect)
    EmptyHeart_rect.center = (20, 20)
    screen.blit(EmptyHeart, EmptyHeart_rect_2)
    EmptyHeart_rect_2.center = (40, 20)
    screen.blit(EmptyHeart, EmptyHeart_rect_3)
    EmptyHeart_rect_3.center = (60, 20)
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
      screen.blit(RedBall, RedBallrect_2_1)
      screen.blit(RedBall, RedBallrect_2_2)
      RedBall_2_x = RedBall_2_x - ball_speed
      RedBall_2_x_1 = RedBall_2_x_1 - ball_speed
      RedBall_2_x_2 = RedBall_2_x_2 - ball_speed
      RedBall_2_y_1 = RedBall_2_y_1 - ball_sec_speed 
      RedBall_2_y_2 = RedBall_2_y_2 + ball_sec_speed 
      
    
  #Slowmotion
    if keys[pygame.K_SPACE]:
      speed = 0.015
      ball_speed = 0.01
      ball_sec_speed = 0.003
  
    if keys[pygame.K_SPACE] == False:
      speed = 0.03 
      ball_speed = 0.035
      ball_sec_speed = 0.01
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
      RedBall_2_x = 265
      RedBall_2_y = 150
    if RedBall_2_y < -10:
      RedBall_2_x = 265
      RedBall_2_y = 150
    if RedBall_2_x < -10:
      RedBall_2_x = 265
      RedBall_2_y = 150
    if RedBall_2_x > 310:
      RedBall_2_x = 265
      RedBall_2_y = 150

    if RedBall_2_y_1 > 310:
      RedBall_2_x_1 = 265
      RedBall_2_y_1 = 150
    if RedBall_2_y_1 < -10:
      RedBall_2_x_1 = 265
      RedBall_2_y_1 = 150
    if RedBall_2_y_1 < -10:
      RedBall_2_x_1 = 265
      RedBall_2_y_1 = 150
    if RedBall_2_y_1 > 310:
      RedBall_2_x_1 = 265
      RedBall_2_y_1 = 150

    if RedBall_2_y_2 > 310:
      RedBall_2_x_2 = 265
      RedBall_2_y_2 = 150
    if RedBall_2_y_2 < -10:
      RedBall_2_x_2 = 265
      RedBall_2_y_2 = 150
    if RedBall_2_y_2 < -10:
      RedBall_2_x_2 = 265
      RedBall_2_y_2 = 150
    if RedBall_2_y_2 > 310:
      RedBall_2_x_2 = 265
      RedBall_2_y_2 = 150

  #Collusion
    if RedBallrect.colliderect(imagerect):
      RedBAll_x = 150
      RedBAll_y = 35
      life = life - 1

    if RedBallrect_2.colliderect(imagerect):
      RedBall_2_x = 290
      RedBall_2_y = 150
      life = life - 1

    if RedBallrect_2_1.colliderect(imagerect):
      RedBall_2_x_1 = 290
      RedBall_2_y_1 = 150
      life = life - 1
    
    if RedBallrect_2_2.colliderect(imagerect):
      RedBall_2_x_2 = 290
      RedBall_2_y_2 = 150
      life = life - 1
  
    if imagerect.colliderect(Coinrect):
      COINx = random.uniform(20, 280)
      COINy = random.uniform(20, 280)
      score = score + 1
    
  #Jeta
    if life == 2:
      player_3Hp = False
    if life == 1:
      player_2Hp = False
    if life == 0:
      player_1Hp = False
      print(score)
      score = 0
      
      
    if player_1Hp:
      screen.blit(FullHeart, FullHeart_rect)
      FullHeart_rect.center = (20, 20)
    if player_2Hp:
      screen.blit(FullHeart, FullHeart_rect_2)
      FullHeart_rect_2.center = (40, 20)
    if player_3Hp:
      screen.blit(FullHeart, FullHeart_rect_3)
      FullHeart_rect_3.center = (60, 20)
    
  #Game's close
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
  
  pygame.display.flip()
        
    

  
  

