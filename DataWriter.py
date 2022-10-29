import json
import sys

class DataWriter:
    write_type = 0 # 0：写 1：读取
    game_type = 0  # 0:用户信息，1:对局信息 2:对局列表
    path = sys.path[0]
    data = dict()

    def __init__(self, type):
        self.game_type = type
        if self.game_type == 0:
            self.path = self.path + "\\user_info"
        elif self.game_type == 1:
            self.path = self.path + "\\game_info"
        else:
            self.path = self.path + "\\game_info\\list.txt"
    