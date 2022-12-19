import pygame


size = (1600,800)
menu_background = "/home/juanm/Documents/Programming/Moon War 2050/images/MenuBackground.png"
logo = "/home/juanm/Documents/Programming/Moon War 2050/images/LogoTerminado.png"
buttonSingle = "/home/juanm/Documents/Programming/Moon War 2050/images/BotonSinglePlayer.png"
buttonMultiplayer = "/home/juanm/Documents/Programming/Moon War 2050/images/botonMultiplayer.png"
meteoro = "/home/juanm/Documents/Programming/Moon War 2050/images/meteoro.png"
backSound = "/home/juanm/Documents/Programming/Moon War 2050/Sound_Efects/Music/backgrundSound.mp3"
clock = pygame.time.Clock()

class moonWar2050:
    def __init__(self):
        pygame.init()
        self.screen1 = pygame.display.set_mode(size)
        self.loaded_menu_background = pygame.image.load(menu_background)
        self.loaded_logo = pygame.image.load(logo)
        self.loaded_buttonSingle = pygame.image.load(buttonSingle)
        self.loaded_buttonMultiplayer = pygame.image.load(buttonMultiplayer)
        self.loaded_meteoro = pygame.image.load(meteoro)
        self.loaded_backSound = pygame.mixer.music.load(backSound)
        pygame.mixer.music.play(-1)
        pygame.display.set_caption("Moon War 2050")
    def start(self):
        state = True
        x = 0
        y = 0
        delta_x = 5
        delta_y = 4
        while state:
            x += delta_x
            y += delta_y
            if x < -80 or x > 1650:
                delta_x *= -1
            if y < -80 or y > 850:
                delta_y *= -1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = False
            self.screen1.blit(self.loaded_menu_background,[0,0])
            self.screen1.blit(self.loaded_meteoro,[x,y])
            self.screen1.blit(self.loaded_logo,[533,50])
            self.screen1.blit(self.loaded_buttonSingle,[533,400])
            self.screen1.blit(self.loaded_buttonMultiplayer,[533,550])
            pygame.display.flip()
            clock.tick(20)
        pygame.quit()

class Button:
    def __init__(self,pos,size,state):
        self.pos = pos
        self.size = size
        self.state = state



        

