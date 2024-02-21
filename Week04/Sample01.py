import pygame as pg

pg.init()
win_width = 1000
win_height = 500
win = pg.display.set_mode([win_width, win_height])
background_color = (255,255,255)
background_img01 = pg.image.load("./background.png")
bgImg_xPos = 0
bgImg_yPos = 0


temp = 0
con = True
while con:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            con = False

    win.fill(background_color)
    win.blit(background_img01, (bgImg_xPos, bgImg_yPos))
    bgImg_xPos = bgImg_xPos - 5;
    pg.display.update()
    

pg.quit()

