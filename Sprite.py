import pygame

#rotate img
def rot_center(image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect
        
#Character
character = pygame.image.load('Sprites/MouseCharacter.png')
imagerect = character.get_rect()

#Turret
turret = pygame.image.load('Sprites/Turret.png')
turretrect = turret.get_rect()
turret2, turretrect2 = rot_center(turret, turretrect, -90)


#RedBall
RedBall = pygame.image.load('Sprites/RedBall.png')
RedBallrect = RedBall.get_rect()
RedBallrect_2 = RedBall.get_rect()


#Coin
Coin = pygame.image.load('Sprites/Coin.png')
Coinrect = Coin.get_rect()

#map
pista = pygame.image.load('Sprites/Map000.jpg')
pista_rect = pista.get_rect()

#Heart and empty heart
FullHeart = pygame.image.load('Sprites/HeartFull.png')
FullHeart_rect = FullHeart.get_rect()
FullHeart_rect_2 = FullHeart.get_rect()
FullHeart_rect_3 = FullHeart.get_rect()

EmptyHeart = pygame.image.load('Sprites/EmptyHeart.png')
EmptyHeart_rect = EmptyHeart.get_rect()
EmptyHeart_rect_2 = EmptyHeart.get_rect()
EmptyHeart_rect_3 = EmptyHeart.get_rect()
