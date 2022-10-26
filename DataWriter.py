import json


class DataWriter:
    type = 0  # 0:用户信息，1:对局信息 2:对局列表
    data = {'type': type}

    def __init__(self, type):
        self.type = type
        self.data[type] = type
