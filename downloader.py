# coding: utf-8
__author__ = 'junfeng7'
import logging
import os.path

import requests


__all__ = ["Bing", "YouDao", "ICiBa"]

DOWNLOADS = "downloads"

class Base():
    __DIR__ = None
    __URL__ = None
    __SESSION__ = requests.Session()
    def fetch(self, word):
        file_name = os.path.join(self.__DIR__, word + ".html")
        if os.path.isfile(file_name):
            return
        url = self.__URL__.format(word=word)
        headers = {}
        headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) Apple" \
                                "WebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.91 Safari/537.36"
        r = self.__SESSION__.get(url, headers=headers, timeout=20, allow_redirects=False)
        logging.info("real_url: " + r.url)
        if r.status_code == 200:
            with open(file_name, "wb") as fw:
                fw.write(r.text.encode("utf-8"))

class Bing(Base):
    __DIR__ = os.path.join(DOWNLOADS, "bing")
    __URL__ = "http://cn.bing.com/dict/search?q={word}"


class YouDao(Base):
    __DIR__ = os.path.join(DOWNLOADS, "youdao")
    __URL__ = "http://dict.youdao.com/search?q={word}"

class ICiBa(Base):
    __DIR__ = os.path.join(DOWNLOADS, "iciba")
    __URL__ = "http://www.iciba.com/{word}"