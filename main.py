import cv2 as cv
import discord
import numpy
from matplotlib import pyplot as plt
import asyncio
import time

OUTPUT_WIDTH = 32
OUTPUT_HEIGHT = 24
BLOCK_FULL = "█"
BLOCK_HALF = "▒"
BLOCK_EMPTY = "⠀"
BLOCK_BLACK = ":black_large_square:"
BLOCK_WHITE = ":white_large_square:"




token = ""

"""
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content == 'start':

            while video.isOpened():
                ret, frame = video.read()
                if ret:

                    ret, frame = cv.threshold(cv.resize(frame, (OUTPUT_WIDTH, OUTPUT_HEIGHT)), 127, 255,
                                              cv.THRESH_BINARY)

                    cv.imshow('Frame', frame)

                    await asyncio.sleep(1)

                    response = '0'

                    for y in range(OUTPUT_HEIGHT):
                        for x in range(OUTPUT_WIDTH):

                            # print(frame[y][x][0], end=' ')

                            response += x

                            if x == OUTPUT_WIDTH - 1:
                                # print('\n')
                                response += '\n'

                        await message.channel.send(response)

                    if cv.waitKey(25) & 0xFF == ord('q'):
                        break
                else:
                    break

            video.release()


video = cv.VideoCapture('bad.mp4', cv.IMREAD_GRAYSCALE)

frames_num = int(video.get(cv.CAP_PROP_FRAME_COUNT))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
"""
video = cv.VideoCapture('bad.mp4', cv.IMREAD_GRAYSCALE)
fps = video.get(cv.CAP_PROP_FPS)

while video.isOpened():
    ret, frame = video.read()
    if ret:

        ret, frame = cv.threshold(cv.resize(frame, (OUTPUT_WIDTH, OUTPUT_HEIGHT)), 127, 255,
                                  cv.THRESH_BINARY)

        time.sleep(0.017)

        cv.imshow('Frame', frame)

        response = ''

        for y in range(OUTPUT_HEIGHT):
            for x in range(OUTPUT_WIDTH):

                # print(frame[y][x][0], end=' ')

                response += str(frame[y][x][0])

                if x == OUTPUT_WIDTH - 1:
                    # print('\n')
                    response += '\n'

            print(response.replace('0', BLOCK_EMPTY).replace('255', BLOCK_FULL))

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

video.release()
