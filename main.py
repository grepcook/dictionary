#!/usr/bin/env python
# encoding: utf-8
import logging
import time
import os
import os.path
from multiprocessing import Process, Queue

from downloader import *

handle_table = dict(
    bing=Bing(),
    iciba=ICiBa(),
    youdao=YouDao()
)
queue_table = dict(
    bing=Queue(10),
    iciba=Queue(10),
    youdao=Queue(10)
)
def produce_word(site):
    in_name = os.path.join("input", "temp.txt")
    q = queue_table[site]
    with open(in_name, "rb") as fin:
        for w in fin:
            w = w.strip().decode("utf-8")
            logging.info("put word: %s on site: %s's queue" %(w, site))
            q.put(w)
    q.put("&end&")
    logging.info("put all words on site: %s's queue" %(site, ))

def fetch_process(site):
    # fetch word page on {site}
    # site in [bing, youdao, iciba]
    s = handle_table[site]
    q = queue_table[site]
    while True:
        w = q.get()
        if w == "&end&":
            break
        time.sleep(1)
        logging.info("fetching word: %s on site: %s" %(w, site))
        s.fetch(w)
    logging.info("completely fetched all words from site: %s" % (site, ))



if __name__ == "__main__":
    logging.basicConfig(level = logging.INFO,
                        format = '%(asctime)s:%(msecs)03d %(levelname)-8s %(message)s',
                        datefmt = '%m-%d %H:%M')
    logging.getLogger("requests.packages.urllib3.connectionpool").setLevel(logging.ERROR)
    producers = []
    consumers = []
    sites = ["bing", "iciba", "youdao"]
    for s in sites:
        dir = os.path.join("downloads", s)
        if not os.path.isdir(dir):
            os.mkdir(dir)
    for site in sites:
        p = Process(target=produce_word, args=(site,))
        c = Process(target=fetch_process, args=(site,))
        producers.append(p)
        consumers.append(c)
        p.start()
        c.start()
    for p in producers:
        p.join()
    for c in consumers:
        c.join()

    logging.info("All Done!")

