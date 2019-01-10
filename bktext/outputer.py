#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import json
from collections import OrderedDict
from argument_parser import ArgumentParser

class HtmlOutputer(object):
    def __init__(self):
        self.args = ArgumentParser()
        text_start = self.args.text_start
        self.file_count = int(text_start / 300000)
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas) % 350000 == 0:
            self.output_html()

    def output_html(self):
        result_file = open(self.args.text_output_path + str(self.file_count) + ".json", "w+", encoding='UTF-8')
        for data in self.datas:
            result = OrderedDict()
            result["title"] = data['title']
            result["subtitle"] = data['subtitle']
            result["syn"] = data['syn']
            result["infnames"] = data['infnames']
            result["infvalues"] = data['infvalues']
            result["summary"] = data['summary']
            result["content"] = data['content']
            result["tags"] = data['tags']
            result["url"] = data['url']
            result_file.write(json.dumps(result, ensure_ascii=False))
            result_file.write("\n")
        result_file.close()
        print("Output %d" % self.file_count)
        self.file_count += 1
        self.datas = []
