# -*- coding: utf-8 -*-
# Author: Coaixy

import asyncio
from hashlib import md5
import time
import websockets

from DataWriter import DataWriter

HOST = '127.0.0.1'
PORT = 5000
dw = DataWriter()


async def user_handle(websocket):
    data = await websocket.recv()
    data = str(data)
    datas = data.split("-")  # 1:userName 2: password 3：1/2
    if int(datas[2]) == 1: #新建
        if dw.getUserInfo(datas[0])['password'] == datas[1]:
            temp = str(time.time()).encode('utf-8')
            temp = str(md5(temp).hexdigest())
            dw.createGame(temp,datas[0])
            await websocket.send(temp)
    else: #加入
        game_list = []
        with open(dw.paths[2],'r') as f:
            game_list = f.read().split("\n")
        size = len(game_list)
        for i in range(size,0,-1):
            if str(dw.getGameInfo['state']) == "1":
                await websocket.send(game_list[i])
            else:
                break


async def run(websocket, path):
    while True:
        try:
            if path == "/user":
                await user_handle(websocket)
        except websockets.ConnectionClosed:
            break


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(websockets.serve(run, HOST, PORT))
    asyncio.get_event_loop().run_forever()
