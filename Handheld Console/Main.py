#This is the main script which is the control loop that the program follows
import StartScreen, pygame, ruamel.yaml, GlobalFunctions, MenuScreen, time, os, subprocess
from pygame.locals import *
from Colours.BasicColours import *


pygame.init()


_StartScreen_= StartScreen.StartScreenInit()
Resolution = _StartScreen_.Resolution
Screen = pygame.display.set_mode(Resolution ,_StartScreen_.FullScreen)


YamlParser = ruamel.yaml.YAML()
ConfigPath = GlobalFunctions.Find("Config.yaml", "/.")
Config = open(ConfigPath, "r")
Config = YamlParser.load(Config)


_StartScreenText_ = StartScreen.Start()
TextSize = _StartScreenText_.PixelFont.size("Press Any Key To Continue")
ImageSize = _StartScreenText_.LogoImage.get_size()

#Menu Class
MainMenu = MenuScreen.MenuScreenInit()
_MainMenu_ = MenuScreen.Menu()
AllGames = _MainMenu_.ListGames()

#BigTextHeight
BigTextHeight = _MainMenu_.GetTextSize(AllGames)[1]

#For Main Menu
Selector = 0
SelectorPos = [0, 0]

#For Gif Loading By Frame
AllVideo = _MainMenu_.VideoList()
Frame = 0

InStartScreen = True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()
    while InStartScreen:
        Screen.fill(Black)
        _StartScreenText_.TextFlash(Screen, ((Resolution[0] / 2) - (TextSize[0] / 2), (Resolution[1] * 0.85)))
        _StartScreenText_.ShowLogo(Screen, ((Resolution[0] / 2) - (ImageSize[0] / 2), (Resolution[1] * 0.20)))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                else:
                    InStartScreen = False
                    InMainMenu = True
                    SelectorSurface = pygame.Surface((260, 51))         #TODO Make height of text
                    SelectorSurface.fill(White)

    while InMainMenu:
        print(Selector)
        Screen.fill(Black)
        _MainMenu_.ShowGames(Screen, [0,0], AllGames)
        Screen.blit(SelectorSurface, SelectorPos)
        _MainMenu_.BlackGame(Screen, SelectorPos, AllGames, Selector)
        VideoLocation = AllVideo[Selector]
        #print(VideoLocation)
        #print(str(VideoLocation) + str(Frame) + ".gif")
        SpecificFrame = (str(VideoLocation) + str(Frame) + ".gif")
        FrameSurface = pygame.image.load(SpecificFrame)
        Screen.blit(FrameSurface, (260,0))
        pygame.display.flip()
        Frame += 1
        if Frame > 500:
            Frame = 1
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()

                elif event.key == K_DOWN:
                    Frame = 0
                    Selector += 1
                    SelectorPos[1] += 51 #TODO Make height of text

                elif event.key == K_UP:
                    Frame = 0
                    Selector -= 1
                    SelectorPos[1] -= 51 #TODO Make height of text

                elif event.key == K_BACKSPACE:
                    PathToGame = os.path.join("Games." + str(AllGames[Selector]) + "." + "Main")
                    exec("import " + PathToGame)

        time.sleep(0.02)





