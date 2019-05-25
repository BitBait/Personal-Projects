import ruamel.yaml
import pygame
from pygame.locals import FULLSCREEN
import GlobalFunctions
import glob, os

pygame.init()

class MenuScreenInit:
    def __init__(self):
        YamlParser = ruamel.yaml.YAML()
        ConfigPath = GlobalFunctions.Find("Config.yaml", "../")
        Config = open(ConfigPath, "r")
        self.Config = YamlParser.load(Config)
        self.Config = self.Config["Config"]["Main Menu"]


class Menu(MenuScreenInit):
    def __init__(self):
        super().__init__()
        self.Size = self.Config["TitleSize"]
        self.PixelFont = pygame.font.SysFont("basis33", self.Size)



    def ListGames(self):
        YamlParser = ruamel.yaml.YAML()
        self.GamesList = []
        for files in os.listdir("Games"):
            for file in os.listdir("Games/" + files):
                if file.endswith("Yaml"):
                    TempConfig = open(os.path.join("Games/" + files + "/" + file), "r")
                    TempConfig = YamlParser.load(TempConfig)
                    Game = TempConfig["Information"]["Name"]
                    self.GamesList.append(Game)
        return self.GamesList

    def ShowGames(self, Screen, Position, GamesList): #TODO Change screen to surface in all of these
        self.GamesList = GamesList
        for Game in self.GamesList:
            TextRender = self.PixelFont.render(Game , False, (255, 255, 255))
            Screen.blit(TextRender, Position)
            Position[1] += self.PixelFont.size(Game)[1]
            global BigTextSize
            BigTextSize = self.PixelFont.size(Game)

    def BlackGame(self, Screen, Position, GamesList, Selector):
        self.GamesList = GamesList
        TextRender = self.PixelFont.render(GamesList[Selector], False, (0, 0, 0))
        Screen.blit(TextRender, Position)

    def GetTextSize(self, GamesList):
        self.GamesList = GamesList
        for Game in self.GamesList[0]:
            BigTextSize = self.PixelFont.size(Game)
        return BigTextSize

    def VideoList(self):
        YamlParser = ruamel.yaml.YAML()
        self.VideoList = []
        for files in os.listdir("Games"):
            for file in os.listdir("Games/" + files):
                if file.endswith("Yaml"):
                    TempConfig = open(os.path.join("Games/" + files + "/" + file), "r")
                    TempConfig = YamlParser.load(TempConfig)
                    Game = TempConfig["Information"]["Video"]
                    self.VideoList.append(Game)
        return self.VideoList











