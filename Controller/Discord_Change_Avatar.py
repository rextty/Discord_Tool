# -*- coding: utf-8 -*-
# @Author  : LiWayne
# @Time    : 2020/11/21
from Module import Discord_Avatar_Changer

import os
import time
import base64
import random
import threading
import configparser


class Change_Avatar:
    def __init__(self, imagesDir):
        self.imagesDir = self.convertPath(imagesDir)

        self.changer = None
        self.b64ImageList = []
        self.imageNameList = []

        self.__initFolder()
        self.__initConfig()

    def __initFolder(self):
        """
        To check images folder is exist, and put images name to list,
        and put base64 images to another list.
        :return:
        """
        if not os.path.isdir(self.imagesDir):
            print(f'Pls check the images path, {self.imagesDir}')
            return

        self.imageNameList = os.listdir(self.imagesDir)

        for image in self.imageNameList:
            self.b64ImageList.append(self.image2b64(f'{self.imagesDir}{image}'))
        print(f'Images init done, total {len(self.imageNameList)} images!\n{self.imageNameList}\n')

    def __initConfig(self):
        """
        Use configParser to load the user data of discord.
        """
        parser = configparser.ConfigParser()
        parser.read(f'{os.getcwd()}/Resources/user.ini')

        config = {
            'DATA': {
                'username': parser['DATA']['username'],
                'email': parser['DATA']['email'],
            },

            'HEADERS': {
                'cookie': parser['HEADERS']['cookie'],
                'user-agent': parser['HEADERS']['user-agent'],
                'authorization': parser['HEADERS']['authorization'],
                'x-super-properties': parser['HEADERS']['x-super-properties']
            }
        }

        self.changer = Discord_Avatar_Changer.Avatar_Changer(config)

    def start(self, randomBool: bool):
        """
        Use threading to start keep avatar changer.
        :param randomBool: Condition for random choice image.
        """
        print(f'Start discord avatar slide show, RandomMode: {randomBool}\n')

        if randomBool:
            threadStart = threading.Thread(target=self.__startRandomSlideShow)
        else:
            threadStart = threading.Thread(target=self.__startSlideShow)

        threadStart.start()

    def __startSlideShow(self):
        """
        Use while to loop do pre 5 min change avatar,
        and it's according to the order.
        """
        while 1:
            for index, b64image in enumerate(self.b64ImageList):
                self.changer.changeAvatar(b64image, self.imageNameList[index])
                time.sleep(300)

    def __startRandomSlideShow(self):
        """
        Same as above function,
        But it's random choice image.
        """
        while 1:
            randomInt = random.randint(0, len(self.b64ImageList)-1)
            self.changer.changeAvatar(self.b64ImageList[randomInt], self.imageNameList[randomInt])
            time.sleep(300)

    @staticmethod
    def image2b64(imagePath: str) -> str:
        """
        To convert image to base64.
        :param imagePath: path of images path.
        :rtype str: base64
        """
        with open(f'{imagePath}', 'rb') as image:
            b64Image = base64.b64encode(image.read())
        return b64Image.decode()

    @staticmethod
    def convertPath(path: str) -> str:
        """
        To convert the separator "\" to "/" and add the "/" to last.
        because 「 Backslashes in strings trigger escape characters 」
        so i make the simple function to solve the problem.
        :param path: just the path str.
        :rtype str: converted path.
        """
        if path == '':
            raise KeyError

        if path[-1] == '/' or path[-1] == '\\':
            return path.replace('\\', '/')
        else:
            return path.replace('\\', '/') + '/'


if __name__ == '__main__':
    # No mock test, cuz parameter from main
    obj = Change_Avatar("imagePath")
    obj.start(False)
