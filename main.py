from time import sleep
import pygame
from pygame import mixer
import helpFunc
import generalParam
import screenUpdate

pygame.init() 
mixer.init()

pygame.display.set_caption("gues birth day")                        #Name the display

def main():
    clock       = pygame.time.Clock()                               #We want the app to run in the same frequency (60 FPS), and not based on the computer speed
    day         = 0
    question    = 0
    run         = True
    while run:
        clock.tick(generalParam.FPS)                                #We want the app to run in the same frequency (60 FPS), and not based on the computer speed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                           #If the window is closed we want to stop the runnong of the app
                run = False

        if question < 5:                                            #If we have the result we want to show it on the screen
            screenUpdate.draw_window(question,day)
        else:
            screenUpdate.draw_conclution(day)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if generalParam.button_yes.collidepoint(mouse_pos):     #Recognising yes button press
                helpFunc.play_sound('/Users/royvaygue/PycharmProjects/helloWorld/assets/yes-sound.mp3')
                day         = day+pow(2,question)                   #Based on the questions adding the correct ammount to the answer
                question    = question+1
                print("YES!")
                sleep(0.4) 
            if generalParam.button_no.collidepoint(mouse_pos):       #Recognising no button press
                helpFunc.play_sound('/Users/royvaygue/PycharmProjects/helloWorld/assets/no-sound.mp3')
                question    = question+1
                print("NO!")
                sleep(0.4)
            if generalParam.button_restart.collidepoint(mouse_pos): #Recognising restart button press
                print(day)
                question    = 0                                     #Restarting parameters
                day         = 0                                     #Restarting parameters
                print("RESTARTED")
                sleep(0.4)
            if question == 5:
                helpFunc.play_sound('/Users/royvaygue/PycharmProjects/helloWorld/assets/happy-birthday.mp3')
                question    = question+1

    pygame.quit()

if __name__ == "__main__":
    main()
