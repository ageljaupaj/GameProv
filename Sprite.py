import pygame

#Character
character = pygame.image.load('Sprites/MouseCharacter.png')
imagerect = character.get_rect()

#Turret
turret = pygame.image.load('Sprites/Turret.png')
turretrect = turret.get_rect()
turretrect2 = turret.get_rect()

#RedBall
RedBall = pygame.image.load('Sprites/RedBall.png')
RedBallrect = RedBall.get_rect()
RedBallrect_2 = RedBall.get_rect()

#Coin
Coin = pygame.image.load('Sprites/Coin.png')
Coinrect = RedBall.get_rect()