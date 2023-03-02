import pygame
import generalParam
import colors

pygame.init() 
########ScreenUpdate###########
def draw_set(lines):
    for i in range(len(lines)):
            text            = generalParam.font_text.render(lines[i], True, colors.BLACK, colors.WHITE)
            textRect        = text.get_rect()
            textRect.center = (generalParam.WIDTH // 2, generalParam.HEIGHT // 4 + (i*generalParam.HEIGHTBTN))
            generalParam.SCREEN.blit(text, textRect)

def draw_window(question, day):
    q_img = pygame.image.load('/Users/royvaygue/PycharmProjects/helloWorld/assets/question mark background.jpeg')  #loads packground picture
    q_img = pygame.transform.scale(q_img,(generalParam.WIDTH,generalParam.HEIGHT))                                                    #Scale the picture to the screen
    generalParam.SCREEN.blit(q_img,(0,0))
    generalParam.SCREEN.blit(generalParam.button_yes_surface, generalParam.button_yes)
    generalParam.SCREEN.blit(generalParam.button_no_surface, generalParam.button_no)
    if(question==0):
        draw_set(generalParam.lines1)
    if(question==1):
        draw_set(generalParam.lines2)
    if(question==2):
        draw_set(generalParam.lines3)
    if(question==3):
        draw_set(generalParam.lines4)
    if(question==4):
        draw_set(generalParam.lines5)
    pygame.display.update()

def draw_conclution(day):
    bd_img = pygame.image.load('/Users/royvaygue/PycharmProjects/helloWorld/assets/birthday-background.webp')  #loads packground picture
    bd_img = pygame.transform.scale(bd_img,(generalParam.WIDTH,generalParam.HEIGHT))                                              #Scale the picture to the screen
    generalParam.SCREEN.blit(bd_img,(0,0))
    result = "your birth day is : " + str(day)
    finaltext = generalParam.font_text.render(result, True, colors.DARK)
    # create a rectangular object for the
    # text surface object
    textRect = finaltext.get_rect()
    # set the center of the rectangular object.
    textRect.center = (generalParam.WIDTH // 2, generalParam.HEIGHT // 2)
    generalParam.SCREEN.blit(finaltext, textRect)
    generalParam.SCREEN.blit(generalParam.button_restart_surface, generalParam.button_restart)
    pygame.display.update()
