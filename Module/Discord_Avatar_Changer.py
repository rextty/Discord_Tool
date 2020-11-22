# -*- coding: utf-8 -*-
# @Author  : LiWayne
# @Time    : 2020/11/21
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests
import json


class Avatar_Changer:
    def __init__(self, config):

        self.data = {
            'username': config['DATA']['username'],
            'email': config['DATA']['email'],
            'password': '',
            'avatar': '',
            'discriminator': None,
            'new_password': None
        }

        self.headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-TW',
            'authorization': config['HEADERS']['authorization'],
            'content-length': '10653',
            'content-type': 'application/json',
            'cookie': config['HEADERS']['cookie'],
            'origin': 'https://discordapp.com',
            'referer': 'https://discordapp.com/channels/@me',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': config['HEADERS']['user-agent'],
            'x-super-properties': config['HEADERS']['x-super-properties']
        }

        self.apiUrl = 'https://discordapp.com/api/v8/users/@me'

        # Disable SSL error
        requests.packages.urllib3.disable_warnings()

    def changeAvatar(self, b64Image: str, imageName: str):
        """
        Send request to discord api for change avatar.
        :param b64Image: just the base64 of image
        :param imageName: to helpful you see the image what's change now.
        """
        self.data["avatar"] = fr'data:image/png;base64,{b64Image}'
        data = json.dumps(self.data)

        rs = requests.patch(url=self.apiUrl, headers=self.headers, data=data, verify=False)

        print(f'Responses: {rs.status_code}, Image: {imageName}')


if __name__ == '__main__':
    #  No mock test, cuz parameter from controller
    obj = Avatar_Changer("config")
    obj.changeAvatar('base64Image', 'imageName')
