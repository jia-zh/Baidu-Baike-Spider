#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from urllib.parse import quote
from argument_parser import ArgumentParser

class UrlManager(object):
    def __init__(self):
        args = ArgumentParser()
        text_start = args.text_start
        text_end = args.text_end
        self.new_urls = set()
        key_words = [line.strip() for line in open(args.key_word_path, 'r', encoding='UTF-8')]
        for index in range(text_start, text_end):
            url = "https://baike.baidu.com/item/" + quote(key_words[index].strip())
            self.new_urls.add(url)
        key_words.clear()
        self.old_urls = set()
        self.fail_urls = set()
        self.fail_url_mark = True

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_old_url(self, url):
        if url is None:
            return
        if url not in self.new_urls:
            self.old_urls.add(url)

    def add_fail_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.fail_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            if url not in self.old_urls:
                self.new_urls.add(url)

    def has_new_url(self):
        if len(self.new_urls) != 0:
            return True
        elif self.fail_url_mark and len(self.fail_urls) != 0:
            self.new_urls = self.fail_urls.copy()
            self.fail_urls.clear()
            self.fail_url_mark = False
            return True
        else:
            return False

    def get_new_url(self):
        new_url = self.new_urls.pop()
        return new_url
