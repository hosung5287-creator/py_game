import pygame
import py_img
pygame.init()

pygame.display.set_caption("타이핑_야겜 (임시타이틀)")

b_width = 600
b_height = 600
breakground = pygame.display.set_mode((b_width,b_height))


#이미지 
testIMG = pygame.image.load("py_img/00010-3785310329.png")

o_size_width = testIMG.get_size()[0]
o_size_height = testIMG.get_size()[1]

target_height= int(o_size_height * (b_width / o_size_width))


#breakground_size = breakground.get_size()

testIMG = pygame.transform.scale(testIMG,(b_width, target_height))

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    breakground.blit(testIMG, (0,0))
    pygame.display.update()
pygame.quit()

