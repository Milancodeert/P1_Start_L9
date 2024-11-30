import pygame, sys
from pygame.locals import QUIT
eersteCombinatie = int(input("wat wil je als achtergrond hebben? (tik de eerste kleur in van de kleur in python) "))
tweedeCombinatie = int(input("tik hetzelfde in, maar dan de tweede combinatie. "))
derdeCombinatie = int(input("tik hetzelfde in, maar dan de derde combinatie. "))
pygame.init()
venster = pygame.display.set_mode((600, 500))
venster.fill((eersteCombinatie,tweedeCombinatie,derdeCombinatie))
tekengrootte = 10
#def extraGrootte():
 #   if event.type == pygame.MOUSEWHEEL:
  #      if event.y == -1:
   #         tekengrootte -= 1







while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if pygame.mouse.get_pressed() == (True,False,False):
            pygame.draw.circle(venster,color,pygame.mouse.get_pos(),tekengrootte)
        if pygame.mouse.get_pressed() == (False,False,True):
            pygame.draw.circle(venster,(eersteCombinatie,tweedeCombinatie,derdeCombinatie),pygame.mouse.get_pos(),10)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (255,0,0)
            if event.key == pygame.K_s:
                pygame.image.save(venster,"tekening" + ".jpg")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (0, 0, 0)
            if event.key == pygame.K_s:
                pygame.image.save(venster, "tekening" + ".jpg")
        if event.type == pygame.MOUSEWHEEL:
            if event.y == -1:
                tekengrootte -= 1
        if event.type == pygame.MOUSEWHEEL:
            if event.y == +1:
                tekengrootte += 1


    pygame.display.update()
