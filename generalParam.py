import pygame
import helpFunc
import colors
import questions

pygame.init() 
FPS = 60
WIDTH, HEIGHT       = 900, 500                      #Define the sizes of the screen
WIDTHBTN, HEIGHTBTN = 100, 30                       #Define the sizes of the buttons
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))   #Set the screen sizes
########Buttons###########
button_yes              = pygame.Rect(WIDTHBTN, HEIGHT - (HEIGHTBTN*4), WIDTHBTN, HEIGHTBTN) #The buttons are dinamoc to the decided screen page
button_no               = pygame.Rect(WIDTH - (WIDTHBTN*2), HEIGHT - (HEIGHTBTN*4), WIDTHBTN, HEIGHTBTN)
button_restart          = pygame.Rect(WIDTH // 2 - (WIDTHBTN // 2), HEIGHT - (HEIGHTBTN*4), WIDTHBTN, HEIGHTBTN)
# Create the button surface
button_yes_surface      = pygame.Surface((WIDTHBTN, HEIGHTBTN))
button_yes_surface.fill(colors.DARK)
button_no_surface       = pygame.Surface((WIDTHBTN, HEIGHTBTN))
button_no_surface.fill(colors.DARK)
button_restart_surface  = pygame.Surface((WIDTHBTN, HEIGHTBTN))
button_restart_surface.fill(colors.DARK)
# Render the button text
font_button             = pygame.font.SysFont(None, 24)                     # None means default font, 24 is font size
text_yes_surface        = font_button.render("YES", True, colors.BLACK)     # "YES" is the text, the color of the text is black
text_no_surface         = font_button.render("NO", True, colors.BLACK)      # "NO" is the text, the color of the text is black
text_restart_surface    = font_button.render("RESTART", True, colors.BLACK) # "RESTART" is the text, the color of the text is black

# Position the text on the buttons
text_yes_rect       = text_yes_surface.get_rect(center=button_yes_surface.get_rect().center)
text_no_rect        = text_no_surface.get_rect(center=button_no_surface.get_rect().center)
text_restart_rect   = text_restart_surface.get_rect(center=button_restart_surface.get_rect().center)

# Draw the buttons and text
button_yes_surface.blit(text_yes_surface, text_yes_rect)
button_no_surface.blit(text_no_surface, text_no_rect)
button_restart_surface.blit(text_restart_surface, text_restart_rect)

########TextBox###########
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font_text = pygame.font.Font('freesansbold.ttf', 20)
 
# create a text surface object,
# on which text is drawn on it.
lines1  = helpFunc.split_lines(questions.question1)
text1   = font_text.render(lines1[0], True, colors.BLACK, colors.WHITE)
lines2  = helpFunc.split_lines(questions.question2)
text2   = font_text.render(lines2[0], True, colors.BLACK, colors.WHITE)
lines3  = helpFunc.split_lines(questions.question3)
text3   = font_text.render(lines3[0], True, colors.BLACK, colors.WHITE)
lines4  = helpFunc.split_lines(questions.question4)
text4   = font_text.render(lines4[0], True, colors.BLACK, colors.WHITE)
lines5  = helpFunc.split_lines(questions.question5)
text5   = font_text.render(lines5[0], True, colors.BLACK, colors.WHITE)
 
# create a rectangular object for the
# text surface object
textRect = text1.get_rect()
 
# set the center of the rectangular object.
textRect.center = (WIDTH // 2, HEIGHT // 2)
