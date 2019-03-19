import pygame
background_colour = (35, 35, 35)
(width, height) = (300, 300)

x = 150
y = 150

life = 3


RedBAll_x = 150
RedBAll_y = 35

ball_speed = 0.03
speed = 0.03

character = pygame.image.load('Sprites/MouseCharacter.png')
imagerect = character.get_rect()

turret = pygame.image.load('Sprites/Turret.png')
turretrect = turret.get_rect()

RedBall = pygame.image.load('Sprites/RedBall.png')
RedBallrect = RedBall.get_rect()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('kot')

playermoving = False

running = True
while running:
  screen.fill(background_colour)
  screen.blit(character, imagerect)
  screen.blit(turret, turretrect)
  imagerect.center = (x, y)
  turretrect.center = (150, 15)
  RedBallrect.center = (RedBAll_x, RedBAll_y)
  keys = pygame.key.get_pressed() 
  
  if x < 10:
    x = x + speed
  if x > 290:
    x = x - speed
  if y < 10:
    y = y + speed
  if y > 290:
    y = y - speed
  
  if playermoving:
    screen.blit(RedBall, RedBallrect)
    RedBAll_y = RedBAll_y + ball_speed
    

  if keys[pygame.K_SPACE]:
    speed = 0.015
    ball_speed = 0.01
  
  if keys[pygame.K_SPACE] == False:
    speed = 0.03
    ball_speed = 0.03
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

  if RedBallrect.colliderect(imagerect):
    RedBAll_x = 150
    RedBAll_y = 35
    life = life - 1
    print(life)

  if life < 1:
    running = False
    
  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False