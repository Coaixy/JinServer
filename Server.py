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
    datas = data.split("-") # 1:userName 2: password
    if dw.getUserInfo(datas[0])['password'] == datas[1]:
        temp = str(time.time()).encode('utf-8')
        temp = str(md5(temp).hexdigest())
        await websocket.send(temp)
    else:
        await websocket.send("")


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