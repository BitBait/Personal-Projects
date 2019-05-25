import ruamel.yaml
import pygame
from pygame.locals import FULLSCREEN
import GlobalFunctions

class StartScreenInit:
    def __init__(self):
        YamlParser = ruamel.yaml.YAML()
        ConfigPath = GlobalFunctions.Find("Config.yaml", "../")
        Config = open(ConfigPath, "r")
        self.Config = YamlParser.load(Config)
        self.Config = self.Config["Config"]["Start Menu"]
        self.Resolution = (self.Config["Aspect Ratio"][0] * self.Config["Scale"],
                           self.Config["Aspect Ratio"][1] * self.Config["Scale"])
        if self.Config["FullScreen"]:
            self.FullScreen = FULLSCREEN






class Start(StartScreenInit):
    def __init__(self):
        self.FlashDirection = "Down"
        self.Flash = 256

        super().__init__()

        self.Text = str(self.Config["StartScreenText"])
        self.Logo = str(self.Config["Logo"])

        self.LogoImage = pygame.image.load(self.Logo)

        self.Size = self.Config["TextSize"]
        self.PixelFont = pygame.font.SysFont("basis33", self.Size)

    def TextFlash(self, Surface, Position, Do = True):
        if Do:
            if self.FlashDirection == "Down":
                self.Flash -= 1
            elif self.FlashDirection == "Up":
                self.Flash += 1

            if self.Flash == -1:
                self.FlashDirection = "Up"
                self.Flash += 1
            elif self.Flash == 256:
                self.FlashDirection = "Down"
                self.Flash -= 1

            TextRender = self.PixelFont.render(self.Text, False, (self.Flash, self.Flash, self.Flash))
            Surface.blit(TextRender, Position)


    def ShowLogo(self, Surface, Position):
        Surface.blit(self.LogoImage, Position)
