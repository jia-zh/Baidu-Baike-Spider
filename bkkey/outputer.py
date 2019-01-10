#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import json
from argument_parser import ArgumentParser

class HtmlOutputer(object):
    def __init__(self):
        self.datas = set([])

    def collect_data(self, data):
        if data is None:
            return
        for word in data:
            self.datas.add(word)

    def output_html(self):
        result_file = open("../data/keyword.txt", "a+", encoding='UTF-8')
        for data in self.datas:
            result_file.write(data)
            result_file.write("\n")
        result_file.close()
        print("Write Finish, Count:" + str(len(self.datas)))
        self.datas = []
