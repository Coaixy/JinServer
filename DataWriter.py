import json
import sys


class DataWriter:
    game_type = 0  # 0:用户信息，1:对局信息 2:对局列表
    paths = [sys.path[0] + "\\user_info", sys.path[0] +
             "\\game_info", sys.path[0] + "\\game_info\\list.txt"]
    path = paths[game_type]

    def __init__(self):
        pass

    def getUserInfo(self, user_name):
        if self.game_type != 0:
            self.game_type = 0
            self.path = self.paths[self.game_type]
        with open(self.path+"\\"+user_name+".json", 'r') as f:
            data = json.load(f)
            return data

    def getGameInfo(self, ugid):
        if self.game_type != 1:
            self.game_type = 1
            self.path = self.paths[self.game_type]
        with open(self.path+"\\"+ugid+".json", 'r') as f:
            data = json.load(f)
            return data

    def getGameList(self):
        if self.game_type != 2:
            self.game_type = 2
            self.path = self.paths[self.game_type]
        with open(self.path, 'r') as f:
            return f.read().split("\n")

    def createGame(self, ugid, user_name):
        with open(self.paths[2], 'w+') as f:
            f.write(f.read()+"\n"+ugid)
        data = {}
        with open(self.paths[1]+"\\template.json", 'r') as f:
            data = json.load(f)
        data['state'] = "1"
        data['Ugid'] = ugid
        data['Game_Info']['u1'] = user_name
        
    