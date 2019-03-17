import pygame
background_colour = (0,  0, 0)
(width, height) = (300, 300)

x = 150
y = 150
speed = 0.03

character = pygame.image.load('Sprites/MouseCharacter.png')
imagerect = character.get_rect()


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('kot')


running = True
while running:
  screen.fill(background_colour)
  screen.blit(character, imagerect)
  pygame.display.flip()
  imagerect.center = (x, y)
  keys = pygame.key.get_pressed() 
  
  if keys[pygame.K_SPACE]:
    speed = 0.01
  if keys[pygame.K_SPACE] == False:
    speed = 0.03
  
  if keys[pygame.K_w]:
    x = x + 0
    y = y -speed
  if keys[pygame.K_s]:
    x = x + 0
    y = y + speed
  if keys[pygame.K_a]:
    x = x -speed
    y = y + 0
  if keys[pygame.K_d]:
    x = x + speed
    y = y + 0
  
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False