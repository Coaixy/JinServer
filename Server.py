# -*- coding: utf-8 -*-
# Author: XiaoXinYo

import asyncio
import websockets
import json

HOST = '127.0.0.1'
PORT = 5000


async def handle(websocket):
    print('连接成功')


async def run(websocket, path):
    while True:
        try:
            await handle(websocket)
        except websockets.ConnectionClosed:
            print('断开连接')
            break


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(websockets.serve(run, HOST, PORT))
    loop.run_forever()
