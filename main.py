# -*- coding: utf-8 -*-
# @Author  : LiWayne
# @Time    : 2020/11/21
from Controller import Discord_Change_Avatar
import os


class Main:
    def __init__(self):
        imagePath = fr'{os.getcwd()}\Data\Images\Test_Images'

        avatarChanger = Discord_Change_Avatar.Change_Avatar(imagePath)
        avatarChanger.start(True)


if __name__ == '__main__':
    obj = Main()
